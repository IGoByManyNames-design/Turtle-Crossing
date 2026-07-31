from turtle import Screen,Turtle
import time
import player
import car

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)

ref = Turtle()
ref.ht()
ref.pencolor('white')
def scorecard():
    ref.clear()
    ref.penup()
    ref.goto(-350, 250)
    ref.write(arg='Level : ' + str(car.LEVEL), move=False, align='center', font=('Times New Roman', 24, 'bold'))

bob = player.Player()
car.army(5)
screen.listen()
screen.onkeypress(key='space', fun=bob.move)

is_game_on = True
iteration = 0
scorecard()

while is_game_on:
    time.sleep(0.05)
    screen.update()
    for i in car.bob_killer:
        i.move()
        if i.xcor() <= -400:
            i.reset()
    if bob.ycor() >= 270.0:
        car.LEVEL += 1
        bob.reset()
        for i in car.bob_killer:
            i.reset()
        car.army(1)
        scorecard()

    if iteration % 200 == 0:
        car.soldier()
    iteration += 1
    for i in car.bob_killer:
        if abs(bob.ycor() - i.ycor()) <= 20 and (bob.xcor() <= i.get_back() and bob.xcor() >= i.get_front()):
            is_game_on = False
            bob.dead()







screen.exitonclick()