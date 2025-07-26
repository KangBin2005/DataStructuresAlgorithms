import turtle
import math

def drawCircle(center, size, color, myTurtle):
    """
    Draw a filled circle with the specified center, size, and color.
    Size here refers to the diameter of the circle.
    """
    myTurtle.fillcolor(color)  # Set the fill color
    myTurtle.up()  # Pen up
    myTurtle.goto(center[0], center[1] - size / 2)  # Move to the top of the circle
    myTurtle.down()  # Pen down
    myTurtle.begin_fill()
    myTurtle.circle(size / 2)  # Draw the circle (radius = size / 2)
    myTurtle.end_fill()

def sierpinskiCircle(center, size, degree, myTurtle, rotation = 0):
    """
    Recursive function to draw the Sierpinski Circle fractal.
    Size refers to the diameter of the circles.
    Includes rotation for smaller circles.
    """
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow', 'violet', 'orange']

    # Draw the main circle
    drawCircle(center, size, colormap[degree % len(colormap)], myTurtle)

    # Base case: Stop recursion when degree is 0
    if degree > 0:
        # Define the size of the smaller circles based on the current circle size
        newSize = size / 3  # Initially, smaller circles are 1/3 the size of the large circle

        # Increase the size of the smaller circles until they touch each other
        newSize *= 1.25  # Slightly increase the size to make sure they touch each other perfectly

        # Calculate the distance from the center to the edge of the large circle
        offset = size / 2 - newSize / 2  # Ensure that smaller circles touch each other and the boundary

        # Angles for the three smaller circles (315°, 45°, and 135°) with rotation
        # - for clockwise, + for anticlockwise
        angles = [(315 - rotation) % 360, (45 - rotation) % 360, (135 - rotation) % 360]

        # Calculate the positions for the smaller circles
        red_centers = []
        for angle in angles:
            # Convert angle to radians
            angle_rad = math.radians(angle)

            # Calculate the x and y coordinates of the smaller circle centers
            x = center[0] + offset * math.cos(angle_rad)
            y = center[1] + offset * math.sin(angle_rad)
            red_centers.append([x, y])

        # Draw the three smaller circles
        for red_center in red_centers:
            # Recursively call for the smaller circles with updated rotation
            sierpinskiCircle(red_center, newSize, degree - 1, myTurtle, rotation + 90)

# Main function to set up the turtle and draw the Sierpinski Circle.
def main():
    # Set up turtle
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)  # Set turtle speed to fastest
    myWin = turtle.Screen()  # Create the drawing window

    # Center and size (diameter) of the initial large circle
    center = [0, 0]
    size = 300  # This is the diameter of the large circle
    degree = 5  # Adjust recursion depth

    # Draw the Sierpinski Circle fractal
    sierpinskiCircle(center, size, degree, myTurtle)

    # Hide the turtle cursor and wait for user to click
    myTurtle.hideturtle()
    myWin.exitonclick()

# Run the program
main()
