import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Dodge Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)  # fastest animation speed

# Function to move the player turtle
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# Create a list of obstacles
obstacles = []

# Function to create obstacles
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Main game loop
while True:
    screen.update()

    # Create obstacles randomly
    if random.random() < 0.02:  # Adjust the probability to control obstacle creation rate
        create_obstacle()

    # Move each obstacle
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() - 1)  # Adjust the obstacle speed

        # Check for collision with player
        if obstacle.distance(player) < 20:
            obstacle.hideturtle()
            player.hideturtle()
            turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
            screen.update()
            screen.mainloop()

    # Remove obstacles that have gone off screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.xcor() > -300]

