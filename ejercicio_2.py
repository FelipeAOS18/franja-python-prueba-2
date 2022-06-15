# Ejercicio 2 (30 puntos): Escriba un programa que pida dos palabras
#  y diga si riman o no. Si coinciden las últimas tres letras tiene
#  que decir que riman. Si coinciden sólo las últimas dos tiene que 
# decir que riman un poco. Y si no coinciden, decir que no riman.
#  Validar que las palabras tengan al menos tres letras. 
# Nota: Utilizar slices

palabra1=input("Ingrese la Primera palabra: ")
palabra2=input("Ingrese la Segunda palabra: ")
palabra1=palabra1.replace(" ","")
palabra1=palabra1.lower()
palabra2=palabra2.replace(" ","")
palabra2=palabra2.lower()
if palabra1==palabra2:
    print("Ingrese distintas palabras")
elif len(palabra1)< 3 and 3 > len(palabra2):
    print("Ingrese palabras con más letras")
else:
    ult1 = palabra1[-3:] 
    ult2 = palabra2[-3:]
    ult3 = palabra1[-2:]
    ult4 = palabra2[-2:]
    rima1= palabra1[-1:-3]
    rima2= palabra2[-1:-3]

    if ult1 == ult2:
        print("Las palabras riman")
    elif ult3 == ult4:
        print("Las palabras riman un poco")
    elif rima1 == rima2 :
        print("Las palabras riman")
    else:
        print("Las palabras no riman")
