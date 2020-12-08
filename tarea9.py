
fname = input("Enter file name: ")
#fname=("mbox-short.txt")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
    count=0
    for line in fh:
        line=line.rstrip()#quita espacios en blanco
        if not line.startswith('From:'):continue
        palabra=line.split()
        print(palabra[1])
        count=count+1
    print("There were",count,"lines in the file with From as the first word")
except:
    print("Ingrese un archivo valido")
    quit()
