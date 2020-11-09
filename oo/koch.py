import turtle as t

def controllo_input(interacao):
    if interacao == "":
        interacao =4
    else:
        interacao = int(interacao)

    return interacao


def move():
    t.penup()
    t.backward(lunghezza/2)
    t.pendown()


def floco_de_neve_koch(lunghezza,interacao):
    for i in range(3):
        koch(lunghezza,interacao)
        t.right(120)


def koch(lunghezza, interacao):
    if interacao == 0:
        t.forward(lunghezza)
    else:
        lunghezza /= 3
        koch(lunghezza,interacao-1)
        t.left(60)
        koch(lunghezza,interacao - 1)
        t.right(120)
        koch(lunghezza,interacao - 1)
        t.left(60)
        koch(lunghezza,interacao - 1)




bob = t.Turtle()

t.speed(0)

lunghezza = 300
interacao = input("Inseriro numero de interação da curva de koch(Default ->4): ")
interacao = controllo_input(interacao)

move()

floco_de_neve_koch(lunghezza,interacao)

t.mainloop()

