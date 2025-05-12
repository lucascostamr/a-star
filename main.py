import copy
from math import hypot


class Node:
    indice: int = 0
    distancia_percorrida: float = 0
    funcao_heuristica: float = 0
    caminho: list[tuple] = []


def funcao_heuristica(
    distancia_percorrida: float, distancia_linha_reta: float
) -> float:
    return distancia_linha_reta + distancia_percorrida


def diagonal(coord_anterior: tuple, coord_atual: tuple) -> bool:
    x_1, x_2 = coord_anterior
    y_1, y_2 = coord_atual
    return abs(x_1 - x_2) == abs(y_1 - y_2)


def hipotenusa(coord_a: tuple, coord_b: tuple) -> float:
    x1, y1 = coord_a
    x2, y2 = coord_b

    return round(hypot(x2 - x1, y2 - y1), 2)


def get_min(lista_filhos: list[Node]):
    if len(lista_filhos) == 0:
        return None

    melhor_filho: Node = lista_filhos[0]
    indice_menor = 0
    for index, filho in enumerate(lista_filhos[1:], start=1):
        if filho.funcao_heuristica < melhor_filho.funcao_heuristica:
            melhor_filho = filho
            indice_menor = index
    del lista_filhos[indice_menor]
    return melhor_filho


tab = [
    ["C", "_", "_", "_", "B", "_"],
    ["_", "B", "_", "_", "_", "_"],
    ["_", "_", "F", "_", "_", "_"],
    ["_", "_", "_", "B", "B", "_"],
    ["_", "_", "_", "A", "_", "_"],
    ["_", "_", "_", "_", "_", "S"],
]

pai = Node()
pai.indice = 0
pai.distancia_percorrida = 0
lista_filhos = []
final = Node()

personagem = "C"
chegada = "S"

coord_chegada = (5, 5)
coordenada_anterior = None

while True:
    for x in range(len(tab[0])):
        filho = Node()
        filho.indice = x
        if coordenada_anterior and diagonal(coordenada_anterior, (x, pai.indice)):
            filho.distancia_percorrida = pai.distancia_percorrida + 1.4
        else:
            coordenada_anterior = (x, pai.indice)
            filho.distancia_percorrida = pai.distancia_percorrida + 1

        resultado_hipotenusa = hipotenusa((x, pai.indice), coord_chegada)

        filho.funcao_heuristica = funcao_heuristica(
            filho.distancia_percorrida, resultado_hipotenusa
        )
        filho.caminho = copy.deepcopy(pai.caminho)
        filho.caminho.append((x, pai.indice))
        lista_filhos.append(filho)
        print(
            "adicionou:",
            filho.indice,
            " funcao heuristica:",
            filho.funcao_heuristica,
            " do pai: ",
            pai.indice,
        )
        print(tab[x][pai.indice])

    # depois do loop na matriz
    pai = get_min(lista_filhos)
    if pai is None:
        print("Melhor final selecionado:", final.indice)
        print("distancia", final.distancia_percorrida)
        print("caminho", final.caminho)
        break
    print("Melhor filho selecionado:", pai.indice, " fe:", pai.funcao_heuristica)
    print("caminho", pai.distancia_percorrida)
    if pai.indice == len(tab) - 1 and (
        final.funcao_heuristica == -1 or pai.funcao_heuristica < final.funcao_heuristica
    ):  # CONDIÇÂO DE PARADA DEVE SER LISTA VAZIA!
        final = pai
