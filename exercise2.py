correos= open('mbox-short.txt')
count=0
for linea in correos:
    linea=linea.rstrip()
    if not linea.startswith('From:'):
        continue
    print(linea)
    count=count+1
print(count)





'''
#funcion que lee un archivo y lo guarda en una variable
fichero=correos.read()
#
muestra el largo del fichero
print(len(fichero))
#imprime linea a linea el fichero
for linea in correos:
    print(linea)
'''
