# estatistica_simples/__init__.py

# Importa as funções que você quer que sejam diretamente acessíveis
# quando o pacote for importado.
from .medidas_tendencia_central import media, mediana, moda
from .medidas_dispersao import desvio_padrao, variancia

# Opcional: Definir a versão do pacote
__version__ = "0.1.0"