# estatistica_simples/medidas_dispersao.py

import math

from .medidas_tendencia_central import media  # Importa a função media do módulo medidas_tendencia_central

def desvio_padrao(lista_de_numeros):
    """Calcula o desvio padrão de uma lista de números."""
    if not lista_de_numeros:
        return 0
    
    media_lista = media(lista_de_numeros)
    soma_dos_quadrados = sum([(x - media_lista) ** 2 for x in lista_de_numeros])
    variancia = soma_dos_quadrados / len(lista_de_numeros)
    return math.sqrt(variancia)

def variancia(lista_de_numeros):
    """Calcula a variância de uma lista de números."""
    if not lista_de_numeros:
        return 0

    media_lista = media(lista_de_numeros)
    soma_dos_quadrados = sum([(x - media_lista) ** 2 for x in lista_de_numeros])
    return soma_dos_quadrados / len(lista_de_numeros)