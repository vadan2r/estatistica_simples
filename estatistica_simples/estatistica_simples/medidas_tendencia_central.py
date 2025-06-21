# estatistica_simples/medidas_tendencia_central.py

def media(lista_de_numeros):
    """Calcula a média de uma lista de números."""
    if not lista_de_numeros:
        return 0  # Evita divisão por zero se a lista estiver vazia
    return sum(lista_de_numeros) / len(lista_de_numeros)

def mediana(lista_de_numeros):
    """Calcula a mediana de uma lista de números."""
    lista_ordenada = sorted(lista_de_numeros)
    tamanho = len(lista_ordenada)
    if tamanho % 2 == 0:  # Lista com número par de elementos
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        return (meio1 + meio2) / 2
    else:  # Lista com número ímpar de elementos
        return lista_ordenada[tamanho // 2]

def moda(lista_de_numeros):
    """Calcula a moda de uma lista de números."""
    # TODO: Implementar cálculo da moda (valor que mais se repete)
    # Esta é uma boa oportunidade para um exercício adicional.
    # Por enquanto, retorna None.
    frequencias = {}
    for numero in lista_de_numeros:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1

    moda = None
    maior_frequencia = 0
    for numero, frequencia in frequencias.items():
        if frequencia > maior_frequencia:
            moda = numero
            maior_frequencia = frequencia
        elif frequencia == maior_frequencia:
            # Se houver múltiplos valores com a mesma frequência máxima, retorna None
            moda = None

    return moda