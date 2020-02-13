import glob

list_of_files = glob.glob("D:/SALVA/Gustavob/Trabalhos/Ibilce/TCC/data/conc/proc/compil*.txt")
#string = 'Wavelength(nm)\t405'
#cnt = 0
#value = 3
num_list = []
#found = False
#found2 = False
#output = []

for file_name in list_of_files:
    fl = open(file_name, 'r')
    f2 = open(file_name.replace(".txt", "_tab.txt"), 'a')
    for line in fl:
        line.replace(" ", "\t")
    fl.close()
    f2.close()