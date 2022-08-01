import numpy as np

anos = np.loadtxt("carros-anos.txt", dtype=int)
km = np.loadtxt("carros-km.txt")
valor = np.loadtxt("carros-valor.txt")

dataset = np.column_stack((anos, km, valor))

print(dataset.shape)

#Retorna a média, porém a média de todo o dataset, o que não faz sentido
print(np.mean(dataset))

#Para solucionar isso usamos o axis, aqui teremos como retorno a média de cada uma das colunas, porém, a média de anos não faz sentido...
#Axis: 0 coluna; 1 linhas

print(np.mean(dataset, axis=0))

#Apenas o que fazem sentido, KM

print(f'Média de km: {np.mean(dataset[:, 1])}')

#Apenas valor

print(f'Média de valor: {np.mean(dataset[:, 2])}')

#Calculando o desvio padrão:

print(f'O desvio padrão do valor é : {np.std(dataset[:,2])}')

#Somatório:

print(f'O somatório do Dataset é: {np.sum(dataset, axis=0)}')

#Novamente ter o somatório dos anos não faz sentido, então:

print(f'O somatório do km é: {np.sum(dataset[:, 1])}')

print(f'O somatório do valor é: {np.sum(dataset[:, 2])}')