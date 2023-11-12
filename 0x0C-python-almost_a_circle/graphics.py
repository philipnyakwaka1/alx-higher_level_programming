import turtle


def draw_shapes(rectangles, squares):
    # Create a Turtle object
    t = turtle.Turtle()

    # Set the speed of the turtle (optional)
    t.speed(1)  # You can adjust the speed as needed

    # Function to draw a rectangle
    def draw_rectangle(width, height):
        for _ in range(2):
            t.forward(width)  # Move the turtle forward by the width
            t.left(90)
            t.forward(height)
            t.left(90)        # Turn the turtle left by 90 degrees

    # Loop through rectangles and draw them
    for rectangle in rectangles:
        width, height = rectangle
        # Move to a new starting position (optional)
        t.penup()
        t.goto(t.xcor() + 50, t.ycor() + 50)  # Adjust the starting position
        t.pendown()
        draw_rectangle(width, height)

    # Function to draw a square
    def draw_square(side_length):
        for _ in range(4):
            # Move the turtle forward by the side length
            t.forward(side_length)
            t.left(90)              # Turn the turtle left by 90 degrees

    # Loop through squares and draw them
    for side_length in squares:
        # Move to a new starting position (optional)
        t.penup()
        t.goto(t.xcor() - 50, t.ycor() - 50)  # Adjust the starting position
        t.pendown()
        draw_square(side_length)

    # Close the Turtle graphics window when clicked
    turtle.exitonclick()


# Example usage:
rectangles = [(200, 100), (150, 75), (180, 90)]
squares = [100, 50, 80]

draw_shapes(rectangles, squares)
