#Nombre del alumno: Rosa Elena Utuy Santos 
#Fecha : 22 de abril del 2026 
#nombre del trabajo: descuento en la llantera 
while True:
    try:
        compra_del_producto =int(input("ingresa la cantidad de llanatas compradas : "))

        print("Cantida de llantas copradas",compra_del_producto)
        if compra_del_producto < 5:
            valor_llanta=300
            print("aplica la promocion ")
        elif compra_del_producto >= 5 and compra_del_producto <=10 :
            valor_llanta = 250
            print("aplica el escuento")
            
        elif  compra_del_producto > 10 : 
            valor_llanta = 200
            print("aplica la promocion")
        break    
    except ValueError:
        print("ERROR, ingrese un valor entero")
total_a_pagar = compra_del_producto * valor_llanta
print("cantidad a pagar" , total_a_pagar) 
    