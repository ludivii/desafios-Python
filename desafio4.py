name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

print("Olá,", name, "! Você tem", age, "anos.")
print("Olá, {}! Você tem {} anos.".format(name,age))
print(f"Olá, {name}! Você tem {age} anos.")