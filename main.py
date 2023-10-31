import turtle
import random

dimensiuni_petale = [10, 15, 20, 25, 30, 35, 40, 45, 50] #vectorul din care se alege marimea florii
def desen_floare(x, y):
    f = turtle.Screen()
    f.bgcolor("black") #culoarea de fundal

    t = turtle.Turtle()
    t.speed(10) #viteza cu care ruleaza cursorul sa realizeze desenul
    t.color("pink") #culoarea florii

    t.penup() #nu mai deseneaza
    t.goto(x, y) #se duce la x,y ul din vectorul de pozitii
    t.pendown() #deseneaza

    dimensiune_petale = random.choice(dimensiuni_petale) #alege din vectorul de dimensiuni, in mod aleatoriu, ce
    #marime o sa aiba floarea, deci de fiecare data o sa apara un alt desen pe ecran

    t.begin_fill()
    for i in range(6): #de 6 ori se executa comenzile de mai jos
        t.circle(dimensiune_petale, 130) #deseneaza conturul unei petale a florii
        t.left(170) #aici se intoarce la 170 de grade la stanga si deseneaza urmatoarea petala
    t.end_fill()

    t.hideturtle() #dispare cursorul de pe ecran dupa ce termina de desenat



pozitii = [ #vectorul de pozitii, adica unde pe ecran sa apara florile
    (0, 0),
    (200, 0),
    (-200, 0),
    (0, 200),
    (0, -200),
    (200, 200),
    (-200, -200),
    (200, -200),
    (-200, 200)
]

for poz in pozitii: # pentru fiecare pozitie din vector, deseneaza o floare
    desen_floare(poz[0], poz[1])

turtle.done()
