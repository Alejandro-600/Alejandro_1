def hablar():
    # esta funcion sirve para communicarse con el robot
    hab1 = print("Que quieres que diga el robot?")
    print("Pulse Q para que diga HOLA, W para que diga ADIOS y E para que diga QUE TAL. ")
    hola = input()
    if hola == "Q" or hola == "q":
        print("Hola soy el robot")
    if hola == "W" or hola == "w":
        print("Adios humano")
    if hola == "E" or hola == "e":
        print("Que tal estas?")
    Conversacion = input()

