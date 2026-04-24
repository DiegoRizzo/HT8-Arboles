import random
import matplotlib.pyplot as plt
import SpTree
import RBTree

def run():
    spt = SpTree.SpTree()
    rbt = RBTree.RBTree()
    procesos = []
    generador = random.Random(8)

    for _ in range(1000):
        procesos.append(generador.randint(1, 1000))

    for proceso in procesos:
        spt.insert(proceso)
        rbt.insert(proceso)

    target = 500
    pasos_spt_repetidos = []
    pasos_rbt_repetidos = []

    for _ in range(50):
        _, pasos = spt.search(target)
        pasos_spt_repetidos.append(pasos)

    for _ in range(50):
        _, pasos = rbt.find(target)
        pasos_rbt_repetidos.append(pasos)

    total_spt = sum(pasos_spt_repetidos)
    total_rbt = sum(pasos_rbt_repetidos)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 51), pasos_spt_repetidos, label='Splay Tree', marker='o', color='blue')
    plt.plot(range(1, 51), pasos_rbt_repetidos, label='Red-Black Tree', marker='s', color='red')
    plt.xlabel('Número de búsquedas')
    plt.ylabel('Pasos para encontrar el valor')
    plt.title(f'Contraste del número de iteraciones en 50 búsquedas repetidas del valor {target}')
    plt.legend()
    plt.grid(True)

    plt.text(0.02, 0.90,
             f'Iteraciones Splay Tree: {total_spt}\nIteraciones Red-Black Tree: {total_rbt}',
             transform=plt.gca().transAxes,
             fontsize=10,
             verticalalignment='top',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()

run()