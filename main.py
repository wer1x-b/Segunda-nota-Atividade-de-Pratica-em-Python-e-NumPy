from pacotes import soma_lista, contar_pares, exemplo_linalg, exemplo_random

# Estruturas básicas
numeros = [1, 2, 3, 4, 5, 6]
print("Soma:", soma_lista(numeros))
print("Pares:", contar_pares(numeros))

# NumPy.linalg
resultado_linalg = exemplo_linalg()
print("\nExemplo numpy.linalg:")
for k, v in resultado_linalg.items():
    print(f"{k}:\n{v}")

# NumPy.random
resultado_random = exemplo_random(10)
print("\nExemplo numpy.random:")
for k, v in resultado_random.items():
    print(f"{k}:\n{v}")
