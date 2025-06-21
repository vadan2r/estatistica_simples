# estatistica_simples/utilidades.py
# (Este módulo é opcional, mas pode ser útil para funções auxiliares)

def converter_para_numeros(lista_de_strings):
    """
    Converte uma lista de strings para uma lista de números (float).
    Levanta uma exceção ValueError se a conversão falhar.
    """
    try:
        return [float(x) for x in lista_de_strings]
    except ValueError:
        raise ValueError("A lista contém valores que não podem ser convertidos para números.")