## Desafio 15
# Fazer uma lista de frutas com maçã 3x e use um for para contar quantas
# vezes a palavra maçã repete

frutas = ["maçã", "banana", "maçã", "uva", "maçã", "pera"]
qtd = 0

for fruta in frutas:
    if fruta == "maçã":
        qtd += 1
        
print(f"A quantidade de maçãs é: {qtd}")