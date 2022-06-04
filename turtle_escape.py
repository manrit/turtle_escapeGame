# Mai Pham, John Anthony Mart Diego, Manrit Kaur
# 6/2/22
# Final Project: Turtle Escape Game

import random
import turtle

# Approximate size of turtle objects in pixels
BODY_SIZE = 80

# Half if the body size for collision detection with the edge of the screen
HALF_BODY_SIZE = BODY_SIZE / 2

# if enemies get this close to friend there is collision
COLLISION_DISTANCE = 5

# The window size
SIZE = 500

# inner boundary within window for reversing the direction of enemies
LOWER_BOUND = -SIZE / 2 + HALF_BODY_SIZE
UPPER_BOUND = SIZE / 2 - HALF_BODY_SIZE
print(LOWER_BOUND, UPPER_BOUND)

# Create screen
win = turtle.Screen()
win.delay(0)
win.tracer(2)
win.setup(500,500)
win.title('Turtle Escape')

# creating our main turtle 'friend'
friend = turtle.Turtle()
friend.penup()
friend.shape('turtle')
friend.color('lime')
friend.shapesize(3)
friend.goto(win.window_width() / 2 - BODY_SIZE, - win.window_height() / 2 + BODY_SIZE)
border = win.window_width() / 2

# create the red balls
def create_turtle():
    red = turtle.Turtle()
    red.color('red')
    red.shape('circle')
    red.penup()
    red.shapesize(3, 3)
    red.setheading(random.randrange(0, 360))

    return red

def move(t):
    x, y = t.position()
    if x > border or y > border or y < -border or x < -border:
        t.forward(-5)
        t.setheading(random.randrange(360))



def up():
    friend.penup()
    friend.setheading(90)
    friend.forward(45)
    friend.pendown()


def down():
    friend.penup()
    friend.setheading(270)
    friend.forward(45)
    friend.pendown()


def left():
    friend.penup()
    friend.setheading(180)
    friend.forward(45)
    friend.pendown()


def right():
    friend.penup()
    friend.setheading(0)
    friend.forward(45)
    friend.pendown()


# If turtle friend collides with enemies
def collision(friend, enemies):
        is_collision = False
        for enemy in enemies:
            dist = friend.distance(enemy.pos())
            if dist <= COLLISION_DISTANCE:
                is_collision = True
        return is_collision

# if turtle friend reaches the other corner
def reached_opposite_corner(friend):
    reached_corner = False
    x, y = friend.pos()
    if x < LOWER_BOUND and y > UPPER_BOUND:
        reached_corner = True
    return reached_corner

enemies = []
for i in range(5):
    enemies.append(create_turtle())

# move turtle friend using arrows
win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(down, "Down")
win.listen()

# Repeat until a collision or friend as reached upper left corner
while True and not collision(friend, enemies) and not reached_opposite_corner(friend):
    for enemy in enemies:
        enemy.forward(5)
        move(enemy)

# Checking whether player won or not
if reached_opposite_corner(friend):
    print("Game over: Your friend made it!")
elif collision(friend, enemies):
    print("Game over: Your friend is now turtle soup!")
else:
    print("Game over: Unknown reason: Programming error!")