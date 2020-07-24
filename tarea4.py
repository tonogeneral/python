largest = None
smallest = None
while True:
    num = input("Ingresa un numero Gabrielito: ")
    if num == "done" : break
    try:
        fnum=int(num)
    except:
        print("Número inválido")
        continue
    if smallest is None or largest is None:
        smallest=fnum
        largest=fnum
    elif fnum < smallest:
        smallest=fnum
    elif fnum > largest:
        largest=fnum
print("Maximum is", largest)
print("Minimum is", smallest)
