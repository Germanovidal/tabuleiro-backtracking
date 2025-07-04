FUNÇÃO mostrar_tabuleiro(tabuleiro)
    PARA cada linha no tabuleiro:
        IMPRIMIR a linha formatada com os Pipes -> | 

FUNÇÃO proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade)
    Inicializa melhor_profundidade como infinito
    Define melhor_linha e melhor_coluna como a posição atual

    PARA cada direção em [direita, esquerda, cima, baixo]:
        Calcula nova_linha e nova_coluna com base na direção

        SE o movimento for válido:
            SE nova posição for o destino:
                RETORNA (nova_linha, nova_coluna, profundidade)

            Marca a nova posição no tabuleiro como visitada ('*')
            Chama recursivamente proximo_movimento com nova posição e profundidade + 1
            Desmarca a posição (restaura para espaço em branco)

            SE profundidade do resultado for melhor que a atual:
                Atualiza melhor_linha, melhor_coluna e melhor_profundidade

    RETORNA (melhor_linha, melhor_coluna, melhor_profundidade)

FUNÇÃO movimento_valido(tabuleiro, linha, coluna)
    RETORNA verdadeiro se linha e coluna estão dentro dos limites e a posição estiver livre

FUNÇÃO chegou_destino(linha, coluna)
    RETORNA verdadeiro se linha == 0 e coluna == 3

FUNÇÃO main()
    Define o tabuleiro com posições livres (' ') e bloqueadas ('X') -> Matriz criada
    Define posição inicial (linha 3, coluna 0) e marca com '*'

    Mostra o tabuleiro inicial

    ENQUANTO usuário continuar e não tiver chegado ao destino:
        Chama proximo_movimento com posição atual
        SE não for possível encontrar caminho (profundidade infinita):
            Mostra mensagem de erro e encerra

        Atualiza a posição atual com o melhor movimento encontrado
        Marca a nova posição no tabuleiro
        Mostra o tabuleiro atualizado

INÍCIO
    Executa main()