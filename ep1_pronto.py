# -*- coding: utf-8 -*-

import turtle
import random

print('ENTRADA: F-F-F-F')
print('REGRA: F yF-pF+xF+bFoF-rF-gF+bF ')
turtle.setpos(-400,0)
pen = turtle.Pen()
def get_color():
    colors  = ["red","green","blue","orange","purple","pink","yellow","black"]
    return random.choice(colors)

inicial = str(input("Entrada: "))
regra1 =str(input("regra1: "))
regra2 =str(input("regra2: "))
passos=int(input("passos: "))

final=""
regra1 = regra1.split(' ')
regra2 = regra2.split(' ')

i=0
while i < passos:
    final = inicial.replace(regra1[0],regra1[1])
    final = inicial.replace(regra2[0],regra2[1])
    inicial=final
    i+=1

print(final)
turtle.speed('fast')
for i in final:
    if i=='f':
        turtle.penup()
        turtle.forward(10)

#for i in final.upper(): 
for i in final:            
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
        
        