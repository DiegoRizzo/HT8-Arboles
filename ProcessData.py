import random


def get_processes():
    generador = random.Random(8)
    procesos = []

    for _ in range(1000):
        procesos.append(generador.randint(1, 10000))

    return procesos


def get_inserted_processes():
    procesos = get_processes()
    insertados = []
    vistos = set()

    for proceso in procesos:
        if proceso not in vistos:
            vistos.add(proceso)
            insertados.append(proceso)

    return insertados


def get_searches():
    generador = random.Random(25)
    return generador.sample(get_inserted_processes(), 100)
