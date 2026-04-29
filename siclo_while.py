#nombre del alumno: rosa elena utuy santos 
#fecha de elaboracion : 24 de abril de 2026
#Nombre del trabajo: Encontrar el numero mayor de n numeros 

numero = int(input("¿ cuantos numeros vas a ingresar : "))

i = 1

mayor = float(input("ingresa un numero: "))

while i < numero: 
    numero=float(input("ingresa otro numero : "))
    
    if numero > mayor: 
        mayor = numero

        i = i + 1
        print(" el numero mayor es : ", mayor )