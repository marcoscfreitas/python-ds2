# -*- coding: utf-8 -*-
"""atividade2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15jcq_qWQDpSWYdoJBnLDXq8d7jp4tsuj
"""

#atividade 1

nomeVendedor = input('nome do vendedor:')
salarioFixo = float(input('salário fixo:'))
vendasEfetuadas = float(input('dinheiro em vendas efetuadas:'))

valorFinal = salarioFixo + ((15*vendasEfetuadas)/100)

print('a remuneração final de ' , nomeVendedor , ' é de ' , valorFinal)

#atividade 2

quilometragem = 12
tempoViagem = float(input('quantas horas tem a viagem? '))
velocidadeMedia = float(input('qual a velocidade média da viagem? '))
distanciaPercorrida = velocidadeMedia * tempoViagem
consumo = distanciaPercorrida/quilometragem

print(f'a quantidade de gasolina é: {consumo:.2f} litros.')

