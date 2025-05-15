from math import hypot


def encontrar_coordenadas(
    identificador_personagem: str,
    identificador_chegada: str,
    tabuleiro: list[list[str]],
) -> tuple[int, int]:
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    coordenada_personagem = None
    coordenada_chegada = None

    for i in range(num_linhas):
        for j in range(num_coluas):
            if tabuleiro[i][j] == identificador_personagem:
                coordenada_personagem = (i, j)
            if tabuleiro[i][j] == identificador_chegada:
                coordenada_chegada = (i, j)

    return (coordenada_personagem, coordenada_chegada)


def cacular_funcao_heuristica(
    coordenas_personagem, coordenadas_chegada, distancia_percorrida
):
    x_personagem, y_personagem = coordenadas_personagem
    x_chegada, y_chegada = coordenadas_chegada

    hipotenusa = hypot(abs(x_personagem - x_chegada), abs(y_personagem - y_chegada))

    return hipotenusa + distancia_percorrida


def movimento_valido(coordenadas, tabuleiro):
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    x, y = coordenadas

    if x >= 0 and y >= 0 and x < num_linhas - 1 and y < num_coluas - 1:
        return True
    return False

def retorna_menor_caminho(lista_caminhos):
    if not lista_caminhos:
        return None

    menor_caminho = lista_caminhos[0]
    for caminho in lista_caminhos[1:]:
        if caminho.funcao_heuristica < menor_caminho.funcao_heuristica:
            menor_caminho = caminho

    lista_caminhos.remove(menor_caminho)
    return menor_caminho


tab: list[list[str]] = [
    ["C", "_", "_", "_", "B", "_"],
    ["_", "B", "_", "_", "_", "_"],
    ["_", "_", "F", "_", "_", "_"],
    ["_", "_", "_", "B", "B", "_"],
    ["_", "_", "_", "A", "_", "_"],
    ["_", "_", "_", "_", "_", "S"],
]

# Calcular a funcao heuristica ao redor

movimentos: dict[str, tuple[int, int]] = {
    "cima": (0, 1),
    "baixo": (0, -1),
    "esquerda": (-1, 0),
    "direita": (1, 0),
    "diagonal_inferior_direita": (1, -1),
    "diagonal_inferior_esquerda": (-1, -1),
    "diagonal_superior_direita": (1, 1),
    "diagonal_superior_esquerda": (-1, 1),
}

distancia_diagonal = {False: 1, True: 1.4}

coordenadas_personagem, coordenadas_chegada = encontrar_coordenadas(
    identificador_personagem="C", identificador_chegada="S", tabuleiro=tab
)

lista_caminhos = []


class Caminho:
    def __init__(self, funcao_heuristica, coordenada, distancia_percorrida):
        self.coordenadas_percorridas = []
        self.funcao_heuristica = funcao_heuristica
        self.distancia_percorrida = distancia_percorrida

        self.coordenadas_percorridas.append(coordenada)

    def __repr__(self):
        return f"Caminho (funcao_heuristica={self.funcao_heuristica}, coordenadas={self.coordenadas_percorridas}, distancia_percorrida={self.distancia_percorrida})"


menor_caminho = Caminho(0, None, 0)

for key in movimentos.keys():
    movimento_x, movimento_y = movimentos[key]
    x_atual, y_atual = coordenadas_personagem

    nova_coordenada = (movimento_x + x_atual, movimento_y + y_atual)
    if movimento_valido(nova_coordenada, tab):
        distancia = key in [
            "diagonal_inferior_direita",
            "diagonal_inferior_esquerda",
            "diagonal_superior_direita",
            "diagonal_superior_esquerda",
        ]

        distancia_percorrida = (
            distancia_diagonal[distancia] + menor_caminho.distancia_percorrida
        )

        funcao_heuristica = cacular_funcao_heuristica(
            coordenadas_chegada=coordenadas_chegada,
            coordenas_personagem=coordenadas_personagem,
            distancia_percorrida=distancia_percorrida,
        )
        novo_caminho = Caminho(
            funcao_heuristica,
            nova_coordenada,
            distancia_percorrida
        )
        lista_caminhos.append(novo_caminho)

menor_caminho = retorna_menor_caminho(lista_caminhos)

print(lista_caminhos)
print(menor_caminho)
