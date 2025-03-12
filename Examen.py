#Gabriel Rodrigo Salvatierra

def buscarPalabra(objetivo, palabras):     
    for letra in palabras:
        if letra == objetivo:
            edades[letra] += 1
            return True
    return False
   
nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
        "Mengano": 0,
        "Fulano": 25,
        "Zutano": 50,
        "Perantano": 75
    }




def imprimirListaInversa(lista):
            return lista[::-1]
print(imprimirListaInversa(["Mengano", "Fulano", "Zutano", "Perantano"]))






