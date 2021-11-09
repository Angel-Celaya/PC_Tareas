import argparse
from Funciones import crackeo, cifrado, descifrado
if __name__ == '__main__':
    
    description = """Tareas:
    "c" o "C": Cifrado
    "d" o "D": Descifrado
    "crack" o "CRACK": Crackeo


    Ejemplos de uso:
        + Mensaje ingresado:
            -msg [mensaje] -mod cif -key
            -msg [mensaje] -mod des -key
            -msg [mensaje] -mod cr """
    parser = argparse.ArgumentParser(description='Crackeo de mensajes cifrado Cesar', epilog=description,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-msg', dest='msg', type=str,
                        help='Mensaje por modificar',
                        required=True)
    parser.add_argument('-mod', dest='mod', type=str,
                        help='Accion por realizar: cifrar-descifrar-crackear',
                        required=True)
    parser.add_argument('-key', dest='key',
                        help='Palabra clave para cifrar o descifrar si se selecciona cif o des')
    args = parser.parse_args()

mensaje = args.msg
tipo = args.mod
if args.key:
    llave = args.key

resultado = 0

if tipo == "crack" or tipo == "CRACK":
    try:
        crackeo(mensaje)
    except Exception as e:
        print("Error no se pudo crackear:", e)
elif tipo == "c" or tipo == "C":
    try:
        cifrado(mensaje, llave)
    except Exception as e:
        print("Error no se pudo cifrar:", e)
elif tipo == "d" or tipo == "D":
    try:
        descifrado(mensaje, llave)
    except Exception as e:
        print("Error no se pudo descifrar:", e)
else:
    print("El argumento no existe, recuerde que es crack, c o d")
