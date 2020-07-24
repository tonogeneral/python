# Use the file name mbox-short.txt as the file name
# Este programa realiza la validación del dígito verificador modulo 11.
#Prueba


while True:
    rut = input("Ingrese un rut valido: ")
    if rut=="salir":break
    try:
        num=rut.replace(".",'') #Quitamos puntos
        numero=num.find('-') #Encontramos posicion guion
        valor=num[0:numero] #Separamos valor
        ivalor=int(valor) #transformamos a entero
        svalor=str(ivalor)#seteamos como string ese valor
        digito=num[numero+1:numero+2] # guardamos el digito
        print(digito)
    except:
        print("RUT CON FORMATO INVALIDO")
        continue
    #reversamos valor numerico
    def reverse(svalor):
        rev = ''
        for i in range(len(svalor), 0, -1):
            rev += svalor[i-1]
        return rev

    trabajo=reverse(valor)
    suma=0
    mult=2
    for pos in trabajo:
        if mult <=7:
            suma=(int(pos)*mult)+suma
            mult=mult+1
            print(rut,reverse(svalor),suma)
        elif mult >7:
            mult=2
            suma=(int(pos)*mult)+suma
            mult=mult+1
            #print(rut,reverse(svalor),suma)
    modulo=suma%11
    DV=11-modulo
    print(DV)
    if DV <10:
        DV=str(DV)
    else:
        DV='K'
    if (DV==digito.upper()):
        print("RUT CORRECTO")
    else:
        print("RUT INCORRECTO")
