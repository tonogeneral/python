# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#1. Importar urllib y los conectores ssl

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#2. Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#3.Guardar los parámetros de entrada: url, cant y posición
url = input('Enter url:')
position=input('Enter position:')
count=input('Enter count:')
posi=int(position)-1
cuenta=int(count)+1
list_pag=list()
urls=list()
urls.append(url)
#print(listita[0])
#4. Crear un ciclo que ejecute el numero de veces del contador y busque la url de la posicion
#listita=['http://py4e-data.dr-chuck.net/known_by_Fikret.html','http://py4e-data.dr-chuck.net/known_by_Montgomery.html','http://py4e-data.dr-chuck.net/known_by_Mhairade.html','http://py4e-data.dr-chuck.net/known_by_Butchi.html','http://py4e-data.dr-chuck.net/known_by_Anayah.html']
#Ejecuta 3 veces la sentencia
for i in range(cuenta):
    print("Retrieving:",urls[i])
    html = urlopen(urls[i], context=ctx).read()
    #print(html)
    #5.Parsear con Beautiful soup
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    #page=urls[i]
    for tag in tags:
        #print(tag.get('href', None))
        list_pag.append(tag.get('href', None))
    urls.append(list_pag[posi])
    list_pag=[]
