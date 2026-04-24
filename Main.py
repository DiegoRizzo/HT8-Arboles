import BSTree
import SpTree
import graphviz
import numpy as np
import matplotlib.pyplot as plt
import ProcessData

def run():
    # Crear un árbol binario de búsqueda y un Splay Tree
    bst = BSTree.BSTree()
    spt = SpTree.SpTree()

    # Insertar los mismos 1000 procesos que se usan en el experimento
    for key in ProcessData.get_processes():
        bst.root = BSTree.BSTree.insert(bst.root, key)
    
    # Usar Graphviz para genrar el gráfico del árbol
    dot = graphviz.Digraph(comment="Binary Search Tree")
    
    # Función para agregar nodos al gráfico
    def add_nodes(graph, node):
        if node:
            graph.node(str(node.val))
            if node.left:
                graph.edge(str(node.val), str(node.left.val))
                add_nodes(graph, node.left)
            if node.right:
                graph.edge(str(node.val), str(node.right.val))
                add_nodes(graph, node.right)
    
    # Agregar todos los nodos del BST al gráfico
    add_nodes(dot, bst.root)
    
    # Renderizar el gráfico y guardarlo como imagen PNG
    dot.render('bst_graph', format='png', view=True)
    print("El gráfico del árbol binario de búsqueda se ha generado y guardado como 'bst_graph.png'")

run()
