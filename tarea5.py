text = "X-DSPAM-Confidence:             0.8475";
posicion= text.find('0')
numero=text[posicion:posicion+6]
flotante=float(numero)
print(flotante,len(str(flotante)))
