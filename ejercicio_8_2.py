fname=input("Ingrese un nambre de archivo:")
texto=open(fname) #abre archivo
cuenta=dict() #inicializa diccionario
for linea in texto:
    palabras=linea.split() #Separa en palabras las líneas del texto.
    #print(palabras)
    for palabra in palabras:
        cuenta[palabra]=cuenta.get(palabra,0)+1 #llena el diccionario con las tuplas palabras, cantidad
#print(cuenta)

bigcount=None
bigword=None
for palabra,cantidad in cuenta.items(): #busca palabra e indice en diccionario
    if bigcount is None or cantidad > bigcount:
        bigword=palabra
        bigcount=cantidad
print(bigword,bigcount)
