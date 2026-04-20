from Node import Node

class BSTree:
    def __init__(self):
        self.root = None

    # Método de inserción
    def insert(root, key):

        # Si el árbol está vacío, devuelve un nuevo nodo
        if root is None:
            return Node(key)
        
        # Si el valor a insertar es igual al valor de la raíz, no se inserta y retorna la raíz
        if root.val == key:
            return root
        
        # Si el valor a insertar es mayor que el valor de la raíz, se repite el proceso de inserción para el subárbol derecho
        if root.val < key:
            root.right = BSTree.insert(root.right, key)

        # Si el valor a insertar es menor que el valor de la raíz, se repite el proceso de inserción para el subárbol izquierdo
        else:
            root.left = BSTree.insert(root.left, key)

        return root

    # Método de búsqueda
    def search(root, key):

        # Si el árbol está vacío o el valor de la raíz es igual al valor a buscar, devuelve la raíz
        if root is None or root.val == key:
            return root
        
        # Si el valor a buscar es mayor que el valor de la raíz, se repite el proceso de búsqueda para el subárbol derecho
        if root.val < key:
            return BSTree.search(root.right, key)
        
        # Si el valor a buscar es menor que el valor de la raíz, se repite el proceso de búsqueda para el subárbol izquierdo
        return BSTree.search(root.left, key)
    
    # Método para encontrar el sucesor de un nodo
    def get_successor(current):

        # Se hace la búsqueda en el subárbol derecho del nodo actual
        current = current.right

        # Mientras que el nodo actual no sea nulo y tenga un hijo izquierdo, se sigue buscando en el subárbol izquierdo
        while current is not None and current.left is not None:
            current = current.left

        # Al no tener más hijos a la izquierda, el nodo actual es el valor mínimo del subárbol derecho, es decir, el sucesor del nodo original
        return current
    
    # Método de eliminación
    def delete(root, key):

        # Si el árbol está vacío, devuelve la raíz
        if root is None:
            return root
        
        # Si el valor a eliminar es mayor que el valor de la raíz, se repite el proceso de eliminación para el subárbol derecho
        if root.val < key:
            root.right = BSTree.delete(root.right, key)

        # Si el valor a eliminar es menor que el valor de la raíz, se repite el proceso de eliminación para el subárbol izquierdo
        elif root.val > key:
            root.left = BSTree.delete(root.left, key)

        else:
            # Si el nodo a eliminar tiene uno o menos hijos, se elimina el nodo y se reemplaza por su hijo (si tiene uno)
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left

            # Si el nodo a eliminar tiene dos hijos, se encuentra el sucesor del nodo
            # Se reemplaza el valor del nodo a eliminar con el valor del sucesor
            successor = BSTree.get_successor(root)
            root.val = successor.val
            root.right = BSTree.delete(root.right, successor.val)
        
        return root

    # Método de recorrido in-order
    def in_order(root):

        # Si el árbol está vacío, no ocurre nada
        if root is None:
            return
        
        # Se recorre el subárbol izquierdo hasta llegar al valor mínimo
        # Se imprimen los valores de los nodos a medida que se recorren hasta llegar a la raíz del árbol
        # Se repite el proceso para el subárbol derecho
        BSTree.in_order(root.left)
        print(root.val, end=", ")
        BSTree.in_order(root.right)
        