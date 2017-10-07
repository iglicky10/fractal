# -*- coding: utf-8 -*-

import turtle
import random
manual='''
Bem vindo ao desenhador de fractais!!
Este programa funciona com uma entrada, regra e repetiçoes que retornam um desenho.
Manual:
    Comandos de direçao:
        f = Ir para frente
        - = Virar 90 graus para direita
        + = Virar 90 graus para esquerda
        * = Virar 60 graus para direita
        / = Virar 60 graus para esquerda
        . = Virar 45 graus para direita
        , = Virar 45 graus para esquerda
    Cores:
         r = Vermelho
         g = Verde
         b = Azul
         o = Laranja
         p = Roxo
         y = Amarelo
         k = Preto
         x = Cor aleatória
    
   
ENTRADA: F-F-F-F
REGRA: F F-F+F+FF-F-F+F
PASSOS: 2

Teste agora com cores!

ENTRADA: F-F-F-F
REGRA: F xF-xF+xF+xFxF-xF-xF+xF
PASSOS: 2

Teste mudando o numero de passos!!

Obs: Pode escrever em letras minúsculas!!
Obs2: Fique a vontade em criar a sua entrada e regra!!
'''
print(manual)
turtle.shape('turtle')
pen = turtle.Pen()
def get_color():
    colors  = ["red","green","blue","orange","purple","pink","yellow","black"]
    return random.choice(colors)

inicial = str(input("Entrada: "))
regra =str(input("regra: "))
passos=int(input("passos: "))

final=""
regra = regra.split(' ')


i=0
while i < passos:
    final = inicial.replace(regra[0],regra[1])
    inicial=final
    i+=1

print(final)
turtle.speed('fast')

for i in final.upper():           
    if i =='F':
       turtle.pendown() 
       turtle.forward(10)
    elif i=='-':
        turtle.right(90)
    elif i=='+':
        turtle.left(90)
    elif i=='*':
        turtle.right(60)
    elif i=='/':
        turtle.left(60)
    elif i=='.':
        turtle.right(45)
    elif i==',':
        turtle.left(45)
    elif i=='R':
        turtle.color('red')
    elif i=='G':
        turtle.color('green')
    elif i=='B':
        turtle.color('blue')
    elif i=='O':
        turtle.color('orange')
    elif i=='P':
        turtle.color('purple')
    elif i=='Y':
        turtle.color('yellow')
    elif i=='K':
        turtle.color('k')
    elif i=='X':
        turtle.color(get_color())
        
       