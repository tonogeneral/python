# Use the file name mbox-short.txt as the file name
archivo = input("Enter file name: ")
try:
    texto = open(archivo)
except:
    print=("Ingrese un archivo correcto")
    quit()
count=0
total=0
for line in texto:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    posicion=line.find(':')
    numero=line[posicion+2:posicion+8]
    flotante=float(numero)
    total=total+flotante
    count=count+1
print("X-DSPAM-Confidence:",round(total/count,12))
