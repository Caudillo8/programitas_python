#IMPORTO RANDOM
import random
x=random.randint(30,40)#ELIJO LOS ENTRE NROS
#print(x) #LO USÉ PARA PROBAR CORRECTO E INCORRECTO


#PRESENTACION
nombre=input("ESCRIBE TU NOMBRE...")

for i in "Hola":
    print(f"{i}")
print(" ")
print(nombre.title())#PASO NOMBRE A TÍTULO
print(" ")
print("Adivina el número...")
print(" ")

#COMIENZO CON EL BUCLE WHILE Y DESDE ALLI LAS VARIABLES...
intento_2="s"
while intento_2=="s":
    intento =int(input("INGRESA UN NRO DEL 1 AL 100..."))
    if intento== x:
        print("¡CORRECTO! Has ganado $$$ 1 PALO VERDE!")
        break;#ES UN IF POSITIVO, CON BREAK EVITO QUE CONTINUE LEYENDO
    else:
        print("El nro era el...", x)#IMPRIMO EL NRO QUE SALIÓ
        print("Has fallado! ERES UN DESGRACIADO/A!!")
        x=random.randint(1,10)#Para que cambie cada vez
        #print(x)Prueba
        intento_2=input("¿Deseas volver a intentarlo?:s/n  ").lower()#PASA CUALQUIER RPTA A MINUSCULA
		
s
