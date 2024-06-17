import turtle as t
import winsound
import time

# Initialize scores
player_a_score = 0
player_b_score = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("pink")
window.setup(width=800, height=600)
window.tracer(0)

# Create the left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Create the right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Create the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball_dx = 0.2  # horizontal speed
ball_dy = 0.2  # vertical speed

# Create the score display
score_display = t.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0   Player B: 0", align="center", font=('Courier', 24, 'normal'))

# Function to move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    if y > 250:
        y = 250
    left_paddle.sety(y)

# Function to move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    if y < -240:
        y = -240
    left_paddle.sety(y)

# Function to move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    if y > 250:
        y = 250
    right_paddle.sety(y)

# Function to move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    if y < -240:
        y = -240
    right_paddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border collision checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_a_score += 1
        score_display.clear()
        score_display.write("Player A: {}   Player B: {}".format(player_a_score, player_b_score), align="center", font=('Courier', 24, 'normal'))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_b_score += 1
        score_display.clear()
        score_display.write("Player A: {}   Player B: {}".format(player_a_score, player_b_score), align="center", font=('Courier', 24, 'normal'))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    # Paddle collisions
    if (ball_dx > 0) and (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball_dx < 0) and (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Delay to control the game speed
    time.sleep(0.001)
