# -*- coding: utf-8 -*-
"""atividade4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i9aX-85ZPejAwu3sCDu-j49qB2qIPtYN
"""

#verificar se é maior de idade

idade = int(input('digite sua idade:'))

if idade<18 :
  print('voce é MENOR de idade')
else :
  print('voce é MAIOR de idade')

#verificar animal

animal = input('digite um animal: ')

if animal.lower() == 'cachorro' :
  print('é um cachorro')
elif animal.lower() == 'gato' :
  print('é um gato')
else :
  print('é outro animal')

#imprimir ímpares

for i in range (1,100, 2) :
  print(i)

#verificar media numeros

#numeros = int(input('digite um número: '))
media = 0
numero = 0
div=0
while numero != -1 :
  numero = int(input('digite um número: '))
  if numero == -1 :
    break
  div+=1
  media+=numero
  print(media)
  print(div)
print((media)/div)

#soma fração

s = 0
n = int(input('digite um número: '))
div = n

while div!=0 :
  s+=1/div
  div-=1
  print(n,s,div)
print(s)

#numeros entre 1000 e 2000 quando divididos por 11 sobre 5

for i in range(1000,2001) :
  if i%11 == 5 :
    print(i)