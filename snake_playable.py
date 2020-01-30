import turtle
import time
import random

delay = 0.1
score = 0
high = 0
segments = []

root = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()
pen = turtle.Turtle()

# screen setup
def screen_setup():
    root.title("Snake")
    root.bgcolor("black")
    root.setup(width=650,height=700)
    root.tracer(0)

# snake head
def head_init():
    head.speed(0)
    head.color("#42D816")
    head.shape("square")
    head.penup()
    head.turtlesize(0.9,0.9,0.9)
    head.goto(0,0)
    head.direction = "stop"

# snake food
def food_init():
    food.speed(0)
    food.color("red")
    food.shape("circle")
    food.penup()
    food.goto(0,100)
    food.turtlesize(0.9,0.9,0.9)
    food.direction = "stop"

def score_init():
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.ht()
    pen.goto(0,300)
    pen.write("Score: 0  High Score: 0", align = "center", font = ("Monaco", 24, "normal"))

def draw_boundary():
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.ht()
    border.goto(-291,-291)
    border.pensize(3)
    border.pendown()
    for i in range(4):
        border.fd(582)
        border.lt(90)

def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def in_body(x,y):
    for i in segments:
        if i.xcor()/20 == x and i.ycor()/20 == y:
            return 0
    return 1

# keyboard bindings
def key_bind():
    root.listen()
    root.onkeypress(go_up,"Up")
    root.onkeypress(go_up,"w")
    root.onkeypress(go_down,"Down")
    root.onkeypress(go_down,"s")
    root.onkeypress(go_left,"Left")
    root.onkeypress(go_left,"a")
    root.onkeypress(go_right,"Right")
    root.onkeypress(go_right,"d")

# main loop
screen_setup()
head_init()
food_init()
score_init()
key_bind()
draw_boundary()

while True:
    root.update()

    # check for collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for i in segments:
            i.goto(1000,1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high), align = "center", font = ("Monaco", 24, "normal"))

    if head.distance(food) < 20 :
        # move food
        x = random.randint(-14,14)
        y = random.randint(-14,14)

        while True:
            if in_body(x,y) == 0:
                x = random.randint(-14,13)
                y = random.randint(-14,13)
            else: break

        food.goto(x*20,y*20)

        # add snake length
        seg = turtle.Turtle()
        seg.speed(0)
        seg.color("#41CF17")
        seg.shape("square")
        seg.penup()
        seg.turtlesize(0.9,0.9,0.9)
        segments.append(seg)
        score += 1
        high = max(high, score)
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high), align = "center", font = ("Monaco", 24, "normal"))

    # move segments
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for body collisions
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for i in segments:
                i.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high), align = "center", font = ("Monaco", 24, "normal"))

    time.sleep(delay)

root.mainloop()
