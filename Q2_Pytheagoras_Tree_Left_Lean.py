import turtle
import math
import random

# Initialize the screen with a midnight blue background, simulating a night sky
screen = turtle.Screen()
screen.bgcolor("midnight blue")  # Set the background color to midnight blue
screen.tracer(0)  # Turn off automatic screen updates for performance

# Initialize the main turtle for drawing the tree
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")  # Set the turtle shape to "turtle"
myTurtle.speed(0)  # Set the turtle speed to the fastest for drawing

# Predefined colors for different parts of the tree to match the rainy night theme
tree_colors = ["dimgray", "darkslategray", "darkgray"]  # Dark colors for tree trunk and branches
flower_colors = ["lightblue", "lavender", "lightgray"]  # Soft colors for flowers
leaf_colors = ["darkgreen", "forestgreen", "olive"]  # Muted dark greens for damp leaves


# Function to draw a single square with an outline
def drawSquare(t, size, color):
    t.fillcolor(color)  # Set the fill color of the square
    t.pendown()  # Start drawing
    t.begin_fill()  # Start filling the shape
    for _ in range(4):  # Draw the four sides of the square
        t.forward(size)
        t.left(90)  # Turn by 90 degrees for a square
    t.end_fill()  # End the filling
    t.penup()  # Lift the pen to move without drawing


# Recursive function to draw a node (part of the tree)
def drawNode(t, size, level):
    if level < 1:  # Base case: stop recursion if level is less than 1
        return
    else:
        # Alternate between tree branches and flowers or leaves based on the level
        if level % 2 == 0:  # Even levels are for branches
            color = random.choice(tree_colors)  # Choose a tree color
        else:  # Odd levels are for flowers or leaves
            color = random.choice(flower_colors if level > 2 else leaf_colors)  # Choose flower or leaf color

        # Draw the square at the current level
        drawSquare(t, size, color)

        # Calculate the size and angle for the left and right branches
        leftSize = size * math.sin(math.radians(60))  # Left branch size based on sine(60°)
        t.forward(size)  # Move forward by the current square size
        t.left(90)  # Turn left by 90 degrees
        t.forward(size)  # Move forward again by the square size
        t.right(150)  # Tilt the turtle for the left branch angle
        t.forward(leftSize)  # Move forward by the left branch size
        t.left(90)  # Turn left by 90 degrees to prepare for drawing the left branch recursively
        drawNode(t, leftSize, level - 1)  # Recursively draw the left branch

        # Repeat for the right branch
        rightSize = size * math.cos(math.radians(60))  # Right branch size based on cosine(60°)
        t.right(180)  # Turn the turtle around to face the opposite direction
        t.forward(rightSize)  # Move forward by the right branch size
        t.left(90)  # Turn left by 90 degrees to prepare for the right branch
        drawNode(t, rightSize, level - 1)  # Recursively draw the right branch
        t.left(60)  # Reset the turtle angle after the right branch
        t.back(size)  # Move backward by the square size to return to the original position


# Function to draw stars in the night sky, with a twinkling effect
def drawStars():
    star_turtle = turtle.Turtle() # Create a new turtle for drawing stars
    star_turtle.hideturtle()  # Hide the turtle as we only need to draw the stars
    star_turtle.speed(0)  # Set the turtle to the fastest speed
    star_turtle.penup()  # Lift the pen to avoid drawing unnecessary lines

    stars = []  # List to hold data for the stars (position, size, twinkle status)

    # Generate random positions and characteristics for the stars
    for _ in range(30):  # Draw 30 stars for a scattered effect
        x = random.randint(-350, 350)  # Random x-coordinate for the star
        y = random.randint(100, 250)  # Random y-coordinate for the star
        size = random.randint(3, 7)  # Random size for each star
        twinkle = random.choice([True, False])  # Randomly decide if the star twinkles
        stars.append([x, y, size, twinkle])  # Add the star data to the list

    # Function to draw a single star
    def draw_star(x, y, size, color):
        star_turtle.goto(x, y)  # Move the turtle to the star position
        star_turtle.dot(size, color)  # Draw the star with a dot

    # Function to update the twinkling effect of the stars
    def twinkle_stars():
        star_turtle.clear()  # Clear previous stars to update the scene
        for star in stars:
            x, y, size, twinkle = star
            color = random.choice(["white", "lightyellow", "lightblue", "silver"])  # Random star colors

            # Draw static stars (no twinkle)
            if not twinkle:
                draw_star(x, y, size, color)

            # Draw twinkling stars (random brightness)
            else:
                brightness = random.randint(3, 7)  # Random brightness for twinkling effect
                draw_star(x, y, brightness, color)

        # Redraw stars every 100 milliseconds for the twinkle effect
        screen.ontimer(twinkle_stars, 100)

    twinkle_stars()  # Start the twinkling effect for the stars


# Function to draw the glowing moon
def drawMoon():
    moon_turtle = turtle.Turtle()
    moon_turtle.hideturtle()  # Hide the turtle
    moon_turtle.penup()  # Lift the pen
    moon_turtle.goto(-200, 200)  # Position the moon on the screen
    moon_turtle.color("lightyellow")  # Moon color

    # Draw a glowing effect around the moon using a large circle
    moon_turtle.begin_fill()
    moon_turtle.circle(80)  # Draw a large circle for the glow effect
    moon_turtle.end_fill()

    # Draw the main moon as a smaller circle inside the glow
    moon_turtle.goto(-200, 200)
    moon_turtle.begin_fill()
    moon_turtle.circle(60)  # Smaller circle for the moon itself
    moon_turtle.end_fill()


# Function to create rain effect
def drawRain():
    rain_turtle = turtle.Turtle()
    rain_turtle.hideturtle()  # Hide the turtle for rain drawing
    rain_turtle.speed(0)  # Set the turtle to the fastest speed
    rain_turtle.penup()  # Lift the pen to avoid drawing unnecessary lines

    raindrops = []  # List to hold the raindrop data (position and size)

    # Generate random positions and lengths for the raindrops
    for _ in range(100):  # Draw 100 raindrops
        x = random.randint(-350, 350)  # Random x-coordinate for raindrop
        y = random.randint(50, 250)  # Random y-coordinate for raindrop
        length = random.randint(10, 20)  # Random length for each raindrop
        raindrops.append([x, y, length])  # Add raindrop data to the list

    # Function to draw a single raindrop
    def draw_raindrop(x, y, length):
        rain_turtle.goto(x, y)  # Move to the raindrop's position
        rain_turtle.setheading(270)  # Point the turtle downwards
        rain_turtle.pendown()  # Start drawing the raindrop
        rain_turtle.pensize(2)  # Set the pen size
        rain_turtle.pencolor("lightblue")  # Set the color of the raindrop
        rain_turtle.forward(length)  # Draw the raindrop
        rain_turtle.penup()  # Lift the pen after drawing the raindrop

    # Update function to animate the rain
    def updateRain():
        rain_turtle.clear()  # Clear the previous raindrops
        for raindrop in raindrops:
            x, y, length = raindrop
            y -= 10  # Move the raindrop down
            if y < -250:  # Reset raindrop if it goes off-screen
                y = 250
            draw_raindrop(x, y, length)  # Draw the raindrop at its new position
            raindrop[1] = y  # Update the raindrop's y-position

        # Redraw the rain every 50 milliseconds for animation effect
        screen.ontimer(updateRain, 50)

    updateRain()  # Start the rain animation


# Function to simulate lightning strikes in the scene
def drawLightning():
    lightning_turtle = turtle.Turtle()
    lightning_turtle.hideturtle()  # Hide the turtle for lightning drawing
    lightning_turtle.speed(0)  # Set the turtle to the fastest speed
    lightning_turtle.penup()  # Lift the pen to avoid drawing unnecessary lines

    # Function to trigger a lightning flash at a random position and angle
    def lightningFlash():
        x = random.randint(-400, 400)  # Random x-coordinate for lightning
        y = random.randint(100, 250)  # Random y-coordinate for lightning
        angle = random.randint(-60, 60)  # Random angle for lightning bolt

        # Draw the lightning bolt
        lightning_turtle.goto(x, y)
        lightning_turtle.setheading(angle)  # Set random angle for the lightning bolt
        lightning_turtle.pendown()  # Start drawing the lightning
        lightning_turtle.pensize(4)  # Set the pen size
        lightning_turtle.pencolor("white")  # Set the lightning color to white
        lightning_turtle.goto(x + random.randint(-100, 100), y - random.randint(100, 300))  # Randomize the endpoint
        lightning_turtle.penup()  # Lift the pen after drawing the lightning

        # Clear the lightning after 1-2 seconds and trigger another lightning flash
        screen.ontimer(clearLightning, random.randint(1000, 2000))

    # Function to clear the lightning after it's drawn
    def clearLightning():
        lightning_turtle.clear()  # Clear the lightning flash from the screen
        screen.ontimer(lightningFlash, random.randint(3000, 7000))  # Trigger another lightning flash after 3-7 seconds

    lightningFlash()  # Start the first lightning flash


# Position the turtle to start drawing the tree
myTurtle.penup()
myTurtle.goto(0, -150)  # Move the turtle to the starting position for the tree
myTurtle.left(90)  # Face the turtle upwards to start drawing

# Start drawing the Midnight Tree with a recursion depth of 10
drawNode(myTurtle, 80, 10)

# Draw stars with a twinkling effect
drawStars()

# Draw the glowing moon
drawMoon()

# Add the rain effect
drawRain()

# Simulate lightning and thunder
drawLightning()

# Hide the main turtle and update the screen
myTurtle.hideturtle()
screen.update()

# Wait for a click to close the window
screen.exitonclick()
