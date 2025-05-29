class Caminho:
    def __init__(
        self, caminho_percorrido, funcao_heuristica = 0, coordenada = None, distancia_percorrida = 0, fruta_coletada=False
    ):
        self.caminho_percorrido = caminho_percorrido
        self.coordenada = coordenada
        self.funcao_heuristica = funcao_heuristica
        self.distancia_percorrida = distancia_percorrida
        self.fruta_coletada = fruta_coletada

    def __repr__(self):
        return f"Caminho (funcao_heuristica={self.funcao_heuristica}, caminho={self.caminho_percorrido}, distancia_percorrida={self.distancia_percorrida}, fruta_coletada={self.fruta_coletada})"