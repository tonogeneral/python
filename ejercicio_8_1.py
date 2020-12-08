fname=input("Ingrese un nambre de archivo:")
texto=open(fname)
cuenta=dict()
for linea in texto:
    palabras=linea.split() #Separa en palabras el texto.
    for palabra in palabras:
        cuenta[palabra]=cuenta.get(palabra,0)+1
print(cuenta)
