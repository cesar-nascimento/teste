# substitua pelo numero escolhido
numero = 34

def fib(n):
    # caso base
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)

nao_ultrapassou = True
n = 0
while nao_ultrapassou:
    temp = fib(n)
    if temp < numero:
        n += 1
        continue
    elif temp == numero:
        print("numero encontrado na sequencia")
        break
    elif temp > numero:
        print("numero NAO encontrado na sequencia")
        break