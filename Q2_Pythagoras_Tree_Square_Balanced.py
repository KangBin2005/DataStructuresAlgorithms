import turtle
import math
import random

# Initialize the screen
screen = turtle.Screen()
screen.bgcolor("midnight blue")  # Set the background color to a midnight blue for the night sky
screen.tracer(0)  # Disable automatic screen updates for smoother drawing

# Initialize the turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")  # Set the turtle shape to a "turtle"
myTurtle.speed(0)  # Set the turtle drawing speed to the fastest

# Predefined tree colors (earthy tones for the trunk and subtle greens for the leaves)
tree_colors = ["saddlebrown", "darkolivegreen", "darkgreen"]  # Colors for the tree trunk and leaves
flower_colors = ["lightpink", "lavender", "lightyellow"]  # Soft colors for flowers in the tree
leaf_colors = ["darkgreen", "forestgreen"]  # Dark green leaves for the night theme

# Function to draw a single square with a given size and color
def drawSquare(t, size, color):
    t.fillcolor(color)  # Set the fill color to the specified color
    t.pendown()  # Start drawing
    t.begin_fill()  # Begin filling the shape with the color
    for _ in range(4):  # Draw a square
        t.forward(size)  # Move forward by the square's size
        t.left(90)  # Turn left 90 degrees
    t.end_fill()  # Complete filling the square
    t.penup()  # Stop drawing

# Recursive function to draw a node with tree colors matching the midnight theme
def drawNode(t, size, level):
    if level < 1:  # Base case: stop drawing if the level is less than 1
        return
    else:
        # Choose tree color for even levels and flower or leaf color for odd levels
        if level % 2 == 0:  # Even levels (branches or trunk)
            color = random.choice(tree_colors)  # Choose a random tree color
        else:  # Odd levels (flowers or leaves)
            color = random.choice(flower_colors if level > 2 else leaf_colors)  # Choose a flower or leaf color

        # Draw the current square with the selected color
        drawSquare(t, size, color)

        # Calculate the size for the next branch (smaller than the current size)
        branchSize = math.sqrt(size * size / 2)  # Size of the next branch using the Pythagorean theorem

        # Draw the left branch
        t.forward(size)  # Move forward by the size
        t.left(90)  # Turn left 90 degrees
        t.forward(size)  # Move forward by the size again
        t.right(135)  # Turn right 135 degrees to start drawing the left branch
        t.forward(branchSize)  # Draw the left branch
        t.left(90)  # Turn left 90 degrees for the recursive call
        drawNode(t, branchSize, level - 1)  # Recursive call for the left branch with a smaller size

        # Draw the right branch
        t.right(180)  # Turn 180 degrees to face the opposite direction
        t.forward(branchSize)  # Move forward by the branch size
        t.left(90)  # Turn left 90 degrees
        drawNode(t, branchSize, level - 1)  # Recursive call for the right branch with a smaller size
        t.left(45)  # Turn left 45 degrees to restore the turtle's orientation
        t.back(size)  # Move backward to the starting position

# Function to draw stars in the night sky, with a twinkling effect
def drawStars():
    star_turtle = turtle.Turtle()  # Create a new turtle for drawing stars
    star_turtle.hideturtle()  # Hide the turtle while drawing
    star_turtle.speed(0)  # Set the drawing speed to the fastest
    star_turtle.penup()  # Lift the pen to avoid drawing lines

    stars = []  # List to store star data (x, y, size, twinkle status)

    # Draw random stars in the sky
    for _ in range(30):  # Number of stars to draw
        x = random.randint(-350, 350)  # Random x-coordinate
        y = random.randint(100, 250)  # Random y-coordinate (stars positioned above the tree)
        size = random.randint(3, 7)  # Random size for the stars
        twinkle = random.choice([True, False])  # Randomly decide if the star twinkles
        stars.append([x, y, size, twinkle])  # Store star data

    # Function to draw a single star at given position and size
    def draw_star(x, y, size, color):
        star_turtle.goto(x, y)  # Move the turtle to the star position
        star_turtle.dot(size, color)  # Draw the star with a dot

    # Function to update the twinkling stars
    def twinkle_stars():
        star_turtle.clear()  # Clear the previous stars
        for star in stars:  # Iterate over all stars
            x, y, size, twinkle = star
            color = random.choice(["white", "lightyellow", "lightblue", "silver"])  # Random color for the star

            # If the star does not twinkle, draw it with a fixed brightness
            if not twinkle:
                draw_star(x, y, size, color)

            # If the star twinkles, change its brightness randomly
            else:
                brightness = random.randint(3, 7)  # Random brightness for twinkling stars
                draw_star(x, y, brightness, color)

        # Redraw the stars every 100 milliseconds to simulate twinkling
        screen.ontimer(twinkle_stars, 100)

    twinkle_stars()  # Start the twinkling effect

# Function to draw fireflies that move around the tree
def drawFireflies():
    firefly_turtle = turtle.Turtle()  # Create a new turtle for fireflies
    firefly_turtle.hideturtle()  # Hide the turtle while drawing
    firefly_turtle.speed(0)  # Set the drawing speed to the fastest
    firefly_turtle.penup()  # Lift the pen to avoid drawing lines

    fireflies = []  # List to store firefly data (x, y, size, target_x, target_y)

    # Draw fireflies randomly scattered across the tree area
    for _ in range(40):  # Number of fireflies to draw
        x = random.randint(-150, 150)  # Random x-coordinate for firefly
        y = random.randint(-200, 200)  # Random y-coordinate for firefly
        size = random.randint(2, 5)  # Random size for fireflies
        target_x = random.randint(-100, 100)  # Random target x-coordinate
        target_y = random.randint(-150, 100)  # Random target y-coordinate
        fireflies.append([x, y, size, target_x, target_y])  # Store firefly data

    # Function to draw a firefly at a given position and size
    def draw_firefly(x, y, size):
        firefly_turtle.goto(x, y)  # Move to the firefly position
        firefly_turtle.setheading(random.randint(0, 360))  # Set a random direction
        firefly_turtle.pendown()  # Start drawing
        firefly_turtle.color(random.choice(flower_colors))  # Random color for fireflies
        firefly_turtle.begin_fill()  # Start filling the firefly shape

        # Draw a small oval for the firefly's body
        firefly_turtle.circle(size, 90)  # Half circle for the body
        firefly_turtle.left(90)
        firefly_turtle.circle(size, 90)  # Complete the oval shape
        firefly_turtle.end_fill()  # End the filling
        firefly_turtle.penup()  # Lift the pen to stop drawing

    # Function to move the fireflies towards their targets
    def move_fireflies():
        firefly_turtle.clear()  # Clear previous fireflies
        for firefly in fireflies:  # Iterate over all fireflies
            x, y, size, target_x, target_y = firefly
            dx = target_x - x  # Change in x-coordinate
            dy = target_y - y  # Change in y-coordinate
            distance = math.sqrt(dx ** 2 + dy ** 2)  # Calculate the distance to the target
            if distance > 5:  # Keep moving towards the target if not too close
                firefly[0] += dx / distance * 2  # Move firefly towards target in x direction
                firefly[1] += dy / distance * 2  # Move firefly towards target in y direction

            # Occasionally update the firefly's target position
            if random.random() < 0.02:  # 2% chance to change target
                target_x = random.randint(-100, 100)  # New target x-coordinate
                target_y = random.randint(-150, 100)  # New target y-coordinate

                firefly[3] = target_x  # Update target_x
                firefly[4] = target_y  # Update target_y

            draw_firefly(firefly[0], firefly[1], size)  # Draw the firefly

        # Redraw the fireflies every 50 milliseconds for movement
        screen.ontimer(move_fireflies, 50)

    move_fireflies()  # Start moving the fireflies

# Function to draw the glowing moon with a subtle glow effect
def drawMoon():
    moon_turtle = turtle.Turtle()  # Create a new turtle for the moon
    moon_turtle.hideturtle()  # Hide the turtle while drawing
    moon_turtle.penup()  # Lift the pen to avoid drawing lines
    moon_turtle.goto(-200, 200)  # Set the position for the moon
    moon_turtle.color("lightyellow")  # Set the color for the moon

    # Create a glowing effect around the moon
    moon_turtle.begin_fill()  # Start filling the glow
    moon_turtle.circle(80)  # Draw a larger circle for the glow
    moon_turtle.end_fill()  # Complete the glow effect

    # Draw the main moon circle
    moon_turtle.goto(-200, 200)  # Set the position for the main moon
    moon_turtle.color("lightyellow")  # Set the moon color again
    moon_turtle.begin_fill()  # Start filling the moon circle
    moon_turtle.circle(60)  # Draw a smaller circle for the moon
    moon_turtle.end_fill()  # Complete the moon drawing

# Position the turtle to start drawing the tree
myTurtle.penup()
myTurtle.goto(0, -150)  # Move the turtle to a starting position closer to the center
myTurtle.left(90)  # Rotate the turtle to face upwards

# Start drawing the Midnight Tree
drawNode(myTurtle, 80, 8)  # Begin drawing the tree with a size of 80 and recursion level of 8

# Draw stars with twinkle effect
drawStars()

# Draw the glowing moon
drawMoon()

# Add fireflies moving around the tree
drawFireflies()

# Hide the turtle and update the screen to display everything
myTurtle.hideturtle()
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()
