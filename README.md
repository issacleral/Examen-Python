# Examen-Python

- La funcion  ```buscarPalabra ``` es para buscar el nombre de la persona y debajo te imprime la edad del usuario que buscaste.

    ```Python
    Codigo:

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
    ```


- La funcion  ```imprimirListaInversa ``` hace que de los nombres de la lista se Imprimar al reves.

     ```Python
     Codigo:

     def imprimirListaInversa(lista):
         return lista[::-1]
    print(imprimirListaInversa(["Mengano", "Fulano", "Zutano", "Perantano"]))
    ```

    <br>
    <br>
    <br>
    <br>

    ## De Gabriel Rodrigo Salvatierra Callapino: