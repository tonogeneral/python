
#fname = input("Enter file name: ")
fname=("mbox-short.txt")
cadena=list()
contador=dict()
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
    count=0
    for line in fh:
        line=line.rstrip()#quita espacios en blanco
        if not line.startswith('From:'):continue
        palabra=line.split()
        contador=palabra[1]
        print(contador)
        #for remitente in palabra:
        #    contador[remitente]=contador.get(remitente,0)+1
        #print(contador)
        #cadena=(palabra[1]) #llenado de lista con palabra
        #for word in cadena:
        #    contador[word]=contador.get(word,0)+1
    #print(contador)
    #print("There were",count,"lines in the file with From as the first word")
except:
    print("Ingrese un archivo valido")
    quit()
