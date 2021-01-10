import turtle
import time
import random
import os
import math

# SET UP SCREEN
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders by Kunal Choudhary")
window.bgpic("space_invaders_background.gif")
window.tracer(0)

window.register_shape("invader.gif")
window.register_shape("player.gif")




# DRAW BORDER
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-275,-275)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(550)
    border_pen.left(90)
border_pen.hideturtle()
#Score
score = 0
#DRAW SCORE
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-265, 250)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Calibri", 14, "normal"))
score_pen.hideturtle()




# CREATE THE PLAYER TURTLE
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -225)
player.setheading(90)

player.speed = 0.2


# CHOOSE NUMBER OF ENEMIES
number_of_enemies = 30
# CREATE AN EMPTY LIST OF ENEMIES
enemies = []

# ADD ENEMIES TO LIST
for i in range(number_of_enemies):
    # CREATE ENEMY INVADER
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

    enemyspeed = 0.5

# CREATE PLAYER LASER
bullet = turtle.Turtle()
bullet.color("orange")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)

bulletspeed = 10

# BULLET STATE
# READY = READY TO FIRE
# FIRE = BULLET IS FIRING

# MOVE THE PLAYER LEFT AND RIGHT
def go_left():
    player.speed = -3


def go_right():
    player.speed = 3


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -260:
        x = -260
    if x > 260:
        x = +260
    player.setx(x)


def fire_bullet():
    # Delcare variable as global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
    # MOVE BULLET JUST ABOVE PLAYER
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False




# BIND KEYBOARD
window.listen()
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "s")
window.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    window.update()
    move_player()
    for enemy in enemies:
        # MOVE THE ENEMY
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # MOVE ENEMY BACK AND DOWN and checking for border touch
        if enemy.xcor() > 260:
           # MOVES ALL ENEMIES DOWN
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # CHANGE DIRECTION
            enemyspeed *= -1


        if enemy.xcor() < -260:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

            # BULLET COLLISION WITH ENEMY
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(0, 10000)
            #UPDATE SCORE
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Calibri", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("You lose, game over!")
            break


    # MOVE BULLET
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)


    # CHECK BULLET TOUCHING BORDER
    if bullet.ycor() > 255:
        bullet.hideturtle()
        bulletstate = "ready"








