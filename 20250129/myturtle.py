# import library
# pip install turtle  #run this command in terminal not here

import turtle
tv = turtle.Screen()

tom = turtle.Turtle()
tom.shape("turtle")
tom.color('green')

jerry = turtle.Turtle()
jerry.shape('turtle')
jerry.color('red')

tom.forward(100)
jerry.backward(100)

tom.left(90)
jerry.left(90)

tom.forward(200)
jerry.forward(200)

tv.exitonclick()

