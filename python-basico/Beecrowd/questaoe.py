N = int(input())

for i in range(N):
    M = int(input())
    frutas = {}

    for j in range(M):
        fruta, preco = input().split()
        frutas[fruta] = float(preco)

    P = int(input())
    valor = 0.0

    for j in range(P):
        fruta, qnt = input().split()
        valor += frutas[fruta] * int(qnt)

    print(f"R$ {valor:.2f}")
