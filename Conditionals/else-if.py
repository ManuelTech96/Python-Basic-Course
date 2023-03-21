ingreso_mensual = 2500
gasto_mensual = 3000

#Ejemplo de if anidados y else if

if ingreso_mensual > 2000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en numeros rojos!")
    elif ingreso_mensual - gasto_mensual > 1000:
        print("Puedes ahorrar sin problema")
    else:
        print("Esperemos que no tengas un gasto extraordinario...")
        
elif ingreso_mensual > 1000:
    print("No esta mal")
else:
    print("Eres pobre")