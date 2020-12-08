#1. Leer el texto
fname=input("Ingrese archivo:")

#texto=open("mbox-short.txt")
try:
    texto=open(fname)
    contador=dict()
    lista=list()
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
    if (contador=={}):
        print("Archivo no contiene horas")
    else:
        for k,v in sorted(contador.items()):
            print(k,v)
except:
    print("Archivo Incorrecto")
    quit()
