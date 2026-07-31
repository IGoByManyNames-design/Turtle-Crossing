from turtle import Turtle
PLAYER_SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.pencolor('magenta')
        self.pu()
        self.teleport(x=0, y=-270)
        self.setheading(90)

    def move(self):
        self.fd(PLAYER_SPEED)
    def reset(self):
        self.teleport(x=0, y=-270)

    def dead(self):
        a = Turtle()
        a.pencolor('red')
        a.ht()
        a.home()
        a.write(arg='Game Over', move=False, align='center', font=('Times New Roman', 48, 'bold'))