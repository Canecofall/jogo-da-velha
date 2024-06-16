# mostra o tabuleiro
def mostrar(jogo):
    for i in jogo:
        print(" | ".join(i))
        print("--" * 5)

#confere todas as linhas para ver se alguem ganhou
def checar(jogo, player):
    for u in jogo:
        if all([spot == player for spot in u]):#função all() testa todos os casos de teste
            return True
    for o in range(3):
        if all([jogo[u][o] == player for u in range(3)]):
            return True
    if all([jogo[i][i] == player for i in range(3)]) or all([jogo[i][2 - i] == player for i in range(3)]):
        return True
    return False

def jogo_da_velha():
    jogo = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    while True:
        mostrar(jogo)
        u = int(input(f"Jogador {jogador}, escolha uma linha (0-2): "))
        o = int(input(f"Jogador {jogador}, escolha uma coluna (0-2): "))
        if u > 2 or u < 0 or o > 2 or o < 0:
            print("Espaço imposivel, escolha outro.")
            continue
        if jogo[u][o] == " ":
            jogo[u][o] = jogador
        else:
            print("Espaço já ocupado, escolha outro.")
            continue
        if checar(jogo, jogador):
            mostrar(jogo)
            print(f"Jogador {jogador} venceu!")
            break
        if all(all(cell != " " for cell in row) for row in jogo):
            mostrar(jogo)
            print("Empate!")
            break
        jogador = "O" if jogador == "X" else "X"

jogo_da_velha()