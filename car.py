import random
import time
from turtle import Turtle
CAR_SPEED = 5
CAR_INCREMENT = 5
LEVEL = 1
CAR_COLOUR = ['red', 'blue', 'green', 'silver', 'orange', 'cyan', 'purple', 'yellow']

bob_killer = []

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.pu()
        self.length = random.randint(2,5)
        self.shapesize(stretch_len=self.length, stretch_wid=1)
        self.color(random.choice(CAR_COLOUR))
        self.xstart = random.randint(-400, 400)
        self.start = random.randint(-20, 25)*10
        self.setheading(180)

    def move(self):
        CAR_TRUE_SPEED = CAR_SPEED + CAR_INCREMENT*LEVEL
        self.fd(CAR_TRUE_SPEED)
    def reset(self):
        self.start = random.randint(-20, 25)*10
        self.goto(400, self.start)
        self.length = random.randint(2,5)
        self.shapesize(stretch_len=self.length, stretch_wid=1)
        self.color(random.choice(CAR_COLOUR))

    def get_front(self):
        return self.xcor() - self.length * 10
    def get_back(self):
        return self.xcor() + self.length * 10

def army(n):
    for i in range(n):
        a = Car()
        a.goto(a.xstart, a.start)
        bob_killer.append(a)
        time.sleep(random.random()/10)

def soldier():
    a = Car()
    a.goto(400, a.start)
    bob_killer.append(a)