import re
#fname = input("Enter file name: ")
fname=("mbox-short.txt")
cuenta=dict()
correo=list() #inicializa diccionario
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    bigcount=None
    bigword=None
    texto = open(fname)
    for linea in texto:
        palabras=linea.split() #Separa en palabras el texto.
        palabra=linea.rstrip() #elimina espacios
        #if not line.startswith('From:'):continue #selecciona solo los que comiencen con From
        if re.search('^From:',palabra):
            #print(palabra)
            for palabra in palabras:
                cuenta[palabra]=cuenta.get(palabra,0)+1 #llena el diccionario con las tuplas palabras, cantidad
    for palabra,cantidad in cuenta.items():
        if palabra=='From:':
            continue
        elif bigcount is None or cantidad > bigcount:
            bigword=palabra
            bigcount=cantidad
except:
    print("Error")
print(bigword,bigcount)
