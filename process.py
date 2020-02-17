import glob  # biblioteca pra fazer o loop pela pasta
import time
import datetime  # bibliotecas de data e hora
import os
from pathlib import Path

pasta_origem = input("Digite o caminho completo da PASTA contendo os arquivos a serem analisados, "
                     "sem barra no final: ").replace('\\', '/')  # pede a pasta
Path(pasta_origem + "/proc").mkdir(parents=True, exist_ok=True)  # cria subpasta /proc
nvials = int(input("Digite a quantidade de vials distintos que foram testados: "))  # pede o número de vials
componda = input("Digite o comprimento de onda do cromatograma exportado, sem unidade: ")  # pede o comprimento de onda
nomeout = input("Digite o NOME base dos ARQUIVOS de destino, sem pasta nem extensão: ")  # base do nome dos outputs

string = 'Wavelength(nm)\t'+componda  # string pra ser buscada no arquivo
cnt = 0  # contador de linhas
linha = -1  # variável que salva o número da primeira linha do cromatograma
foundStart = False  # boolean pra determinar quando o loop chega nesta^ linha
foundEnd = False  # boolean pra determinar quando o loop chega ao final do cromatograma
output = []  # guarda o texto a ser despejado

for i in range(nvials):
    znum = str(i+1).zfill(3)  # transforma i em 00i
    print("ANALISANDO VIAL: " + znum)
    list_of_files = glob.glob(pasta_origem + "/*"+znum+"_*.txt")  # formato genérico da lista de arquivos
    progresso = 0
    for file_name in list_of_files:  # loop pelos arquivos
        progresso += 1
        print("Analisando arquivo " + str(progresso) + " de " + str(len(list_of_files)) + " (" + str(int(((progresso-1)/len(list_of_files))*100)) + "%)")
        unix = 0.0  # inicializa variável contendo o timestamp
        fl = open(file_name, 'r', encoding='latin-1')  # abre os arquivos do hplc em modo leitura
        fl2 = open(os.path.dirname(file_name) + "/proc/" + nomeout + znum + "_compil.txt", 'a', encoding='latin-1')  # cria novos arquivos em subpasta
        for line in fl:
            cnt += 1
            if line.startswith("Acquired\t"):  # procura a linha "Acquired: [data]"
                stamp = line[9:].rstrip()  # obtém a data+hora
                unix = time.mktime(datetime.datetime.strptime(stamp, "%d/%m/%Y %H:%M:%S").timetuple())  # converte pra epoch
            if string == line.rstrip():  # procura a string
                #print(cnt)  # imprime o número da linha (debug)
                linha = cnt+3  # define a var linha como três linhas a seguir
            if cnt == linha and foundStart is False:  # executa quando chega na primeira linha do cromatograma
                print("Cromatograma encontrado. Analisando...")
                foundStart = True
            if line in ['\n', '\r\n'] and foundStart is True and foundEnd is False:  # acha a última linha do cromatograma
                #print(cnt)  # imprime o número da linha (debug)
                foundEnd = True
            if foundStart is True and foundEnd is False:  # executa nas linhas do cromatograma
                output.append(line[8:].rstrip())  # adiciona a absorbância atual à var output
            if foundStart is True and foundEnd is True:  # ao chegar no final do cromatograma
                #print(output)  # imprime output (debug)
                z = 0  # comparador
                absint = 0
                for absorb in output:  # loop pela var output
                    absint = int(absorb)  # transforma em número
                    if absint/1000 > z:
                        z = absint/1000  # troca z pelo maior valor no output (div. por mil p/ corrigir)
                fl2.write(str(int(unix)) + "\t" + str(z) + "\n")  # escreve tempo e abs no arquivo e pula linha
                print("Sucesso!")
                output = []  # limpa output
                cnt = 0  # limpa cnt
                linha = -1  # limpa linha
                foundStart = False
                foundEnd = False  # reseta os found
        if progresso == len(list_of_files):
            print("Vial " + znum + " terminado!")
        fl.close()
        fl2.close()  # fecha os arquivos
