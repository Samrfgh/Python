import turtle
import time
import random

delay = 0.1
score = 0
high = 0
cycle_id = 419

segments = []
vis = []
path = []
positions = []
d1 = []

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
    head.turtlesize(1,1,1)
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

# score system
def score_init():
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.ht()
    pen.goto(0,300)
    pen.write("Score: 0  High Score: 0", align = "center", font = ("Monaco", 24, "normal"))

def draw_boundary():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t1.ht()
    t2.ht()
    t3.ht()
    t4.ht()
    t1.goto(-291,271)
    t2.goto(-291,-291)
    t3.goto(271,-291)
    t4.goto(271,271)
    t1.color("white")
    t2.color("white")
    t3.color("white")
    t4.color("white")
    t1.forward(562)
    t2.left(90)
    t2.forward(562)
    t3.left(180)
    t3.forward(562)
    t4.left(270)
    t4.forward(562)

def cache_cycle_path():
    x = -14
    y = 13
    for i in range(0, 784):
        d1.append((x,y))
        if path[i] == 'D': y -= 1
        if path[i] == 'R': x += 1
        if path[i] == 'L': x -= 1
        if path[i] == 'U': y += 1

def dist(u, v):
    if u <= v: return v - u
    else: return 784 - u + v

def contains_segment(s, e):
    for i in segments:
        x = (s + 1) % 784
        while x != e + 1:
            if (i.xcor()/20,i.ycor()/20) == d1[x]: return 1
            x = (x + 1) % 784
    return 0

def can_jump_up(x,y):
    if (x,y+1) in d1 and head.direction != "down" and in_body(x,y+1) == 1:
        if d1.index((x,y+1)) <= d1.index(food_pos) and contains_segment(d1.index((x,y)),d1.index((x,y+1))) == 0:
            return d1.index((x,y+1))
    return -1

def can_jump_right(x,y):
    if (x+1,y) in d1 and head.direction != "left" and in_body(x+1,y) == 1:
        if d1.index((x+1,y)) <= d1.index(food_pos) and contains_segment(d1.index((x,y)),d1.index((x+1,y))) == 0:
            return d1.index((x+1,y))
    return -1

def can_jump_left(x,y):
    if (x-1,y) in d1 and head.direction != "right" and in_body(x-1,y) == 1:
        if d1.index((x-1,y)) <= d1.index(food_pos) and contains_segment(d1.index((x,y)),d1.index((x-1,y))) == 0:
            return d1.index((x-1,y))
    return -1

def jump_selection(x,y):
    a = can_jump_up(x,y)
    b = can_jump_right(x,y)
    c = can_jump_left(x,y)
    m = max(a,b,c)
    if m == -1 or dist(m,d1.index(food_pos)) > dist(cycle_id,d1.index(food_pos)) or expanded == 1:
        return 0
    if m == a: return 1
    if m == b: return 2
    if m == c: return 3

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up" :
        head.sety(y + 20)

    if head.direction == "down" :
        head.sety(y - 20)

    if head.direction == "left" :
        head.setx(x - 20)

    if head.direction == "right" :
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
    if head.xcor()/20 == x and head.ycor()/20 == y: return 0
    for i in segments:
        if i.xcor()/20 == x and i.ycor()/20 == y:
            return 0
    return 1

path = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'U', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']

# main loop
screen_setup()
head_init()
food_init()
score_init()
draw_boundary()
cache_cycle_path()
food_pos = (0,5)
expanded = 0

while True:

    root.update()

    if len(segments) == 783:
        print("VICTORY")

    # check for collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for i in segments:
            i.goto(1000,1000)
        segments.clear()
        score = 0
        cycle_id = 419
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high), align = "center", font = ("Monaco", 24, "normal"))

    # move food
    if head.distance(food) < 20 :
        x = random.randint(-14,13)
        y = random.randint(-14,13)
        while True:
            if in_body(x,y) == 0:
                x = random.randint(-14,13)
                y = random.randint(-14,13)
            else: break

        food.goto(x*20,y*20)
        food_pos = (x,y)
        expanded = 1

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

    x = head.xcor()/20
    y = head.ycor()/20

    t = jump_selection(x,y)
    expanded = 0
    # detect jumps
    if t == 0:
        if path[cycle_id] == 'U': go_up()
        if path[cycle_id] == 'D': go_down()
        if path[cycle_id] == 'L': go_left()
        if path[cycle_id] == 'R': go_right()
        cycle_id = (cycle_id + 1) % 784

    elif t == 1:
        head.direction = "up"
        cycle_id = d1.index((x,y+1))

    elif t == 2:
        head.direction = "right"
        cycle_id = d1.index((x+1,y))

    elif t == 3:
        head.direction = "left"
        cycle_id = d1.index((x-1,y))

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
            cycle_id = 419
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high), align = "center", font = ("Monaco", 24, "normal"))

    #time.sleep(delay)

root.mainloop()
