import numpy as np

#calculando a velocidade média do veiculo

km = np.loadtxt('carros-km.txt')

#informa expressamente que o documento recebido pussui números.
anos = np.loadtxt('carros-anos.txt', dtype=int)

km_media = km / (2022 - anos)

print(km_media)

