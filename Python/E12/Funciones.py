import Español
def crackeo(mensaje):
    ABECEDARIO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for key in range(1, len(ABECEDARIO)):
        trad = ''


        for abc in mensaje:
            if abc in ABECEDARIO:
                abcIndex = ABECEDARIO.find(abc)
                tradIndex = abcIndex - key

                if tradIndex < 0:
                    tradIndex = tradIndex + len(ABECEDARIO)

                trad = trad + ABECEDARIO[tradIndex]

            else:
                trad = trad + abc


        if Español.isSpanish(trad):
            print("Key:", str(key)+". Mensaje encontrado: "+trad[:100])
            print("Válido para idioma español")
            print()

def cifrado(mensaje, llave):
    message = mensaje
    espacios = 1
    while espacios > 0:
        clave = llave
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    ABECEDARIO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    trad = ''

    for abc in message:
        if abc in ABECEDARIO:
            abcIndex = ABECEDARIO.find(abc)
            tradIndex = abcIndex + key
            
            if tradIndex >= len(ABECEDARIO):
                tradIndex = tradIndex - len(ABECEDARIO)
            elif tradIndex < 0:
                tradIndex = tradIndex + len(ABECEDARIO)

            trad = trad + ABECEDARIO[tradIndex]
        else:
            trad = trad + abc

    print("Mensaje cifrado:", trad)

def descifrado(mensaje, llave):
    message = mensaje
    espacios = 1
    while espacios > 0:
        clave = llave
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    ABECEDARIO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    trad = ''

    for abc in message:
        if abc in ABECEDARIO:
            abcIndex = ABECEDARIO.find(abc)
            tradIndex = abcIndex - key
            
            if tradIndex >= len(ABECEDARIO):
                tradIndex = tradIndex - len(ABECEDARIO)
            elif tradIndex < 0:
                tradIndex = tradIndex + len(ABECEDARIO)

            trad = trad + ABECEDARIO[tradIndex]
        else:
            trad = trad + abc

    print("Mensaje descifrado:", trad)

