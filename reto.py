print("BIENVENIDOS")
print("JUGEMOS PIEDRA PAPEL O TIJERA")

nom1=input("Ingresa el nombre del primer jugador:")
nom2=input("Ingresa el nombre el nombre del segundo jugador:")


#MOSTRAR LAS 3 OPCIONES:PIEDRA, PAPEL, TIJERA
print ("1.-PIEDRA",
       "2.-PAPEL",
       "3.-TIJERA")

n1 = int(input(nom1 + ", ¿Qué eliges tú?"))  #PARA LEER DATOS NUMERICOS SE CONVIRTE A INT
n2 = int(input(nom2 + ", ¿Qué eliges tú?"))


#CONMBINACIONES
if n1 == 1:  # PIEDRA
    if n2 == 1:
        print("¡UPS! EMPATE")  
    elif n2 == 2:
        print("GANA PAPEL")  
    elif n2 == 3:
        print("GANA PIEDRA") 
elif n1 == 2:  #  PAPEL
    if n2 == 1:
        print("GANA PAPEL")  
    elif n2 == 2:
        print("¡UPS! EMPATE")  
    elif n2 == 3:
        print("GANA TIJERA")  
elif n1 == 3:  # TIJERA
    if n2 == 1:
        print("GANA PIEDRA")  
    elif n2 == 2:
        print("GANA TIJERA")  
    elif n2 == 3:
        print("¡UPS! EMPATE")  





    





