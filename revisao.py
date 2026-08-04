# nomes = []
# for i in range(5):
#     nome = input("Digite seu nome:")
# nomes.append(nome)
# for i in range(5):
#     print(nomes[i])


# ==================== EXERCÍCIO 2 ====================

# #Criando a lista
# frutas = ["maçã", "banana", "uva", "laranja"]

# print("Lista inicial:", frutas)

# # Removendo "uva"
# frutas.remove("uva")
# print("Após remover 'uva':", frutas)

# # Adicionando "morango"
# frutas.append("morango")
# print("Após adicionar 'morango':", frutas)

# # Lista final
# print("\n✅ Lista atualizada:", frutas)
# #  Metodo pop()
# # Removendo o último elemento (padrão)
# ultima = frutas.pop()
# print("\nRemovido com pop() (terceiro):", ultima)
# print("Lista após pop():", frutas)

# # Removendo por índice específico
# segunda = frutas.pop(1)        # remove "banana"
# print("\nRemovido com pop(1):", segunda)
# print("Lista após pop(1):", frutas)

#================== Atividade 3 ======================
# numeros = []
# soma = 0

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
    
# for numero in numeros:
#     soma = soma + numero
# print(soma)
    
# ===================== Atividade 5 =================
# notas = []
# soma = 0

# for i in range[4]:
#     nota = float(input("Digite sua nota: "))
#     notas.append(nota)

# for nota in notas:
#     soma = soma + nota
#     media = soma / len(notas)

# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")    
 

print("=== EXPLORANDO pop() e del ===\n")

frutas = ["maçã", "banana", "uva", "laranja", "morango", "abacaxi"]
print("Lista inicial:", frutas)

# Usando pop()
item1 = frutas.pop()           # último
item2 = frutas.pop(2)          # índice 2

print(f"\nItem removido com pop(): {item1}")
print(f"Item removido com pop(2): {item2}")
print("Lista após pop():", frutas)

# Usando del
del frutas[0]                  # remove primeiro item
print("\nApós del frutas[0]:", frutas)

# del com slice
del frutas[-2:]                # remove os 2 últimos
print("Após del frutas[-2:]:", frutas)

print("testeando")