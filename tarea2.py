nota=input("Ingrese nota:")
try:
    fn=float(nota)
except:
    print("Ingrese valor entre 0.0 y 1.0")
    quit()
if fn >= 0.9:
    calif="A"
elif fn < 0.9 and fn >= 0.8:
    calif="B"
elif fn < 0.8 and fn >= 0.7:
    calif="C"
elif fn < 0.7 and fn >= 0.6:
    calif="D"
elif fn < 0.6:
    calif="F"
print(calif)
