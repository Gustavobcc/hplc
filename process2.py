import glob  # biblioteca pra fazer o loop pela pasta

list_of_files = glob.glob("G:/zLQBOA/Luan/*.txt")  # formato genérico da lista de arquivos
string = 'Wavelength(nm)\t405'  # string pra ser buscada no arquivo
cnt = 0  # contador de linhas
linha = -1  # variável que salva o número da primeira linha do cromatograma desejado
foundStart = False  # boolean pra determinar quando o loop chega nesta^ linha
foundEnd = False  # boolean pra determinar quando o loop chega ao final do cromatograma
output = []  # guarda o texto a ser despejado

for file_name in list_of_files:  #
    fl = open(file_name, 'r')
    f2 = open(file_name.replace('/Luan','/Luan/proc'), 'w')
    for line in fl:
        cnt += 1
        if line.startswith("Acquired\t"):
            f2.write(line[9:])
        if string == line.rstrip():
            print(cnt)
            linha = cnt+2
        if cnt == linha and foundStart is False:
            print(line.rstrip())
            foundStart = True
        if line in ['\n', '\r\n'] and foundStart is True and foundEnd is False:
            print(cnt)
            foundEnd = True
        if foundStart is True and foundEnd is False:
            output.append(line)
            f2.write(line)
        if foundStart is True and foundEnd is True:
            print(output)
            output = []
            cnt = 0
            linha = 0
            foundStart = False
            foundEnd = False
    fl.close()
    f2.close()