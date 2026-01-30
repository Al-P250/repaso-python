minutos=int(input("Introduzca los minutos: "))

if minutos>60:
    horas=int(minutos/60)
    minutos=minutos-60*horas
    print(f"Son {horas} horas y {minutos} minutos")
else:
    print(f"Son {minutos} minutos")
