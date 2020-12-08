import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ingresar archivos:
#http://py4e-data.dr-chuck.net/comments_42.json
#http://py4e-data.dr-chuck.net/comments_768909.json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter url: ')
    if len(address)< 1: break
    param=dict()
    param['address']=address
    #url = urllib.parse.urlencode(param)
    print('Retrieving',address)
    uh=urllib.request.urlopen(address)
    data=uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js=None

    listado=len(js['comments'])
    #print(json.dumps(js, indent=4))
    print('count',listado)

    suma=0
    i=0
    for linea in js['comments']:
        numero=js['comments'][i]['count']
        #print(numero)
        suma=numero+suma
        #print(i)
        i=i+1
    print('sum',suma)
