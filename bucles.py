seguir=True
resultado="no"
while seguir:
    continuacion=input("Introduzca la palabra salir si quiere cerrar la calculadora: ")
    if continuacion.upper()=="SALIR":
        seguir=False
    else:
        num1=int(input("Introduzca el pirmer número: "))
        operacion=input("Introduzca el símbolo de la operación(+,-,*,/): ")
        num2=int(input("Introduzca el segundo número: "))
        if operacion=="+":
            resultado=num1+num2
        elif operacion=="-":
            resultado=num1-num2
        elif operacion=="*":
            resultado=num1*num2
        elif operacion=="/":
            if num2==0:
                print("No se puede dividir entre 0")
                resultado = "no"
            else:
                resultado=num1/num2
        else:
            print("Símbolo no válido")
            resultado="no"
        if type(resultado)==int:
            print(resultado)