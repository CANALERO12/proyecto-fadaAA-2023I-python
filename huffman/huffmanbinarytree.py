"""
Proyecto final: FADA algoritmo Huffman

Integrantes y autores:
    2067805 Andres Mauricio Arias Cortes
    2067705 Santiago Marin Lozano
    2067784 Maher Lopez Rodriguez


Este modulo contiene la clase HuffmanBinaryTree


"""

class HuffmanBinaryTree:
    """
    Clase que implementa un árbol binario de Huffman
    """

    def __init__(self, character=None, frequency=0):
        """
        Constructor de la clase
        """
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def getNumberKey(self):
        """
        Retorna el valor de la llave,
        si es un string retorna -1, si es un
        numero retorna el numero.
        """
        if isinstance(self.character, str):
            return -1
        else:
            return self.character

    def getLeft(self):
        """
        Retorna el hijo izquierdo del arbol.
        """
        return self.left

    def getRight(self):
        """
        Retorna el hijo derecho del arbol.
        """
        return self.right

    def is_leaf(self):
        """
        Metodo que verifica si el nodo es una hoja
        """
        return self.left is None and self.right is None

