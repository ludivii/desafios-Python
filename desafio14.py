## Desafio 14
# Fazer um loop de 1 a 10 com break no 5, depois um segundo loop de 1
# a 10 que ignore o 5

print("Loop com o break: ")
for i in range(1, 11):
    if i > 5:
        break
    print(i)

print("\nLoop com o continue: ")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)