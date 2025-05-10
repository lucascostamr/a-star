import copy

class Node:
    indice: int = 0
    distancia_percorrida: float = 0
    funcao_heuristica: float = 0
    caminho: list[tuple] = []


def funcao_heuristica(distancia_percorrida: float, distancia_linha_reta: float) -> float:
    return distancia_linha_reta + distancia_percorrida

def get_min(lista_filhos: list[Node]):

    if len(lista_filhos) == 0:
        return None

    melhor_filho: Node = lista_filhos[0]
    indice_menor = 0
    for filho, index in lista_filhos[1:]:
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

while True:
    for j in range(len(tab[0])):
        if tab[pai.indice][j] != 0:
            filho = Node()
            filho.indice = j
            filho.distancia_percorrida = pai.distancia_percorrida + tab[pai.indice][j]
            filho.fe = funcao_heuristica(
                dist, pai.distancia_percorrida, tab[pai.indice][j], j
            )
            filho.caminho = copy.deepcopy(pai.caminho)
            filho.caminho.append(pai.indice)
            estados.append(filho)
            print("adicionou:", filho.indice, " fe:", filho.fe, " do pai: ", pai.indice)

    # depois do loop na matriz
    pai = get_min(estados)
    if pai == None:
        print("Melhor final selecionado:", final.indice)
        print("distancia", final.distancia_percorrida)
        print("caminho", final.caminho)
        break
    print("Melhor filho selecionado:", pai.indice, " fe:", pai.fe)
    print("caminho", pai.distancia_percorrida)
    if pai.indice == len(tab) - 1 and (
        final.fe == -1 or pai.fe < final.fe
    ):  # CONDIÇÂO DE PARADA DEVE SER LISTA VAZIA!
        final = pai
