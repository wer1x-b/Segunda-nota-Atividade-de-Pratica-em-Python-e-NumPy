import numpy as np

def exemplo_linalg():
    """Exemplo de uso de funções de álgebra linear do NumPy."""
    # Criando uma matriz 2x2
    A = np.array([[1, 2], [3, 4]])
    
    # Calculando o determinante da matriz
    det_A = np.linalg.det(A)
    
    # Calculando a inversa da matriz
    inv_A = np.linalg.inv(A)
    
    # Resolvendo um sistema de equações lineares Ax = b
    b = np.array([5, 11])
    x = np.linalg.solve(A, b)
    
    return det_A, inv_A, x