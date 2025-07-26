import turtle

def drawTriangle(points ,color, myTurtle):
    # Set fill color
    myTurtle.fillcolor(color)
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0] ,points[0][1])
    myTurtle.down() # Pen down
    myTurtle.begin_fill()
    # Draw lines to connect 3 points
    myTurtle.goto(points[1][0] ,points[1][1])
    myTurtle.goto(points[2][0] ,points[2][1])
    myTurtle.goto(points[0][0] ,points[0][1])
    # Close triangle
    myTurtle.end_fill()


def getMid(p1 ,p2):
    # Calculate midpoint between 2 points
    return ( (p1[0 ] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points ,degree ,myTurtle):
    # Color map for the triangles, based on the recursion level
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow',
                'violet', 'orange']
    # Draw a triangle based on the 3 points given with appropriate color
    drawTriangle(points ,colormap[degree], myTurtle)
    # Eg: colormap[degree1] = red, colormap[degree2] = green , etc..

    # Base case: Draw 1 main triangle when degree is 0
    if degree > 0:
        # Recursive case: Recursively divide into smaller triangles
        # Draws bottom-left triangle
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)
        # Draws top triangle
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)
        # Draws bottom-right triangle
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)

# Main function to set up the turtle and draw the Sierpinski Triangle.
def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(100)   # adjust the drawing speed here
    myWin = turtle.Screen() # Creates drawing window

    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200 ,-50] ,[0 ,200] ,[200 ,-50]]
    degree = 5   # Vary the degree of complexity here


    # first call of the recursive function
    sierpinski(myPoints ,degree ,myTurtle)

    myTurtle.hideturtle(  ) # hide the turtle cursor after drawing is
    # completed

    myWin.exitonclick()  # Exit program when user click on window

# Run the program
main()
