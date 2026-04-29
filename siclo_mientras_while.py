#nombre del alumno: rosa elena utuy santos 
#fecha de elaboración : 24 de abril de 2026
#Nombre del trabajo:salario semanal de obreros 

obreros = int(input("¿cuantos obreros hay ? : "))
 
i= 1

while i  <= obreros: 
    horas = float(input("horas trabajadas : "))
     
    if horas <=40: 
        salario = horas * 20
    else : 
        salario= (40*20)+ ((horas -40)*20)

        print("salario semanal : ", salario )

        i = i +1