import glob  # biblioteca pra fazer o loop pela pasta
import time
import datetime  # bibliotecas de data e hora
from pathlib import Path

list_of_files = glob.glob("/home/gustavo/Documents/testeluan/*.txt")  # formato genérico da lista de arquivos
string = 'Wavelength(nm)\t405'  # string pra ser buscada no arquivo
cnt = 0  # contador de linhas
linha = -1  # variável que salva o número da primeira linha do cromatograma desejado
foundStart = False  # boolean pra determinar quando o loop chega nesta^ linha
foundEnd = False  # boolean pra determinar quando o loop chega ao final do cromatograma
output = []  # guarda o texto a ser despejado

for file_name in list_of_files:  # loop pelos arquivos
    fl = open(file_name, 'r')  # abre os arquivos do hplc em modo leitura
    fl2 = open(file_name.replace('/testeluan','/testeluan/proc'), 'w')  # cria novos arquivos em subpasta /proc
    for line in fl:
        cnt += 1
        if line.startswith("Acquired\t"):  # procura a linha "Acquired: [data]"
            stamp = line[9:]  # obtém a data+hora
            unix = time.mktime(datetime.datetime.strptime(stamp, "%d/%m/%Y %H:%M:%S").timetuple())  # converte pra unix epoch
            fl2.write(unix)  # escreve a data unix no novo arquivo
        if string == line.rstrip():  # procura a string
            print(cnt)  # imprime o número da linha
            linha = cnt+2  # define a var linha como duas linhas a seguir
        if cnt == linha and foundStart is False:  # executa quando chega na primeira linha do cromatograma
            print(line.rstrip())  # imprime o conteúdo da linha
            foundStart = True
        if line in ['\n', '\r\n'] and foundStart is True and foundEnd is False:  # procura a última linha do cromatograma
            print(cnt)  # imprime o nũmero da linha
            foundEnd = True
        if foundStart is True and foundEnd is False:  # executa nas linhas do cromatograma
            output.append(line)  # adiciona a linha atual à var output
            fl2.write(line)  # escreve a linha no arquivo
        if foundStart is True and foundEnd is True:  # ao chegar no final do cromatograma
            print(output)  # imprime output
            output = []  # limpa output
            cnt = 0  # limpa cnt
            linha = -1  # limpa linha
            foundStart = False
            foundEnd = False  # reseta os found
    fl.close()
    fl2.close()  # fecha os arquivos