def computepay(h,r):
mes=40
he=1.5
try:
    fh=float(h)
    ft=float(r)
    fm=float(mes)
    fhe=float(he)
except:
    print("Error: Ingrese un entero")
    quit()
if h <= 40:
        total=fh*ft
        return(total)
    else:
        total=((fh-fm)*ft*fhe)+(fm*ft)
        return(total)

hour=input("Ingrese cantidad de horas trabajadas:")
tasa=input("Ingrese valor HH:")

p=computepay(fh,fr)
print("Pay",p)
