custom={}

def validar(var, co):
    try:
        var(co)
        print(co)
    except ValueError:
        print("Error")

while True:
    var=input("Introduzca variable: ")
    cosa=input("Introduce cosa:")
    validar(var,cosa)