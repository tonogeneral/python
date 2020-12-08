#Este archivo cuenta la cantidad de emails que llegaron en HH hora


#1. Leer el texto
#fname=input("Ingrese archivo")
#texto=open(fname)



texto=open("mbox-short.txt")
contador=dict()
lista=list()
arreglo=list()
for linea in texto:
#2. Seleccionar sólo las líneas que tengan From:
    if not linea.startswith('From '):continue
    linea=linea.rstrip()
    #print(linea)
#3. Separar por líneas
#4. Dividir split por palabras (From,correo,hora)
    linea=linea.split()
#5. Seleccionar la hora ('from, stephen@uct.ca.za,Sat,Jan,5,09:14:16,2008')
    hora=linea[5]
#6.Seleccionar solo el número de horas
    hora=hora[:2]
    lista=[hora]
    #print(lista)
    for hr in lista:
        contador[hr]=contador.get(hr,0)+1
#contador=sorted(contador,reverse=True)
for k,v in sorted(contador.items()):
    print(k,v)




'''
#6.Separar por dos puntos b=lista; re.split('[-:]', b)
#6. Contar el numero de horas
for linea in texto:
    words=linea.split()#separa las palabras
    for word in words:
        contador[word]=contador.get(word,0)+1#las agrega a un diccionario y las cuenta
        (05 01)
'''
#7. Ordenar de menor a mayor
'''
lista=sorted(arreglo,reverse=True)
'''
