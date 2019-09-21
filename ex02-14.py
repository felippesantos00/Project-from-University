"""
Exercicio 02-14:Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
kmPercorrido = float(input('Quantos km foram percorridos? '))
diasAlugados = int(input('Quantos dias você utilizou o veiculo? '))
calculo = (60*diasAlugados)+(0.15*kmPercorrido)

print(f'você utilizou o veiculo por {diasAlugados} dias e rodou {kmPercorrido:.0f}km, portanto, você deve pagar R${calculo:.2f}')