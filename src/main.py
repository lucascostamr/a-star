from a_star import AStar
from view import TabuleiroApp

def main():
    tab: list[list[str]] = [
        ["C", "_", "_", "_", "B", "_"],
        ["_", "B", "_", "_", "_", "_"],
        ["_", "_", "F", "_", "_", "_"],
        ["_", "_", "_", "B", "B", "_"],
        ["_", "_", "_", "A", "_", "_"],
        ["_", "_", "_", "_", "_", "S"],
    ]

    a_star_alogrithm = AStar(debug=False)
    menor_caminho = a_star_alogrithm.start(tab)
    caminhos_visitados = a_star_alogrithm.retornar_caminhos_visitados()

    if not menor_caminho:
        print("Nenhum caminho encontrado")
        return

    print(f"\nMenor Caminho: {menor_caminho}")

    TabuleiroApp(tab, caminhos_visitados, menor_caminho.caminho_percorrido)

if __name__ == "__main__":
    main()