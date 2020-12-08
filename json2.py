import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter url: ')
    if len(address)< 1: break
    param=dict()
    param['address']=address
    url = urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh=urllib.request.urlopen(param)
    data=uh.read().decode
    print('Retrieved',len(data),'characters')

try:
    info = json.loads(data)
except:
    js=None

    print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
