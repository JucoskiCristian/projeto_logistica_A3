from classes import Grafo, Caminhao

def criar_dados_teste():
    # Centros de distribuição
    centros = ['Belém', 'Recife', 'São Paulo', 'Curitiba']

    # Entregas (destino, carga, prazo)
    entregas = [
        ('Destino1', 5, 2), 
        ('Destino2', 8, 3),
        ('Destino3', 3, 1),
        ('Destino4', 7, 4),
        ('Destino5', 2, 2)
    ]

    # Caminhões
    caminhões = [
        Caminhao(1, 10, 8),
        Caminhao(2, 15, 8)
    ]

    # Grafo de distâncias
    grafo = Grafo()
    grafo.adicionar_aresta('Belém', 'Destino1', 4)
    grafo.adicionar_aresta('Belém', 'Destino2', 8)
    grafo.adicionar_aresta('Recife', 'Destino3', 6)
    grafo.adicionar_aresta('Recife', 'Destino4', 3)
    grafo.adicionar_aresta('São Paulo', 'Destino5', 2)
    grafo.adicionar_aresta('Curitiba', 'Destino5', 5)

    return centros, entregas, caminhões, grafo
