import re
#1. Ingresar y Abrir archivo
#fname=input("Ingrese nombre de archivo:")
#texto=open(fname)
#2 Leer archivo por linear
lista=list()

texto=open("regex_sum_768904.txt")
for linea in texto:
    #linea=linea.rstrip()
    linea=re.findall('[0-9]+',linea)
    if linea == []:continue
    suma=0
    for num in linea:
    #    numero=int(num)
    #    suma=numero+suma
        lista.append(num)
#print(lista,len(lista))
        suma=0
        for sum in lista:
            sum=int(sum)
            suma=sum+suma
print(suma)
