n = int(input("informe n: "))
while n <= 0:
    n = int(input("Valor invalido, digite novamente: "))

if n == 1 or n == 2:
    print("fibonacci vale 1")
else:
    ant = 1
    atual = 1
    prox = ant + atual
    posicao = 3
    
    while posicao < n:
        ant = atual
        atual = prox
        prox = ant + atual
        posicao = posicao + 1
    print(f"fibonacci vale {prox}")