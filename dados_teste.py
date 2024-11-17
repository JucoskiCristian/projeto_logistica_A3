from classes import Grafo, Caminhao
import random

def criar_dados_teste():
    # Centros de distribuição
    centros = ['Belém', 'Recife', 'São Paulo', 'Curitiba']

    # Destinos (definidos manualmente)
    destinos = [f"Destino{i}" for i in range(1, 21)]  # 20 destinos possíveis

    # Gerar 100 entregas aleatórias (destino, carga, prazo)
    entregas = [
        (random.choice(destinos), random.randint(1, 10), random.randint(1, 5))
        for _ in range(100)
    ]

    caminhões = [
        Caminhao(1, 15, 10),
        Caminhao(2, 20, 10),
        Caminhao(3, 15, 10),
        Caminhao(4, 20, 10),
        Caminhao(5, 15, 10),
        Caminhao(6, 20, 10),
        Caminhao(7, 15, 10),
        Caminhao(8, 20, 10),
        Caminhao(9, 15, 10),
        Caminhao(10, 20, 10),
        
    ]

    # Grafo de distâncias
    grafo = Grafo()
    # Conectando centros de distribuição a destinos com distâncias aleatórias
    for centro in centros:
        for destino in destinos:
            distancia = random.randint(2, 15)
            grafo.adicionar_aresta(centro, destino, distancia)

    # Adicionar algumas conexões entre destinos para mais rotas
    for _ in range(50):  # 50 conexões extras entre destinos
        origem = random.choice(destinos)
        destino = random.choice(destinos)
        if origem != destino:
            distancia = random.randint(1, 10)
            grafo.adicionar_aresta(origem, destino, distancia)

    return centros, entregas, caminhões, grafo
