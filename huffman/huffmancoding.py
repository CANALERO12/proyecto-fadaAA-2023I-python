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
        Método que codifica una cadena de texto utilizando codificación Huffman
        """
        if len(cadena) == 0:
            return ""
        
        #Verificamos si todas las cadenas son iguales
        if len(set(cadena)) == 1:

            """
            Si todas las cadenas son iguales entonces se retorna una cadena de ceros
            Ya qye analizamos el tamaño con len y luego con el set verificamos si todas las cadenas son iguales
            y nos damos cuenta que si todas las cadenas son iguales entonces el set solo tendra un elemento
            """
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
    

    def get_Tree(self):
        """
        Metodo que retorna el arbol de Huffman
        """
        return self.tree

    def get_Table(self):
        """
        Metodo que retorna la tabla de Huffman
        """
        return self.table

    def get_Summary(self, cadena=None):
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
            """
            for que recorre el diccionario de frecuencias y crea un nodo hoja por cada caracter
            y su frecuencia
            """
            node = HuffmanBinaryTree(char, frequency)
            nodes.append(node)
        return nodes

    def build_huffman_tree(self, nodes):
        """
        Metodo que construye el arbol de Huffman
        """
        while len(nodes) > 1:
            """
            while que se ejecuta mientras la lista de nodos tenga mas de un elemento

            Se ordenan los nodos por frecuencia de menor a mayor con el metodo sort y la funcion lambda
            el metododo sort recibe como parametro una funcion lambda que retorna la frecuencia de cada nodo
            ¿Que es el metodo sort?
            El metodo sort() ordena los elementos de una lista de menor a mayor, si se quiere ordenar de mayor a menor
            """
            nodes.sort(key=lambda x: x.frequency)

            """
            Se extraen los dos primeros nodos de la lista y se crea un nodo padre con la suma de las frecuencias de los el codigo de abajo explica como extrae los dos primeros nodos y empieza a crear el arbol a partir de los siguientes items que son la linea 116 a la 124 que lo que hace cada una es
            1. extraer los dos primeros nodos de la lista
            2. sumar las frecuencias de los dos nodos extraidos
            3. crear un nodo padre con la suma de las frecuencias de los dos nodos extraidos
            4. asignar el nodo padre como hijo izquierdo del primer nodo extraido
            5. asignar el nodo padre como hijo derecho del segundo nodo extraido
            6. agregar el nodo padre a la lista de nodos
            
            El punto 4 y 5 solo aplica para los dos primeros nodos extraidos, para los demas nodos extraidos solo se crea el nodo padre y se agrega a la lista de nodos.
            """
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
            """
            Explicacion del if con los siguientes items
            Si el nodo es hoja entonces se agrega el caracter y su codigo a la tabla de Huffman
            Si no es hoja entonces se llama recursivamente el metodo build_table con el hijo izquierdo y el codigo 0 y despues con el hijo derecho y el codigo 1.
            """
            self.table[node.character] = code
        self.build_table(node.left, code + "0")
        self.build_table(node.right, code + "1")

    def calculate_compression_percentage(self, cadena):
        """
        Metodo que calcula el porcentaje de compresion
        Esto quiere decir que lo que hace es a partir de la cadena original y la cadena codificada calcula el porcentaje de compresion, a lo que se refiere con porcentaje de compresion es a cuanto se redujo la cadena original con respecto a la cadena codificada.
        Ejemplo: si la cadena original es "hola mundo" y la cadena codificada es "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101" entonces el porcentaje de compresion es 50% porque la cadena original se redujo a la mitad.

        Cadena original: "hola mundo"
        Cadena codificada: "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"

        en las siguientes lineas hace el paso a paso asi:
        1. calcula el tamaño de la cadena original se multiplica por 8 porque cada caracter ocupa 8 bits
        2. calcula el tamaño de la cadena codificada porque cada caracter ocupa 1 bit
        3. calcula el porcentaje de compresion con la formula (1 - tamaño cadena codificada / tamaño cadena original) * 100 esto sale de la regla de 3 simple que se llega a esta conclusion porque si se multiplica por 100 se obtiene el porcentaje que nos piden como resultado.
        4. retorna el porcentaje de compresion
        5. fin retorna el porcentaje de compresion
        """
        original_size = 8 * len(cadena)
        encoded_string = self.encode(cadena)
        encoded_size = len(encoded_string)
        compression_percentage = (1 - encoded_size / original_size) * 100
        return compression_percentage

    def count_nodes(self, node):
        """
        Metodo que cuenta los nodos del arbol

        Explicacion del metodo y que hace el if:
        Si el nodo es nulo entonces retorna 0
        Si no es nulo entonces retorna 1 + el metodo recursivo count_nodes con el hijo izquierdo y el hijo derecho, esto se hace para contar los nodos de cada subarbol y sumarlos.

        por ejemplo si se tiene el siguiente arbol:
        1
       
        2   3
        
        4   5   6
       
        7   8   9

        entonces el metodo count_nodes retorna 9 porque cuenta todos los nodos del arbol
        """
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def calculate_depth(self, node):
        """
        Metodo que calcula la profundidad del arbol

        Explicacion del metodo y que hace el if:
        Si el nodo es nulo entonces retorna 0

        Si no es nulo entonces retorna 1 + el maximo entre el metodo recursivo calculate_depth con el hijo izquierdo y el hijo derecho, esto se hace para calcular la profundidad de cada subarbol y retornar la profundidad maxima.

        por ejemplo si se tiene el siguiente arbol:
        1
        
        2   3
        
        4   5   6
       
        7   8   9

        entonces el metodo calculate_depth retorna 4 porque es la profundidad maxima del arbol
        """
        if node is None:
            return 0
        left_depth = self.calculate_depth(node.left)
        right_depth = self.calculate_depth(node.right)
        return 1 + max(left_depth, right_depth)
    
    def write_encoded_data_to_file(self, filename, encoded_data):
        """
        Método que escribe los datos codificados en un archivo.
        """
        with open(filename, "wb") as file:
            encoded_bytes = bytearray(encoded_data, "utf-8")
            file.write(encoded_bytes)

    def read_encoded_data_from_file(self, filename):
        """
        Método que lee los datos codificados de un archivo.
        """
        with open(filename, "rb") as file:
            encoded_bytes = file.read()
            encoded_data = list(encoded_bytes)
        return encoded_data

