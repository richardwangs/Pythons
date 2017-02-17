import turtle
painter = turtle.Turtle()
#square
for i in range(2):
    painter.forward(200)          
    painter.right(90)
    painter.forward(50)         
    painter.right(90)
    
#triangle
painter.forward(200) 
painter.left(120)
painter.forward(200)
painter.left(120)
painter.forward(200)

#moves places
painter.up()
painter.left(120)
painter.forward(20)
painter.right(90)
painter.forward(10)
painter.down()

#windows
painter.forward(30)          
painter.left(90)
painter.forward(30)          
painter.left(90)
painter.forward(30)          
painter.left(90)
painter.forward(30)          
painter.left(90)

#moves places
painter.up()
painter.right(270)
painter.forward(130)
painter.down()
#windows

painter.forward(30)          
painter.right(90)
painter.forward(30)          
painter.right(90)
painter.forward(30)          
painter.right(90)
painter.forward(30)          
painter.right(90)
