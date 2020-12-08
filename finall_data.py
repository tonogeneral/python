import re
x='Tenemos edades entre los 1, 3, 15, 42 y 81 años'
y=re.findall('[1-9]+',x)
print(y)
