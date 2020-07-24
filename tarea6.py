# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    archivo=open(fname)
except:
    print("Ingrese un nombre de archivo valido")
    quit()

for linea in archivo:
    linea=linea.rstrip()
    print(linea.upper())
