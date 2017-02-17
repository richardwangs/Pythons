import turtle 

star = turtle.Turtle()

for i in range(100):
    if i%2==0:
        star.pencolor("red")
    if i%2!=0:
        star.pencolor("blue")

    star.forward(i * 10)
    star.right(144)
