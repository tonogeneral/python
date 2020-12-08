#Este programa muestra la dirección que más correos envió y cuantos

import re
############abrir fichero#################
#fname=input("Ingrese un nombre de archivo")
#######Dejamos el archivo seteado en duro mbox-short.txt#####################
fname=("mbox-short.txt")
archivo=open(fname)
lista=list()
cuenta=dict()#inicializa diccionario
for linea in archivo:
    #if not linea.startswith('From:'):continue
    if not re.findall('^From:',linea):continue
    linea=linea.rstrip()
    linea=linea.split()#Separa el archivo en arreglo de líneasprint(linea)
    #print(linea)
    #print(lista)
    for palabras in linea:
        cuenta[palabras]=cuenta.get(palabras,0)+1
#print(cuenta)
bigcuenta=None
bigpalabra=None
for palabra,cantidad in cuenta.items():
    if palabra =="From:":
        continue
    elif bigcuenta is None or cantidad > bigcuenta:
        bigpalabra=palabra
        bigcuenta=cantidad
print("La dirección que más correos ha enviado es:",bigpalabra,"con",bigcuenta,"correos")
