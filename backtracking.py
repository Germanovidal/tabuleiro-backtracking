def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | ' + ' | '.join(linha) + ' | ')

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float('inf')
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    # Movimento para DIREITA
    proxima_linha = linha_atual
    proxima_coluna = coluna_atual + 1

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna):
            return [proxima_linha, proxima_coluna, profundidade + 1]
        
        tabuleiro[proxima_linha][proxima_coluna] = '*'
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = ' '

        if resultado_movimento is not None and resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]

    # Movimento para CIMA 
    proxima_linha = linha_atual - 1
    proxima_coluna = coluna_atual

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna):
            return [proxima_linha, proxima_coluna, profundidade + 1]
        
        tabuleiro[proxima_linha][proxima_coluna] = '*'
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = ' '

        if resultado_movimento is not None and resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]
    
    
    # Movimento para ESQUERDA
    proxima_linha = linha_atual
    proxima_coluna = coluna_atual - 1
    
    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna):
            return [proxima_linha, proxima_coluna, profundidade + 1]
        
        tabuleiro[proxima_linha][proxima_coluna] = '*'
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = ' '

        if resultado_movimento is not None and resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]
    

    # Movimento para BAIXO
    proxima_linha = linha_atual + 1
    proxima_coluna = coluna_atual
    
    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna):
            return [proxima_linha, proxima_coluna, profundidade + 1]
        
        tabuleiro[proxima_linha][proxima_coluna] = '*'
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = ' '

        if resultado_movimento is not None and resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]
    
    return [melhor_linha, melhor_coluna, melhor_profundidade] if melhor_profundidade != float('inf') else None

def movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
    dentro_dos_limites = 0 <= proxima_linha < len(tabuleiro) and 0 <= proxima_coluna < len(tabuleiro[0])
    return dentro_dos_limites and tabuleiro[proxima_linha][proxima_coluna] == ' '

def chegou_destino(linha_atual, coluna_atual):
    return linha_atual == 0 and coluna_atual == 3

def main():
    tabuleiro = [
        ['X', ' ', ' ', ' '],
        [' ', ' ', 'X', 'X'],
        ['X', ' ', ' ', ' '],
        [' ', ' ', 'X', ' '],
    ]

    linha_atual = 3  
    coluna_atual = 0 

    tabuleiro[linha_atual][coluna_atual] = '*'
    mostrar_tabuleiro(tabuleiro)

    import sys

    while not chegou_destino(linha_atual, coluna_atual):
        melhor_movimento = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

        if melhor_movimento is None or melhor_movimento[2] == float('inf'):
            print('Não foi possível encontrar um caminho até o destino.')
            sys.exit()

        linha_atual, coluna_atual = melhor_movimento[0], melhor_movimento[1]
        tabuleiro[linha_atual][coluna_atual] = '*'
        input('Pressione ENTER para continuar...')
        mostrar_tabuleiro(tabuleiro)

    print('''
         -----------------------\n
          CHEGOU AO DESTINO!!\n
         -----------------------
    ''')

main()
