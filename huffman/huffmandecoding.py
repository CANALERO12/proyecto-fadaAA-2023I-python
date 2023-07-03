"""
Proyecto final: FADA algoritmo Huffman

Integrantes y autores:
    2067805 Andres Mauricio Arias Cortes
    2067705 Santiago Marin Lozano
    2067784 Maher Lopez Rodriguez


Este modulo contiene la clase HuffmanDecoding

Clase que representa el algoritmo de Huffman
"""

class HuffmanDecoding:
    """
    Init de la clase HuffmanDecoding
    """

    def __init__(self):
        """
        Constructor de la clase HuffmanDecoding
        """
        self.tree = None

    def decode(self, cadena):
        """
        Método que decodifica una cadena de texto utilizando codificación Huffman
        Esto se explica en el siguiente if con los siguientes pasos:
        1. Si la cadena esta vacia entonces se retorna una cadena vacia
        2. Se crea una variable decoded_string que sera la cadena decodificada
        3. Se crea una variable current_node que sera el nodo actual
        4. Se recorre la cadena de bits
        5. Si el bit es 0 entonces se mueve a la izquierda
        6. Si el bit es 1 entonces se mueve a la derecha
        7. Si el nodo actual es una hoja entonces se agrega el caracter al decoded_string
        8. Se retorna la cadena decodificada
        """
        if cadena == "":
            return ""

        decoded_string = ""
        current_node = self.tree

        for bit in cadena:
            if bit == "0":
                current_node = current_node.left
            elif bit == "1":
                current_node = current_node.right

            if current_node.is_leaf():
                decoded_string += current_node.character
                current_node = self.tree

        return decoded_string
    
    def write_decoded_data_to_file(self, filename, decoded_data):
        """
        Método que escribe los datos decodificados en un archivo.
        """
        with open(filename, "w") as file:
            file.write(decoded_data)

    def read_decoded_data_from_file(self, filename):
        """
        Método que lee los datos decodificados de un archivo.
        """
        with open(filename, "r") as file:
            decoded_data = file.read()
        return decoded_data

