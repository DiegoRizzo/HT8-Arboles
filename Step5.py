import sys
import graphviz
import BSTree
import SpTree
import RBTree


def draw_bst(graph, node):
    if node is None:
        return

    graph.node(str(node.val))

    if node.left:
        graph.edge(str(node.val), str(node.left.val))
        draw_bst(graph, node.left)

    if node.right:
        graph.edge(str(node.val), str(node.right.val))
        draw_bst(graph, node.right)


def draw_rbt(graph, node, null_node):
    if node == null_node:
        return

    color = "red" if node.color == 1 else "black"
    font = "white" if node.color == 0 else "black"
    graph.node(str(node.key), style="filled", fillcolor=color, fontcolor=font)

    if node.left != null_node:
        graph.edge(str(node.key), str(node.left.key))
        draw_rbt(graph, node.left, null_node)

    if node.right != null_node:
        graph.edge(str(node.key), str(node.right.key))
        draw_rbt(graph, node.right, null_node)


def run():
    sys.setrecursionlimit(5000)

    bst = BSTree.BSTree()
    spt = SpTree.SpTree()
    rbt = RBTree.RBTree()

    for proceso in range(1, 1001):
        bst.root = BSTree.BSTree.insert(bst.root, proceso)
        spt.insert(proceso)
        rbt.insert(proceso)

    _, pasos_bst = BSTree.BSTree.search(bst.root, 1000)
    _, pasos_spt = spt.search(1000)
    _, pasos_rbt = rbt.find(1000)

    print("Proceso buscado: 1000")
    print()
    print("BST:", pasos_bst + 1)
    print("Splay Tree:", pasos_spt)
    print("Red-Black Tree:", pasos_rbt)

    dot_bst = graphviz.Digraph(comment="BST Step 5")
    draw_bst(dot_bst, bst.root)
    dot_bst.render("step5_bst", format="png", view=False)

    print()
    print("step5_bst.png")


run()
