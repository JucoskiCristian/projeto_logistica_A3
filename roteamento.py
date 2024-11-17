from classes import Caminhao

def roteamento(centros, entregas, caminhões, grafo):
    # Alocação de entregas para o centro mais próximo
    alocacao_entregas = {centro: [] for centro in centros}
    for entrega in entregas:
        destino, carga, prazo = entrega
        distancias, _ = grafo.dijkstra(destino)
        centro_mais_proximo = min(centros, key=lambda c: distancias[c])
        alocacao_entregas[centro_mais_proximo].append(entrega)

    # Roteamento por centro
    plano_entregas = {}
    for centro, entregas_alocadas in alocacao_entregas.items():
        caminhões_disponiveis = [Caminhao(c.id, c.capacidade, c.horas_diarias) for c in caminhões]
        distancias, _ = grafo.dijkstra(centro)
        entregas_alocadas.sort(key=lambda e: distancias[e[0]])  # Ordena por proximidade
        plano_entregas[centro] = []

        for entrega in entregas_alocadas:
            destino, carga, prazo = entrega
            tempo_viagem = distancias[destino]
            alocado = False
            for caminhao in caminhões_disponiveis:
                if caminhao.pode_alocar(carga, tempo_viagem):
                    caminhao.alocar(carga, destino, tempo_viagem)
                    alocado = True
                    break
            if not alocado:
                print(f"Erro: Não foi possível alocar a entrega para o destino {destino}")
        
        # Adiciona as rotas detalhadas ao plano
        plano_entregas[centro] = [
            (c.id, [(destino, carga, c.tempo_restante) for destino, carga in zip(c.rota, [ent[1] for ent in entregas_alocadas])])
            for c in caminhões_disponiveis
        ]
    return plano_entregas
