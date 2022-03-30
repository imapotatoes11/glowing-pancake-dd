import turtle,random

turtle.speed(0)
turtle.goto(0,-100)
for i in range(20):
    turtle.fillcolor(random.choice(['yellow','green','green']))
    turtle.begin_fill()
    turtle.circle(200-i*10)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,i*10-100)
    turtle.pendown()

turtle.exitonclick()