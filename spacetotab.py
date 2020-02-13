import glob
import time
import datetime

list_of_files = glob.glob("D:/SALVA/Gustavob/Trabalhos/Ibilce/TCC/data/pH/proc/compil*.txt")
#string = 'Wavelength(nm)\t405'
#cnt = 0
#value = 3
#num_list = []
#found = False
#found2 = False
#output = []

for file_name in list_of_files:
    fl = open(file_name, 'r')
    f2 = open(file_name.replace("com", "unix_com"), 'a')
    for line in fl:
        stamp = line[:19]
        #print(stamp)
        unix = time.mktime(datetime.datetime.strptime(stamp, "%d/%m/%Y %H:%M:%S").timetuple())
        converted = line.replace(line[:19], str(int(unix)))
        print(converted)
        f2.write(converted)
    fl.close()
    f2.close()