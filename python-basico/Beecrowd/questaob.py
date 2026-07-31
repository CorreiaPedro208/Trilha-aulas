respostas = []

while True:
    try:
        N = int(input())
    except EOFError:
        break

    t = []

    for i in range(N):
        num = input()
        t.append(num)

    t.sort()
    r = 0

    for i in range(1, N):
        antes = t[i - 1]
        atual = t[i]
        pos = 0

        while (
            pos < len(antes)
            and pos < len(atual)
            and antes[pos] == atual[pos]
        ):
            pos += 1

        r += pos

    respostas.append(str(r))

print("\n".join(respostas))