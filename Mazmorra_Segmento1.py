import random
separador = "\n--------------------"
print("JUEGO DE LA MAZMORRA\n"
      "--------------------\n"
      "\n"
      "Vos y tu compañero de celda se acaban de escapar de una prisión espacial, burlaron a los guardias y se dirigen al exterior.\n"
      "Entran ambos en una mazmorra controlada por mounstros alienígenas, uno de los guardias ataca a tu compañero, se lo lleva pero tú pasas desapercibido escondido en las sombras. \n"
      "El guardia se retira, es tu posibilidad de escapar. ¿Hacia dónde te diriges?\n")


opcion = input("A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo. Tú:\n"
                           "A - Eliges la puerta entreabierta.\n"
                           "B - Eliges la trampilla en el suelo.\n"
                           "Respuesta: ")

if opcion == "A": # SALES POR LA PUERTA
    print(separador)
    opcion = input("Pasas por la puerta y otro guardia te descubre, ¿qué haces?:\n"
          "A - Te haces el dormido.\n"
          "B - Sales corriendo hacia la siguiente puerta.\n"
          "Respuesta: ")

    if opcion == "A": # TE HACES EL DORMIDO
        print(separador)
        print("El guardia te atrapa y te encierran en una celda de máxima seguridad.\n"
              "FIN.")
    elif opcion == "B": # SALES CORRIENDO
        print(separador)
        opcion = input("Después de esa puerta encontrás una rana mutante que te obsequia un puñal casero hecho con la pata de una mesa. ¿Lo aceptás?\n"
              "A - Si.\n"
              "B - No.\n"
              "Respuesta: ")

        if opcion == "A":
            print(separador)
            opcion = input("Agarrás el puñal y avanzás. Hay dos pasillos circulares, no ves el final de ninguno de los dos. Uno está a la derecha y el otro a la izquierda, ¿cuál tomás?\n"
                           "A - Izquierda.\n"
                           "B - Derecha\n"
                           "Respuesta: ")

            if opcion == "A":
                print(separador)
                print("La habitación se hace cada vez más oscura, ves tan poco que caes por en un agujero con pinchos. Mueres lenta y dolorosamente.\n"
                      "FIN.")
            elif opcion == "B":
                print(separador)
                print("Encontrás la salida. En la puerta hay aparcada una nave espacial. Es tu dia de suerte, te subis, ves que las llaves están puestas y escapas hacia el horizonte.\n"
                    "FIN.")
            else:
                exit()
        elif opcion == "B":
            print(separador)
            print("La rana te devora, morís de forma rápida. El veneno hace efecto de manera instantánea.\n"
                "FIN.")
        else:
            exit()
    else:
        exit()

elif opcion == "B": # Opción sales por la trampilla.
    print(separador)
    opcion = input(
        "Caes en una zona inundada, el agua te llega hasta las rodillas.\n"
        "Avanzas durante media hora y finalmente llegas a una zona abierta, seca y con luz; parecen unas alcantarillas.\n"
        "Encontrás un palo largo, parece algo pesado pero podría servir. ¿Lo agarrás?\n"
        "A - Agarras el palo.\n"
        "B - No agarras el palo.\n"
        "Respuesta: ")

    palo = False
    if opcion == "A":
        palo = True
    elif opcion == "B":
        palo = False
    else:
        exit()

    num_random_rata = random.randint(1, 100)
    multip_rata = 13 * num_random_rata
    print(separador)
    opcion = int(input("Sigues adelante y te encuentras con una rata de dos metros. La rata te mira fijamente y te pregunta cuánto es 13 * {}?\n"
                            "Respuesta: ".format(num_random_rata)))

    if multip_rata == opcion:
        print(separador)
        print ("La rata te devora al instante. Demasiado inteligente.\n"
               "FIN.")
    else:
        print(separador)
        if palo == True:
            opcion = input("Fallaste, el resultado era {}. La rata abre una puerta ante vos y aparece un pasillo que lleva hasta la salida.\n"
                  "Lo recorres, llegas al final, el pasillo se derrumba detrás de tí. No hay salida más que una especie de boca de alcantarilla pero está lejos de tu alcance. ¿Qué haces?\n"
                       "A - Esperás a que alguien te rescate.\n"
                       "B - Usás el palo.\n"
                           "Respuesta: ".format(multip_rata))

            if opcion == "A":
               print("Un montón de ratas aparecen y te devoran vivo.\n"
                     "FIN.")
            elif opcion == "B":
                print("Usas el palo que agarraste antes para impulsarte. Conseguís trepar y salir. \n"
                      "En la puerta hay aparcada una nave espacial. Es tu dia de suerte, te subis, ves que las llaves están puestas y escapas hacia el horizonte.\n")
            else:
                exit()
        else:
            print(separador)
            opcion = input("Fallaste, el resultado era {}. La rata abre una puerta ante vos y aparece un pasillo que lleva hasta la salida.\n"
            "Lo recorres, llegas al final, el pasillo se derrumba detrás de tí. No hay salida más que una especie de boca de alcantarilla pero está lejos de tu alcance. ¿Qué haces?\n"
            "A - Esperás a que alguien te rescate.\n"
            "B - Probás saltar para subir.".format(multip_rata))

            if opcion == "A":
                print("Un montón de ratas aparecen y te devoran vivo.\n"
                      "FIN.")
            elif opcion == "B":
                print("No tenés como subir, si tan solo tuvieras un palo. Finalmente te quedas atrapado y las ratas te devoran vivo.\n"
                      "FIN.")
            else:
                exit()
else:
    exit()