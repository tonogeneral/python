# lO QUE HACE ESTE PROGRAMA ES BUSCAR LOS REGISTROS DENTRO DEL ARCHIVO MBOX.TXT
# EXTRAER LOS DOMINIOS DE LOS CORREOS QUE LO CONTIENE Y CONTARLOS
# LUEGO LOS REGISTR, CUENTA E INSERTA EN LA TABLA LLAMADA Counts EN
# UNA BASE DE DATOS SQLITE


import sqlite3
import re

conn = sqlite3.connect('top_org.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #print(pieces)
    email=list()
    email.append(pieces[1])
    #print(email)
    #dominio=list()
    for correo in email:
        org=correo.split("@")[1]
        print(org)
        #dominio.append(dom)
        #print(dominio)
        cur.execute('SELECT count FROM Counts WHERE org = ? order by count desc', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
            VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
conn.commit()
cur.close()

# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#for row in cur.execute(sqlstr):
#    print(str(row[0]), row[1])

#cur.close()
