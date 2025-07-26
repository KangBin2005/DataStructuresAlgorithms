import turtle  # Import the turtle graphics library
import math  # Import math module for mathematical operations
import random  # Import random module to generate random values

# Initialize the screen
screen = turtle.Screen()
screen.bgcolor("midnight blue")  # Set the background color to midnight blue for the night sky
screen.tracer(0)  # Turn off automatic screen updates to optimize drawing performance

# Initialize the turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")  # Set the turtle shape to a turtle
myTurtle.speed(0)  # Set the turtle's speed to the fastest

# Winter-themed tree colors
tree_colors = ["lightgray", "silver"]  # Colors for the frosty, icy tree trunk and branches
flower_colors = ["white", "lightblue"]  # Colors for snowy flowers
leaf_colors = ["lightgreen", "lightblue", "white"]  # Cool, pale greens and snow-dusted leaves

# Function to draw a single square with an outline and fill
def drawSquare(t, size, color):
    t.fillcolor(color)  # Set the fill color
    t.pendown()  # Put the pen down to start drawing
    t.begin_fill()  # Begin filling the shape
    for _ in range(4):  # Draw the 4 sides of the square
        t.forward(size)  # Move forward by the specified size
        t.left(90)  # Turn left by 90 degrees after each side
    t.end_fill()  # End the fill after completing the square
    t.penup()  # Lift the pen to stop drawing

# Recursive function to draw a tree node (part of the tree)
def drawNode(t, size, level):
    if level < 1:  # Base case: if level is less than 1, stop recursion
        return
    else:
        # Cycle through the colors for different tree parts
        if level % 2 == 0:  # Even levels are branches
            color = random.choice(tree_colors)  # Wintery icy colors for branches
        else:  # Odd levels are flowers or leaves
            color = random.choice(flower_colors if level > 2 else leaf_colors)  # Snowy flowers or leaves

        # Draw the current square with the selected color
        drawSquare(t, size, color)

        # Draw the left branch of the tree
        leftSize = size * math.sin(math.radians(30))  # Calculate the left branch size using sine(30°)
        t.forward(size)  # Move forward by the size of the square
        t.left(90)  # Turn left by 90 degrees to orient the turtle downward
        t.forward(size)  # Move forward again by the size of the square
        t.right(120)  # Turn right by 120 degrees to lean the turtle for the left branch
        t.forward(leftSize)  # Move forward by the calculated size for the left child
        t.left(90)  # Turn left by 90 degrees to prepare for recursive drawing of the left branch
        drawNode(t, leftSize, level - 1)  # Recursively draw the left branch, with a smaller size and lower level

        # Draw the right branch of the tree
        rightSize = size * math.cos(math.radians(30))  # Calculate the right branch size using cosine(30°)
        t.right(180)  # Turn 180 degrees to face the opposite direction
        t.forward(rightSize)  # Move forward by the calculated size for the right child
        t.left(90)  # Turn left by 90 degrees to prepare for recursive drawing of the right branch
        drawNode(t, rightSize, level - 1)  # Recursively draw the right branch, with a smaller size and lower level
        t.left(30)  # Turn left by 30 degrees to reset the turtle's angle after the right branch
        t.back(size)  # Move the turtle back by the size of the square to return to the previous position

# Function to draw snowflakes falling in the sky
def drawSnowflakes():
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.hideturtle()  # Hide the snowflake turtle
    snowflake_turtle.speed(0)  # Set the speed of the turtle to the fastest
    snowflake_turtle.penup()  # Lift the pen so it doesn't draw lines

    # List to hold snowflake data (x, y, size)
    snowflakes = []

    # Generate random snowflakes
    for _ in range(250):  # Create 250 snowflakes
        x = random.randint(-350, 350)  # Random x position within the screen width
        y = random.randint(100, 250)  # Random y position above the tree
        size = random.randint(5, 10)  # Random size for each snowflake
        snowflakes.append([x, y, size])  # Add snowflake data to the list

    # Function to draw a single snowflake at a given position
    def draw_snowflake(x, y, size):
        snowflake_turtle.goto(x, y)  # Move to the position of the snowflake
        snowflake_turtle.pendown()  # Put the pen down to draw
        snowflake_turtle.dot(size, "white")  # Draw a dot representing the snowflake
        snowflake_turtle.penup()  # Lift the pen again

    # Function to update the snowflakes' positions (falling effect)
    def fallSnowflakes():
        snowflake_turtle.clear()  # Clear the previous snowflakes from the screen
        for snowflake in snowflakes:
            x, y, size = snowflake
            if y > -250:  # If the snowflake is above the bottom of the screen
                snowflake[1] -= 2  # Move the snowflake downwards
            else:
                # Reset the snowflake to the top when it reaches the bottom
                snowflake[1] = random.randint(100, 250)
                snowflake[0] = random.randint(-350, 350)

            draw_snowflake(x, y, size)  # Draw the snowflake at its updated position

        # Redraw the snowflakes every 10 milliseconds for continuous falling effect
        screen.ontimer(fallSnowflakes, 10)  # Set a timer to repeat the falling snowflakes

    fallSnowflakes()  # Start the falling snowflakes effect

# Function to draw twinkling stars in the night sky
def drawStars():
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()  # Hide the star turtle
    star_turtle.speed(0)  # Set the speed of the turtle to the fastest
    star_turtle.penup()  # Lift the pen to avoid drawing lines

    stars = []  # List to hold star data (x, y, size, twinkle status)

    # Generate random stars in the sky
    for _ in range(30):  # Create 30 stars
        x = random.randint(-350, 350)  # Random x position within the screen width
        y = random.randint(100, 250)  # Random y position above the tree
        size = random.randint(3, 7)  # Random size for each star
        twinkle = random.choice([True, False])  # Randomly choose if the star twinkles
        stars.append([x, y, size, twinkle])  # Add star data to the list

    # Function to draw a single star at a given position
    def draw_star(x, y, size, color):
        star_turtle.goto(x, y)  # Move to the position of the star
        star_turtle.dot(size, color)  # Draw the star as a dot with the given color

    # Function to update the stars and create a twinkling effect
    def twinkle_stars():
        star_turtle.clear()  # Clear the previous stars from the screen
        for star in stars:
            x, y, size, twinkle = star
            color = random.choice(["white", "lightyellow", "lightblue", "silver"])  # Random star color

            if not twinkle:  # If the star does not twinkle, draw it statically
                draw_star(x, y, size, color)
            else:  # If the star twinkles, vary the brightness
                brightness = random.randint(3, 7)  # Random brightness for twinkling effect
                draw_star(x, y, brightness, color)

        # Redraw the stars every 100 milliseconds for the twinkle effect
        screen.ontimer(twinkle_stars, 100)

    twinkle_stars()  # Start the twinkling effect for the stars

# Function to draw a glowing moon in the sky
def drawMoon():
    moon_turtle = turtle.Turtle()
    moon_turtle.hideturtle()  # Hide the moon turtle
    moon_turtle.penup()  # Lift the pen to avoid drawing lines
    moon_turtle.goto(-200, 200)  # Position the moon at the top left of the screen
    moon_turtle.color("lightyellow")  # Set the moon color to light yellow

    # Create a glowing effect around the moon
    moon_turtle.begin_fill()  # Start filling the moon with color
    moon_turtle.circle(80)  # Draw a larger circle for the glow effect
    moon_turtle.end_fill()  # End the filling of the glow circle

    # Draw the main moon circle in the center of the glow
    moon_turtle.goto(-200, 200)
    moon_turtle.color("lightyellow")  # Set the moon color to light yellow
    moon_turtle.begin_fill()  # Begin filling the moon circle
    moon_turtle.circle(60)  # Draw a smaller circle for the main moon
    moon_turtle.end_fill()  # End the filling of the moon

# Position the turtle to start drawing the tree
myTurtle.penup()
myTurtle.goto(0, -150)  # Position the turtle closer to the center of the screen
myTurtle.left(90)  # Point the turtle upwards to start drawing

# Start drawing the Winter Tree
drawNode(myTurtle, 80, 8)  # Call the recursive function to draw the tree with level 8

# Draw stars with twinkle effect
drawStars()

# Draw the glowing moon
drawMoon()

# Add snowflakes falling continuously
drawSnowflakes()

# Hide the main turtle and update the screen
myTurtle.hideturtle()
screen.update()

# Wait for a click to close the window
screen.exitonclick()
