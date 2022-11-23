while True:
    import random

    user = input("Eliga piedra, papel o tijera: ")

    opciones = ["piedra", "papel", "tijera"]

    output = random.choice(opciones)
    print(f"Elecion del ordenador: {output}")

    if user == "piedra" and output == "papel":
        print("GANO EL ORDENADOR !!!! INTENTA NUEVAMENTE :)")
    elif user == "papel" and output == "tijera":
        print("GANO EL ORDENADOR !!!! INTENTA NUEVAMENTE :)")
    elif user == "tijera" and output == "piedra":
        print("GANO EL ORDENADOR !!!! INTENTA NUEVAMENTE :)")
    else:
        print("ERES EL GANADOR")