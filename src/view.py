import tkinter as tk
import time


TAMANHO = 60
VELOCIDADE = 5

unicodes = {
    '_': '',
    'B': '█',
    'F': '⛽',
    'A': '…',
    'S': '🏁',
    'C': '',
}

cores = {
    '_': "white",
    'B': "white",
    'F': "white",
    'A': "white",
    'S': "white",
    'C': "white",
}

FINAL_COR = "#4caf50"

class TabuleiroApp:
    def __init__(self, matriz, caminhos_visitados, menor_caminho):
        self.matriz = matriz
        self.menor_caminho = menor_caminho
        self.caminhos_visitados = caminhos_visitados
        self.linhas = len(matriz)
        self.colunas = len(matriz[0])

        self.root = tk.Tk()
        self.root.title("A* - Caminho Visual")

        frame_principal = tk.Frame(self.root)
        frame_principal.pack()

        self.canvas = tk.Canvas(frame_principal, width=self.colunas*TAMANHO, height=self.linhas*TAMANHO)
        self.canvas.pack(side=tk.LEFT)

        self.cells = {}
        self.desenha_tabuleiro()

        linha_ini, col_ini = self.menor_caminho[0][1], self.menor_caminho[0][0]
        self.personagem = self.canvas.create_text(
            col_ini * TAMANHO + TAMANHO // 2,
            linha_ini * TAMANHO + TAMANHO // 2,
            text='🚗',
            font=("Arial", 28)
        )

        self.criar_legenda(frame_principal)

        self.root.after(1000, self.animar_caminho_final)
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

        items = [
            ('🚗', "Carrinho (início)"),
            ('█', "Barreira"),
            ('⛽', "Gasolina: permite passar barreira"),
            ('…', "Especial (sem efeito)"),
            ('🏁', "Chegada"),
            ('🟢', "Caminho final"),
        ]

        for icon, desc in items:
            linha = tk.Frame(legenda)
            linha.pack(anchor="w")
            tk.Label(linha, text=icon, font=("Arial", 16)).pack(side=tk.LEFT)
            tk.Label(linha, text=" - " + desc, font=("Arial", 12)).pack(side=tk.LEFT)

    def animar_caminho_final(self):
        for idx in range(len(self.caminhos_visitados)):
            x, y = self.caminhos_visitados[idx]
            rect, _ = self.cells[(y, x)]
            self.canvas.itemconfig(rect, fill='gray')
            self.root.update()
            time.sleep(0.15)
            px, py = x * TAMANHO + TAMANHO // 2, y * TAMANHO + TAMANHO // 2
            rastro = self.canvas.create_text(px, py, text="🟢", font=("Arial", 14))
            self.canvas.tag_lower(rastro)

        for idx in range(len(self.menor_caminho)):
            x, y = self.menor_caminho[idx]
            rect, _ = self.cells[(y, x)]
            self.canvas.itemconfig(rect, fill=FINAL_COR)
            # move o carrinho
            if idx > 0:
                x1, y1 = self.menor_caminho[idx-1]
                linha1, col1 = y1, x1
                linha2, col2 = y, x
                px1 = col1 * TAMANHO + TAMANHO // 2
                py1 = linha1 * TAMANHO + TAMANHO // 2
                px2 = col2 * TAMANHO + TAMANHO // 2
                py2 = linha2 * TAMANHO + TAMANHO // 2
                dx = (px2 - px1) / VELOCIDADE
                dy = (py2 - py1) / VELOCIDADE
                for _ in range(VELOCIDADE):
                    self.canvas.move(self.personagem, dx, dy)
                    self.root.update()
                    time.sleep(0.08)
            self.root.update()
            time.sleep(0.15)
            px, py = x * TAMANHO + TAMANHO // 2, y * TAMANHO + TAMANHO // 2
            rastro = self.canvas.create_text(px, py, text="🟢", font=("Arial", 14))
            self.canvas.tag_lower(rastro)