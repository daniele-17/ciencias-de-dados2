import numpy as np
from scipy import stats

# Nota de matemática
notas = [78, 85, 91, 73, 88, 92, 79, 85, 90, 87]

# Calcular a média
media = np.mean(notas)
print(f'Média: {media}')

# Calcular a mediana
mediana = np.median(notas)
print(f'Mediana: {mediana}')

# Calcular a moda
moda = stats.mode(notas, keepdims=True)
print(f'Moda: {moda.mode[0]}, Frequência: {moda.count[0]}')