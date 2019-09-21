"""
Exercicio 02-12: Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

destino = float(input('Qual a distância até o seu destino: '))
velo = float(input('Qual a velocidade media em que você pretende ir: '))
resultado = destino / velo
print(f'A velocidade media é {velo}km/h ')
print(f'sua distância é {destino}km ')
print(f'O tempo para chegar ao seu destino é {resultado:"h".2f}')