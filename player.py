from turtle import Turtle
PLAYER_SPEED = 10

class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape('turtle')
        self.turtle.color('white')
        self.turtle.pencolor('magenta')
        self.turtle.pu()
        self.turtle.goto(0, -270)
        self.turtle.setheading(90)

    def move(self):
        self.turtle.fd(PLAYER_SPEED)

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def reset(self):
        self.turtle.goto(0, -270)

    def dead(self):
        a = Turtle()
        a.pencolor('red')
        a.ht()
        a.home()
        a.write(arg='Game Over', move=False, align='center', font=('Times New Roman', 48, 'bold'))