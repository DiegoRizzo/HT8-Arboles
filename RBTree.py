from RBNode import RBNode

class RBTree:
    def __init__(self):
        self.nodoFantasma = RBNode(0) # Nodo que representa los nodos nulos
        self.nodoFantasma.color = 0
        self.root = self.nodoFantasma
    
    def left_rotate(self, x):
        y = x.right # y es el hijo derecho de x
        x.right = y.left # El hijo izquierdo de y se convierte en el hijo derecho de x

        # Si el hijo izquierdo de y no es el nodo fantasma, actualizamos su padre
        if y.left != self.nodoFantasma:
            y.left.parent = x
        
        y.parent = x.parent # El padre de y se convierte en el padre de x

        # Si el padre de x no existe, entonces y se convierte en la raíz del árbol
        if x.parent == None:
            self.root = y
        
        # Si x es hijo izquierdo, entonces y se convierte en el hijo izquierdo del padre de x
        elif x == x.parent.left:
            x.parent.left = y
        
        # Si x es hijo derecho, entonces y se convierte en el hijo derecho del padre de x
        else:
            x.parent.right = y
        
        y.left = x # x se convierte en el hijo izquierdo de y
        x.parent = y # El padre de x se convierte en y

    def right_rotate(self, y):
        x = y.left # x es el hijo izquierdo de y
        y.left = x.right # El hijo derecho de x se convierte en el hijo izquierdo de y

        # Si el hijo derecho de x no es el nodo fantasma, actualizamos su padre
        if x.right != self.nodoFantasma:
            x.right.parent = y
        
        x.parent = y.parent # El padre de x se convierte en el padre de y

        # Si el padre de y no existe, entonces x se convierte en la raíz del árbol
        if y.parent == None:
            self.root = x
        
        # Si y es hijo derecho, entonces x se convierte en el hijo derecho del padre de y
        elif y == y.parent.right:
            y.parent.right = x
        
        # Si y es hijo izquierdo, entonces x se convierte en el hijo derecho del padre de y
        else:
            y.parent.left = x
        
        x.right = y # y se convierte en el hijo derecho de x
        y.parent = x # El padre de y se convierte en x
    
    def arreglar(self, k):
        while k.parent.color == 1: # Mientras mi padre sea Rojo

            if k.parent == k.parent.parent.left: # Si mi padre es hijo izquerdo
                u = k.parent.parent.right # Mi tío

                if u.color == 1: # CASO 1: Mi tío es Rojo
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent # Seguimos revisando al abuelo
                
                else:
                    if k == k.parent.right: # CASO 2: Triángulo
                        k = k.parent
                        self.left_rotate(k) # Rotación a la izquierda del padre
                    
                    # CASO 3: Línea
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent) # Rotación a la derecha del abuelo
            
            else: # Simetría: El padre es hijo derecho
                u = k.parent.parent.left # Mi tío

                if u.color == 1: # CASO 1: Mi tío es Rojo
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                
                else:
                    if k == k.parent.left: # CASO 2: Triángulo
                        k = k.parent
                        self.right_rotate(k) # Rotación a la derecha del padre
                    
                    # CASO 3: Línea
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent) # Rotación a la izquierda del abuelo
            
            if k == self.root: # Si llegamos a la raíz, no hay nada más que revisar
                break
        self.root.color = 0 # Raíz siempre Negra
    
    def insert(self, key):
        # 1) Inserción normal BST
        nuevo_nodo = RBNode(key)
        nuevo_nodo.parent = None
        nuevo_nodo.left = self.nodoFantasma
        nuevo_nodo.right = self.nodoFantasma
        nuevo_nodo.color = 1

        padre = None
        actual = self.root

        while actual != self.nodoFantasma:
            padre = actual

            if nuevo_nodo.key < actual.key:
                actual = actual.left
            else:
                actual = actual.right
        
        nuevo_nodo.parent = padre

        if padre == None:
            self.root = nuevo_nodo
        elif nuevo_nodo.key < padre.key:
            padre.left = nuevo_nodo
        else:
            padre.right = nuevo_nodo
        
        # Si es la raíz, debe quedar negra
        if nuevo_nodo.parent == None:
            nuevo_nodo.color = 0
            return

        # Si no hay abuelo, no hay nada que arreglar
        if nuevo_nodo.parent.parent == None:
            return
        
        # 2) Reparar propiedades Rojo-Negro
        self.arreglar(nuevo_nodo)
    
    def find(self, key):
        actual = self.root
        comparaciones = 0

        while actual != self.nodoFantasma:
            comparaciones += 1

            if key == actual.key:
                return actual, comparaciones

            if key < actual.key:
                actual = actual.left
            
            else:
                actual = actual.right
        
        return None, comparaciones
    
    def niveles(self):
        if self.root == self.nodoFantasma:
            return 0
        
        max_nivel = 0
        pila = [(self.root, 1)]

        while pila:
            nodo, nivel = pila.pop()

            if nivel > max_nivel:
                max_nivel = nivel
            
            if nodo.left != self.nodoFantasma:
                pila.append((nodo.left, nivel + 1))

            if nodo.right != self.nodoFantasma:
                pila.append((nodo.right, nivel + 1))
        
        return max_nivel
