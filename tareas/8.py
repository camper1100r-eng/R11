a, b, c = map(int, input().split())
n = int(input())
numeros = list(map(int, input().split()))

for i in range(n):
    if numeros[i] != a and numeros[i] != b and numeros[i] != c:
        print(numeros[i], end=" ")