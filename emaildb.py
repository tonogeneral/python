import sqlite3

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
    email = pieces[1]
    print(email)
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     #print(row)
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#
# cur.close()