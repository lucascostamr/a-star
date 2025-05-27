from math import hypot
from pprint import pprint

from caminho import Caminho

fruta_coletada = False
caminhos_visitados = {}
lista_caminhos = []
menor_caminho = Caminho(0, None, [], 0)

def encontrar_coordenadas(
    identificador_personagem: str,
    identificador_chegada: str,
    identificador_fruta: str,
    tabuleiro: list[list[str]],
) -> tuple[int, int]:
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    coordenada_personagem = None
    coordenada_chegada = None
    coordenada_fruta = None

    for i in range(num_linhas):
        for j in range(num_coluas):
            if tabuleiro[i][j] == identificador_personagem:
                coordenada_personagem = (j, i)
            if tabuleiro[i][j] == identificador_chegada:
                coordenada_chegada = (j, i)
            if tabuleiro[i][j] == identificador_fruta:
                coordenada_fruta = (j, i)

    return (coordenada_personagem, coordenada_chegada, coordenada_fruta)


def cacular_funcao_heuristica(
    coordenadas_personagem, coordenadas_chegada, distancia_percorrida
):
    x_personagem, y_personagem = coordenadas_personagem
    x_chegada, y_chegada = coordenadas_chegada

    hipotenusa = hypot(abs(x_personagem - x_chegada), abs(y_personagem - y_chegada))

    return hipotenusa + distancia_percorrida


def movimento_valido(coordenadas, tabuleiro, fruta_coletada):
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    x, y = coordenadas

    if x < 0 or y < 0 or x >= num_linhas or y >= num_coluas:
        return False

    if coordenadas in caminhos_visitados:
        return False

    caminho_atual = tabuleiro[x][y]

    if caminho_atual == "F":
        fruta_coletada = True
        return True

    if caminho_atual == "B" and not fruta_coletada:
        return False
    return True


def retorna_menor_caminho(lista_caminhos) -> Caminho:
    if not lista_caminhos:
        return None

    menor_caminho = lista_caminhos.pop(0)
    menor_caminho_index = None
    for index, caminho in enumerate(lista_caminhos):
        if caminho.funcao_heuristica < menor_caminho.funcao_heuristica:
            menor_caminho = caminho
            menor_caminho_index = index

    if menor_caminho_index:
        lista_caminhos.pop(menor_caminho_index)
    return menor_caminho


tab: list[list[str]] = [
    ["C", "_", "_", "_", "B", "_"],
    ["_", "B", "_", "_", "_", "_"],
    ["_", "_", "F", "_", "_", "_"],
    ["_", "_", "_", "B", "B", "_"],
    ["_", "_", "_", "A", "_", "_"],
    ["_", "_", "_", "_", "_", "S"],
]

movimentos: dict[str, tuple[int, int]] = {
    "cima": (0, -1),
    "baixo": (0, 1),
    "esquerda": (-1, 0),
    "direita": (1, 0),
    "diagonal_inferior_direita": (1, 1),
    "diagonal_inferior_esquerda": (-1, 1),
    "diagonal_superior_direita": (1, -1),
    "diagonal_superior_esquerda": (-1, -1),
}

distancia_diagonal = {False: 1, True: 1.4}

coordenadas_personagem, coordenadas_chegada, coordenada_fruta = encontrar_coordenadas(
    identificador_personagem="C", identificador_chegada="S", identificador_fruta="F", tabuleiro=tab
)

while True:
    for key in movimentos.keys():
        movimento_x, movimento_y = movimentos[key]
        x_atual, y_atual = coordenadas_personagem

        nova_coordenada = (movimento_x + x_atual, movimento_y + y_atual)
        if movimento_valido(nova_coordenada, tab, fruta_coletada):
            distancia = key.startswith("diagonal")

            if tab[nova_coordenada[0]][nova_coordenada[1]] == "A":
                distancia_percorrida = (
                    distancia_diagonal[distancia] + menor_caminho.distancia_percorrida + 1
                )
            else:
                distancia_percorrida = (
                    distancia_diagonal[distancia] + menor_caminho.distancia_percorrida
                )

            funcao_heuristica = cacular_funcao_heuristica(
                coordenadas_chegada=coordenadas_chegada,
                coordenadas_personagem=nova_coordenada,
                distancia_percorrida=distancia_percorrida,
            )

            caminho_percorrido = [*menor_caminho.caminho_percorrido, nova_coordenada]

            novo_caminho = Caminho(
                funcao_heuristica,
                nova_coordenada,
                caminho_percorrido,
                distancia_percorrida,
            )
            lista_caminhos.append(novo_caminho)

            caminhos_visitados = set((*caminhos_visitados, nova_coordenada))

    pprint(lista_caminhos)
    menor_caminho: Caminho = retorna_menor_caminho(lista_caminhos)
    coordenadas_personagem = menor_caminho.coordenada

    if menor_caminho.coordenada == coordenadas_chegada or lista_caminhos is None:
        break

print(f"\n\nMenor Caminho: {menor_caminho}")
