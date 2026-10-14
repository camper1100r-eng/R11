edades = input().split()

edades = list(set(edades))
edades.sort(reverse=True)

print(edades)