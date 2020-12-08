fname=input("Ingrese archivo:")
texto=open(fname)
contador=dict()
for linea in texto:
    words=linea.split()#separa las palabras
    for word in words:
        contador[word]=contador.get(word,0)+1#las agrega a un diccionario y las cuenta
#print(contador)
lista=list()
arreglo=list()
'''for k,v in contador.items():
    newtup=(v,k) #da vuelta los valores
    #print(newtup)
    lista.append(newtup)#los agrega a una lista
    #print(lista)
'''
arreglo=sorted([(v,k) for k,v in contador.items()]) #da vuelta los valores agreagandolos a una lista
lista=sorted(arreglo,reverse=True)#ordena la lista por numero descendente
#print(lista)
for v,k in lista[:10]:# valor y key da vuelta los valores y muestra los primeros 10 de la lista ordenada
    print(k,v)
