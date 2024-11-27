## Desafio 4
# Crie uma var name e age usando input e mostre os prints

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

print("Olá,", name, "! Você tem", age, "anos.")
print("Olá, {}! Você tem {} anos.".format(name,age))
print(f"Olá, {name}! Você tem {age} anos.")