def encontrar_coordenadas_iniciais(identificador: str, tabuleiro: list[list[str]]) -> tuple[int, int]:
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    for i in range(num_linhas):
        for j in range(num_coluas):
            if tabuleiro[i][j] == identificador:
                return (i, j)

def movimento_valido(coordenadas, tabuleiro):
    num_linhas = len(tabuleiro)
    num_coluas = len(tabuleiro[0])

    x, y = coordenadas

    if x >= 0 and y >= 0 and x < num_linhas -1 and y < num_coluas -1:
        return True
    return False

tab: list[list[str]] = [
    ["C", "_", "_", "_", "B", "_"],
    ["_", "B", "_", "_", "_", "_"],
    ["_", "_", "F", "_", "_", "_"],
    ["_", "_", "_", "B", "B", "_"],
    ["_", "_", "_", "A", "_", "_"],
    ["_", "_", "_", "_", "_", "S"],
]

#Calcular a funcao heuristica ao redor

movimentos: dict[str, tuple[int, int]] = {
    "cima": (0, 1),
    "baixo": (0, -1),
    "esquerda": (-1, 0),
    "direita": (1, 0),
    "diagonal_inferior_direita": (1, -1),
    "diagonal_inferior_esquerda": (-1, -1),
    "diagonal_superior_direita": (1, 1),
    "diagonal_superior_esquerda": (-1, 1)
}

coordenadas_personagem: tuple[int, int] = encontrar_coordenadas_iniciais(identificador="C", tabuleiro=tab)

lista_caminhos = []

class Caminho:
    def __init__(self, funcao_heuristica, coordenada):
        self.funcao_heuristica = funcao_heuristica
        self.coordenada = coordenada

    def __repr__(self):
        return f"Caminho (funcao_heuristica={self.funcao_heuristica}, coordenada={self.coordenada})"

for key in movimentos.keys():
    movimento_x, movimento_y = movimentos[key]
    x_atual, y_atual = coordenadas_personagem

    nova_coordenada = (movimento_x + x_atual, movimento_y + y_atual)
    if movimento_valido(nova_coordenada, tab):
        novo_caminho = Caminho(0, nova_coordenada)
        lista_caminhos.append(novo_caminho)

print(lista_caminhos)
