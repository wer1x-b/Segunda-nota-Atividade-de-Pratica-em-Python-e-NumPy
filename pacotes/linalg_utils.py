import numpy as np

def exemplo_linalg():
    """Exemplo de uso de funções de álgebra linear do NumPy."""
    # Criando uma matriz 2x2
    a = np.array([[1, 2], [3, 4]])
    
    # Calculando a inversa da matriz
    b = np.linalg.inv(a)
    
    # Calculando o determinante da matriz
    c = np.linalg.det(a)
    
    return {
        "matriz original": a,
        "inversa": b,
        "determinante": c
    }