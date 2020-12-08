import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    xml = urllib.request.urlopen(url, context=ctx)
    data = xml.read()
    arbol = ET.fromstring(data)
    lst = arbol.findall('comments/comment')
    suma=0
    for count in lst:
        valor=count.find('count').text
        suma=int(valor)+suma
    print('Retrieved:',len(data))
    print('Count:',len(lst))
    print('Sum:',suma)


    #print("Count:",tree.findall('name').text)
