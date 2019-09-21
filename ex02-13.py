"""
Exercicio 02-13:Escreva um programa que converta uma temperatura digitada em ºC em ºF.
A formula para a conversão é: F = ((9 x C)/5)=32
"""

C = float(input('Qual a temperatura atual °C: '))
converte = C * 1.8 + 32
print(f'A conversão em °F{converte:.1f}')