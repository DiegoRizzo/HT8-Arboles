import BSTree
import SpTree
import RBTree
import matplotlib.pyplot as plt
import ProcessData


def run():
    bst = BSTree.BSTree()
    spt = SpTree.SpTree()
    rbt = RBTree.RBTree()

    procesos = ProcessData.get_processes()

    for proceso in procesos:
        bst.root = BSTree.BSTree.insert(bst.root, proceso)
        spt.insert(proceso)
        rbt.insert(proceso)

    buscados = ProcessData.get_searches()

    iteraciones_bst = []
    iteraciones_spt = []
    iteraciones_rbt = []

    for proceso in buscados:
        _, pasos_bst = BSTree.BSTree.search(bst.root, proceso)
        _, pasos_spt = spt.search(proceso)
        _, pasos_rbt = rbt.find(proceso)

        iteraciones_bst.append(pasos_bst + 1)
        iteraciones_spt.append(pasos_spt)
        iteraciones_rbt.append(pasos_rbt)

    print("Procesos buscados:")
    print(buscados)
    print()

    print("BST")
    print("Iteraciones:", iteraciones_bst)
    print("Total:", sum(iteraciones_bst))
    print("Promedio:", sum(iteraciones_bst) / len(iteraciones_bst))
    print()

    print("Splay Tree")
    print("Iteraciones:", iteraciones_spt)
    print("Total:", sum(iteraciones_spt))
    print("Promedio:", sum(iteraciones_spt) / len(iteraciones_spt))
    print()

    print("Red-Black Tree")
    print("Iteraciones:", iteraciones_rbt)
    print("Total:", sum(iteraciones_rbt))
    print("Promedio:", sum(iteraciones_rbt) / len(iteraciones_rbt))

    datos = list(zip(buscados, iteraciones_bst, iteraciones_spt, iteraciones_rbt))
    datos.sort()

    procesos_ordenados = [dato[0] for dato in datos]
    bst_ordenado = [dato[1] for dato in datos]
    spt_ordenado = [dato[2] for dato in datos]
    rbt_ordenado = [dato[3] for dato in datos]
    x = list(range(len(procesos_ordenados)))
    promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst)
    promedio_spt = sum(iteraciones_spt) / len(iteraciones_spt)
    promedio_rbt = sum(iteraciones_rbt) / len(iteraciones_rbt)

    plt.figure(figsize=(8, 5))
    plt.bar(
        ["BST", "Splay Tree", "Red-Black Tree"],
        [promedio_bst, promedio_spt, promedio_rbt],
        color=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.title("Promedio de iteraciones por arbol")
    plt.ylabel("Promedio de iteraciones")
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


run()
