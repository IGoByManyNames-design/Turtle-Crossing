import random
import time
from turtle import Turtle
CAR_SPEED = 5
CAR_INCREMENT = 5
LEVEL = 1
CAR_COLOUR = ['red', 'blue', 'green', 'silver', 'orange', 'cyan', 'purple', 'yellow']

bob_killer = []

class Car:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape('square')
        self.turtle.pu()
        self.length = random.randint(2, 5)
        self.turtle.shapesize(1, self.length)
        self.turtle.color(random.choice(CAR_COLOUR))
        self.xstart = random.randint(-400, 400)
        self.start = random.randint(-20, 25)*10
        self.turtle.setheading(180)

    def move(self):
        CAR_TRUE_SPEED = CAR_SPEED + CAR_INCREMENT*LEVEL
        self.turtle.fd(CAR_TRUE_SPEED)

    def reset(self):
        self.start = random.randint(-20, 25)*10
        self.turtle.goto(400, self.start)
        self.length = random.randint(2, 5)
        self.turtle.shapesize(1, self.length)
        self.turtle.color(random.choice(CAR_COLOUR))

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def get_front(self):
        return self.turtle.xcor() - self.length * 10

    def get_back(self):
        return self.turtle.xcor() + self.length * 10

def army(n):
    for i in range(n):
        a = Car()
        a.turtle.goto(a.xstart, a.start)
        bob_killer.append(a)
        time.sleep(random.random()/10)

def soldier():
    a = Car()
    a.turtle.goto(400, a.start)
    bob_killer.append(a)