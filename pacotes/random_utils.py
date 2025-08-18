import numpy as np

def exemplo_random(n=5):
    """Gera amostras aleatórias e calcula média e variância"""
    dados = np.random.normal(loc=10, scale=2, size=n)
    media = np.mean(dados)
    variancia = np.var(dados)

    return {
        "amostras": dados,
        "media": media,
        "variancia": variancia
    }
