tabuleiro = [' '] * 9

def exibir_tabuleiro():
    print('------------')
    for i in range(3):
        print(f'| {tabuleiro[i*3]} | {tabuleiro[i*3 + 1]} | {tabuleiro[i*3 + 2]} |')
        print('------------')

def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacao in combinacoes_vencedoras:
        if all(tabuleiro[i] == jogador for i in combinacao):
            return True
    return False

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, 'X'):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, 'O'):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0
    
    if maximizando:
        melhor_valor = -float('inf')
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'O'
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ' '
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float('inf')
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'X'
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ' '
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor
    
def melhor_jogada(tabuleiro):
    melhor_valor = -float('inf')
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ' '
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
    return melhor_posicao

def jogar_jogo():
    while True:
        exibir_tabuleiro()
        
        jogada_valida = False
        while not jogada_valida:
            try:
                jogada = int(input('Escolha uma posição entre 0 e 8: '))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == ' ':
                    tabuleiro[jogada] = 'X'
                    jogada_valida = True
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número entre 0 e 8.")
        
        if verificar_vencedor(tabuleiro, 'X'):
            exibir_tabuleiro()
            print('Você venceu!')
            break
            
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print('Empate!')
            break

        print('Computador está pensando...')
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = 'O'

        if verificar_vencedor(tabuleiro, 'O'):
            exibir_tabuleiro()
            print('O Computador venceu!')
            break
            
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print('Empate!')
            break

print('BEM-VINDO AO JOGO DA VELHA!')
jogar_jogo()