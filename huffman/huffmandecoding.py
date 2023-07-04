class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.tree = None

    def decode(self, cadena, tree):
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
        current_node = tree

        for bit in cadena:
            if bit == "0":
                current_node = current_node.left
            elif bit == "1":
                current_node = current_node.right

            if current_node.is_leaf():
                decoded_string += current_node.key
                current_node = tree

        return decoded_string