"""
Proyecto final: FADA algoritmo Huffman

Integrantes y autores:
    2067805 Andres Mauricio Arias Cortes
    2067705 Santiago Marin Lozano
    2067784 Maher Lopez Rodriguez


Este modulo contiene la clase HuffmanCoding

Clase que representa el algoritmo de Huffman
"""

from huffman.huffmanbinarytree import HuffmanBinaryTree

class HuffmanCoding:
    """
    Init de la clase HuffmanCoding
    """
    def __init__(self):
        self.tree = None
        self.table = {}

    def encode(self, cadena):
        """
        Método que codifica una cadena
        """
        if len(cadena) == 0:
            return ""
        # Verificamos si todas las cadenas son iguales
        if len(set(cadena)) == 1:
            return "0" * len(cadena)

        self.build_tree(cadena)
        self.build_table(self.tree, "")
        encoded_string = ""
        for char in cadena:
            if char in self.table:
                encoded_string += self.table[char]
            elif char == " ":
                encoded_string += "0"
            else:
                # Ignorar el carácter y continuar con el siguiente
                pass
        return encoded_string

    def get_tree(self):
        """
        Metodo que retorna el arbol de Huffman
        """
        return self.tree

    def get_table(self):
        """
        Metodo que retorna la tabla de Huffman
        """
        return self.table

    def get_summary(self, cadena=None):
        """
        Metodo que retorna un resumen de la compresion
        """
        compression_percentage = self.calculate_compression_percentage(cadena)
        num_nodes = self.count_nodes(self.tree)
        depth = self.calculate_depth(self.tree)
        summary = {
            "compression_percentage": compression_percentage,
            "num_nodes": num_nodes,
            "depth": depth
        }
        return summary

    def build_tree(self, cadena):
        """
        Metodo que construye el arbol de Huffman
        """
        frequency_dict = self.get_frequency_dict(cadena)
        nodes = self.create_leaf_nodes(frequency_dict)
        self.build_huffman_tree(nodes)

    def get_frequency_dict(self, cadena):
        """
        Metodo que retorna un diccionario con la frecuencia de cada caracter
        """
        frequency_dict = {}
        for char in cadena:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        return frequency_dict

    def create_leaf_nodes(self, frequency_dict):
        """
        Metodo que crea nodos hoja
        """
        nodes = []
        for char, frequency in frequency_dict.items():
            node = HuffmanBinaryTree(char, frequency)
            nodes.append(node)
        return nodes

    def build_huffman_tree(self, nodes):
        """
        Metodo que construye el arbol de Huffman
        """
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.frequency)
            left_child = nodes.pop(0)
            right_child = nodes.pop(0)
            parent_frequency = left_child.frequency + right_child.frequency
            parent = HuffmanBinaryTree(frequency=parent_frequency)
            parent.left = left_child
            parent.right = right_child
            nodes.append(parent)
        self.tree = nodes[0]

    def build_table(self, node, code):
        """
        Este metodo construye la tabla de Huffman
        """
        if node is None:
            return
        if node.is_leaf():
            self.table[node.key] = code
        self.build_table(node.left, code + "0")
        self.build_table(node.right, code + "1")

    def calculate_compression_percentage(self, cadena):
        """
        Metodo que calcula el porcentaje de compresion
        """
        original_size = 8 * len(cadena)
        encoded_string = self.encode(cadena)
        encoded_size = len(encoded_string)
        compression_percentage = (1 - encoded_size / original_size) * 100
        return compression_percentage

    def count_nodes(self, node):
        """
        Metodo que cuenta los nodos del arbol
        """
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def calculate_depth(self, node):
        if node is None:
            return 0
        left_depth = self.calculate_depth(node.left)
        right_depth = self.calculate_depth(node.right)
        return 1 + max(left_depth, right_depth)
       