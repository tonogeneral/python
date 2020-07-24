#fname = input("Enter file name: ")
file=('romeo.txt')#dejo el archivo en duro
fh = open(file) #reeemplazar file por fh
lst = list(fh)
for line in lst:
    #print(line)
    #print(line.rstrip())
    #lista=(line.split())
    lista=lst.sort()
    olista=list(lista)
    #lista=(line.sort())
    #olista=(lista.sort())
    print(olista)
