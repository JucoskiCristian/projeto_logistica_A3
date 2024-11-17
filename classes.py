import heapq

# Classe Caminhao
class Caminhao:
    def __init__(self, id, capacidade, horas_diarias):
        self.id = id
        self.capacidade = capacidade
        self.horas_diarias = horas_diarias
        self.carga_atual = 0
        self.tempo_restante = horas_diarias
        self.rota = []

    def pode_alocar(self, carga, tempo_viagem):
        return (self.carga_atual + carga <= self.capacidade and 
                self.tempo_restante >= tempo_viagem)

    def alocar(self, carga, destino, tempo_viagem):
        self.carga_atual += carga
        self.tempo_restante -= tempo_viagem
        self.rota.append(destino)

# Classe Grafo
class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, origem, destino, distancia):
        if origem not in self.adjacencias:
            self.adjacencias[origem] = []
        self.adjacencias[origem].append((destino, distancia))
        if destino not in self.adjacencias:
            self.adjacencias[destino] = []
        self.adjacencias[destino].append((origem, distancia))

    def dijkstra(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.adjacencias}
        distancias[inicio] = 0
        prioridade = [(0, inicio)]
        caminho = {}

        while prioridade:
            distancia_atual, nodo_atual = heapq.heappop(prioridade)
            if distancia_atual > distancias[nodo_atual]:
                continue
            for vizinho, peso in self.adjacencias.get(nodo_atual, []):
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminho[vizinho] = nodo_atual
                    heapq.heappush(prioridade, (distancia, vizinho))
        return distancias, caminho
