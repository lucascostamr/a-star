import tkinter as tk
import time
from main import menor_caminho, tab as cenario  # ta importando o back trazendo  o objeto final

TAMANHO = 60
VELOCIDADE = 5

unicodes = {
    '_': '',
    'B': '🧱',
    'F': '🧃',
    'A': '🌀',
    'S': '🎌',
    'C': '',  # como o carrinho  move nao tem icone entao nao e fixo
}

cores = {
    '_': "white",
    'B': "white",
    'F': "white",
    'A': "white",
    'S': "white",
    'C': "white",
}

class TabuleiroApp:
    def __init__(self, matriz, caminho):
        self.matriz = matriz
        self.caminho = caminho
        self.linhas = len(matriz)
        self.colunas = len(matriz[0])

        self.root = tk.Tk()
        self.root.title("A* - Caminho Visual")

        # frame principal com canvas e legenda lado a lado
        frame_principal = tk.Frame(self.root)
        frame_principal.pack()

        self.canvas = tk.Canvas(frame_principal, width=self.colunas*TAMANHO, height=self.linhas*TAMANHO)
        self.canvas.pack(side=tk.LEFT)

        self.cells = {}
        self.desenha_tabuleiro()

        # carrinho aqui ta na posição  inicial
        linha_ini, col_ini = self.caminho[0][1], self.caminho[0][0]
        self.personagem = self.canvas.create_text(
            col_ini * TAMANHO + TAMANHO // 2,
            linha_ini * TAMANHO + TAMANHO // 2,
            text='🚗',
            font=("Arial", 28)
        )

        # legenda do lado
        self.criar_legenda(frame_principal)

        # começa movimentação
        self.root.after(1000, self.mover_animado)
        self.root.mainloop()

    def desenha_tabuleiro(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                x1, y1 = j * TAMANHO, i * TAMANHO
                x2, y2 = x1 + TAMANHO, y1 + TAMANHO
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cores[self.matriz[i][j]], outline="gray")
                texto = self.canvas.create_text(x1 + TAMANHO//2, y1 + TAMANHO//2, text=unicodes.get(self.matriz[i][j], ''), font=("Arial", 24))
                self.cells[(i, j)] = (rect, texto)

    def criar_legenda(self, frame):
        legenda = tk.Frame(frame)
        legenda.pack(side=tk.RIGHT, padx=10)

        itens = [
            ('🚗', "Carrinho (início)"),
            ('🧱', "Barreira"),
            ('🧃', "Gasolina: permite passar barreira"),
            ('🌀', "Especial (sem efeito)"),
            ('🎌', "Chegada"),
            ('🔵', "Caminho percorrido"),
        ]

        for icon, desc in itens:
            linha = tk.Frame(legenda)
            linha.pack(anchor="w")
            tk.Label(linha, text=icon, font=("Arial", 16)).pack(side=tk.LEFT)
            tk.Label(linha, text=" - " + desc, font=("Arial", 12)).pack(side=tk.LEFT)

    def mover_animado(self):
        for idx in range(len(self.caminho) - 1):
            x1, y1 = self.caminho[idx]
            x2, y2 = self.caminho[idx + 1]

            linha1, col1 = y1, x1
            linha2, col2 = y2, x2

            px1 = col1 * TAMANHO + TAMANHO // 2
            py1 = linha1 * TAMANHO + TAMANHO // 2
            px2 = col2 * TAMANHO + TAMANHO // 2
            py2 = linha2 * TAMANHO + TAMANHO // 2

            dx = (px2 - px1) / VELOCIDADE
            dy = (py2 - py1) / VELOCIDADE

            for _ in range(VELOCIDADE):
                self.canvas.move(self.personagem, dx, dy)
                self.root.update()
                time.sleep(0.05)

            rastro = self.canvas.create_text(
                px1, py1, text="🔵", font=("Arial", 14)
            )
            self.canvas.tag_lower(rastro)  

if __name__ == "__main__":
    if menor_caminho:
        TabuleiroApp(cenario, menor_caminho.caminho_percorrido)
    else:
        print("Caminho não encontrado.")
