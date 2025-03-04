def carga_de_datos():
    lista_de_datos_guardados=[]
    print ("Ingrese nombre de usuario y contraseña")
    print ("El programa se cierra al poner en ""SALIR")
    nombre_usuario=input("Ingrese nombre usuario: ")

    while (nombre_usuario.lower() != "salir"):
        contraseña=input("Ingrese contraseña: ")
        for registro in lista_de_datos_guardados:
            if registro[0]==nombre_usuario and registro[1]==contraseña:
                print ("¡Nombre de usuario y contraseña existe!")
                break
        else:
            lista_de_datos_guardados.append([nombre_usuario,contraseña])
            print ("¡Se guardo con exito!")
        nombre_usuario=input("Quiere ingresar un nuevo usuario? Si no quiere, ingrese Salir ")
    return lista_de_datos_guardados




def imprimir_usuarios(lista_datos):
    print ("Los datos guardados son")
    for datos in lista_datos:
        print ("Nombre de usuario ", datos[0],", ""Contraseña", datos[1])




def login(lista_datos):
    nombre_usuario=input("Ingrese nombre de usuario: ")
    contraseña=input("Ingrese contraseña: ")
    for datos in lista_datos:
        if datos[0]==nombre_usuario and datos[1]==contraseña:
            print ("¡Ingresaste al sistema!")
            break
        elif datos[0]==nombre_usuario and datos[1]!=contraseña:
            print ("¡Contraseña incorrecta!")
            break
        elif datos[0]==nombre_usuario and datos[1]!=contraseña:
            print ("¡Contraseña incorrecta!")
    else:
        print ("Nombre de usuario y no existen")


x=carga_de_datos()
imprimir_usuarios(x)
login(x)