from dados_teste import criar_dados_teste
from roteamento import roteamento

def exibir_plano(plano):
    print("\n==== PLANO DE ENTREGA ====")
    for centro, rotas in plano.items():
        print(f"\nCentro de Distribuição: {centro}")
        if not rotas:
            print("  Nenhuma entrega alocada.")
        for id_caminhao, rota in rotas:
            if rota:
                print(f"  Caminhão {id_caminhao}:")
                for entrega in rota:
                    destino, carga, tempo_restante = entrega
                    print(f"    - Destino: {destino}")
                    print(f"      Carga transportada: {carga}")
                    print(f"      Tempo restante do caminhão: {tempo_restante:.1f} horas")
            else:
                print(f"  Caminhão {id_caminhao}: Nenhuma entrega atribuída.")
    print("\n==== FIM DO PLANO ====")

def main():
    # Carrega dados de teste
    centros, entregas, caminhões, grafo = criar_dados_teste()

    # Executa o roteamento
    plano = roteamento(centros, entregas, caminhões, grafo)

    # Exibe o plano de entregas
    exibir_plano(plano)

if __name__ == "__main__":
    main()
