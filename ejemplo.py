def pregunta(respuesta):
    if respuesta.lower() == "bien":
        print("Me alegro que estes bien, Bendiciones")
    else:
        print("El dia todoavia no acaba, puede mejorar")    


persona = "Josue"
print("Hola" , persona , "como estas")
respuesta = input("Ingrese el estado de animo \n")
pregunta(respuesta)