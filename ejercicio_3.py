# Ejercicio 3 (30 puntos): 
# Escribir una función que calcule el área de un círculo y 
# otra que calcule el volumen de un cilindro usando la primera función.
def area_circulo(radio):
    pi=3.1415
    area= pi* radio**2
    return area
def volumen_cilindro(radio, altura):
    volumen= 3.1415*(radio**2) * altura
    return volumen
def main():
    print(area_circulo(2))
    print(volumen_cilindro(2,6))
if __name__== '__main__':
    main()