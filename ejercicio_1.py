# Ejercicio 1 (30 puntos): Escribir un programa
#  que contenga una función que reciba una 
# lista de palabras y devuelva la más larga. 
# Imprimir por pantalla la palabra resultante.
def main():
    numero = int(input("Cuantas palabras tiene la lista: "))

    if numero < 1:
      print("Ingrese más de 1 palabra porfavor")
    else:
      lista = []
      palabramayor=0
      for i in range(numero):
        palabra = input(f"Dígame la palabra {i + 1}: ")
        palabra=palabra.replace(" ","")
        palabra=palabra.lower()
        lista += [palabra]
    print(f"La lista creada es: {lista}")

    for c in lista[0,numero]:
     if palabramayor<len(lista[c+1]):
            palabramayor=len(lista[c+1])
            palabranombre= lista[c+1]


    print(f"La lista creada es: {lista}")
    print("La palabra de largo es " + palabranombre+" ")
    print ("De largo de palabras: "+str(palabramayor))
    
if __name__== "__main__":
    main()  
