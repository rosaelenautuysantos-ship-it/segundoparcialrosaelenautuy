#nombre del alumno: rosa elena utuy santos 
#fecha de elaboracion : 24 de abril de 2026
#Nombre del trabajo : descuento pr computadora 

cantidad= int(input("cuantas  coputadoras compraras ?"))

precio= 11000
total = cantidad*precio

# descuento

if cantidad < 5:
    descuento = total*0.10
elif cantidad >= 5 and cantidad <10 :
    descuento = total*0.20
else:
    descuento = total*0.40

    total_pagar = total - descuento
    
    print("total  sin descuanto : ", total)
    print("descuanto  aplicado: ", descuento)
    print("total a pagar con descuanto aplicado : ", total_pagar)