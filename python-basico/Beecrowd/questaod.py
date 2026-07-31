N = int(input())

for i in range(N):
    M, C = map(int, input().split())
    chaves = list(map(int, input().split()))

    tabela = []

    for j in range(M):
        tabela.append([])

    for chave in chaves:
        posicao = chave % M
        tabela[posicao].append(chave)

    for j in range(M):
        print(f"{j} -> ", end="")

        for chave in tabela[j]:
            print(f"{chave} -> ", end="")

        print("\\")

    if i < N - 1:
        print()