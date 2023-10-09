import turtle
h = int(input("Hauteur ? "))
l = int(input("Largeur ? "))

turtle.forward(l)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(l)
turtle.left(90)
turtle.forward(h)

turtle.exitonclick() 