cadena = input('Ingrese cadena:')
print(cadena[::-1])

def palindromo(cadena):
    if len(cadena)<=1:
        return cadena
    subcadena = ""
    for i in range(len(cadena)):
        for j in reversed(range(i,len(cadena))):
            if cadena[i] == cadena[j] and i!=j:
                if len(cadena[i:j+1]) > len(subcadena):
                    candidata = cadena[i:j+1]
                    candidata = candidata[::-1]
                    if cadena[i:j+1] == candidata:
                        subcadena = candidata
                    
    return subcadena

#print("Subcadena más larga:"+ palindromo(cadena))
