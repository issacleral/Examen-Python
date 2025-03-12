#Gabriel Rodrigo Salvatierra

def buscarPalabra(objetivo, palabras):

    nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
    edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
        }
    
    for buscar in palabras:
        if objetivo in palabras:
            nombres[edades] += 1

        return nombres

print(buscarPalabra("Mengano"))



def imprimirListaInversa(lista):
         return lista[::-1]
print(imprimirListaInversa(["Mengano", "Fulano", "Zutano", "Perantano"]))
