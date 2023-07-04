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
    Clase que representa un arbol binario de Huffman
    """

    def __init__(self, key=None, frequency=0):
        """
        Init de la clase HuffmanBinaryTree
        """
        self.key = key
        self.frequency = frequency
        self.left = None
        self.right = None

    def get_left(self):
        """
        Metodo que retorna el hijo izquierdo del nodo
        """
        return self.left
    
    def get_right(self):
        """
        Metodo que retorna el hijo derecho del nodo
        """
        return self.right
    
    def get_number_key(self):
        """
        Metodo que retorna el valor numerico del nodo
        """
        if isinstance(self.key, int):
            return self.key
        else:
            return -1

    def is_leaf(self):
        """
        Metodo que verifica si el nodo es una hoja
        """
        return self.left is None and self.right is None
