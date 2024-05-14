# Crie um programa que tenha dois conjuntos de 5 números quaisquer e combine-os usando as operações de união, interseção e diferença, apresentando os resultados de cada operação.

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 2}

uniao = conjunto1.union(conjunto2)

intersecao = conjunto1.intersection(conjunto2)

diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

print("União dos conjuntos", uniao)
print("Interseção dos conjuntos", intersecao)
print("Diferença conjunto1 - conjunto2", diferenca1)
print("Diferença conjunto2 - conjunto1", diferenca2)