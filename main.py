import random   # for generating random values
import turtle   # for turtle graphics

# function to check whether turtle is in Screen or not
def isInScreen(win,turt):
    # getting the end points of turtle screen
    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    # getting the cuurent position of the turtle
    turtleX = turt.xcor()
    turtleY = turt.ycor()

    # variable to store whether in screen or not
    stillIn = True

    # condition to check whether in screen or not
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    # returning the result
    return stillIn

# function to check whether both turtle have different position or not
def sameposition(Red,Blue):
    if Red.pos()==Blue.pos():
        return False
    else:
        return True

#   main function
def main():

    # screen initialization for turtle
    wn = turtle.Screen()
    
    # Turtle Red initialization
    Red = turtle.Turtle()  # instantiate a new turtle object called 'Red'
    Red.pencolor("red")    # set pencolor as red
    Red.pensize(5)         # set pensize as 5
    Red.shape('turtle')    # set turtleshape as turtle
    pos=Red.pos()

    # Turtle Blue initialization
    Blue=turtle.Turtle()        # instantiate a new turtle object called 'Blue'
    Blue.pencolor("blue")       # set pencolor as blue
    Blue.pensize(5)             # set pensize as 5
    Blue.shape('turtle')       # set turtleshape as turtle    
    Blue.hideturtle()           # make the turtle invisible
    Blue.penup()                # don't draw when turtle moves
    Blue.goto(pos[0]+50,pos[1])       # move the turtle to a location 50 units away from Red
    Blue.showturtle()           # make the turtle visible
    Blue.pendown()              # draw when the turtle moves

    # variable to store whether turtles are in screen or not
    mT=True
    jT=True

    # loop for the game
    while mT and jT and sameposition(Red,Blue):

        # coin flip for Red
        coinRed = random.randrange(0, 2)

        # angle for Red
        angleRed=90 #random.randrange(0, 180)

        # condition for left or ight based on coin
        if coinRed == 0:
            Red.left(angleRed)
        else:
            Red.right(angleRed)

        # coin flip for Blue
        coinBlue = random.randrange(0, 2)

        # angle for Blue
        angleBlue=90 #random.randrange(0, 180)

        # condition for left or ight based on coin
        if coinBlue == 0:
            Blue.left(angleBlue)
        else:
            Blue.right(angleBlue)

        #draw for Red
        Red.forward(50)
        
        # draw for Blue
        Blue.forward(50)

        # cheking whether turtles are in the screen or not
        mT=isInScreen(wn,Blue)
        jT=isInScreen(wn,Red)

    # set pencolor for Blue and Red as black
    Red.pencolor("black")
    Blue.pencolor("black")

    # writting the name of turtles
    Red.write("Red ", True, align="center",font=("arial",15,"bold"))
    Blue.write("Blue ", True, align="center",font=("arial",15,"bold"))

    # condion check for draw or win
    if jT==True and mT==False:
        print("Turtle Red has won the match")
    elif mT==True and jT==False:
        print("Turtle Blue has won the match")
    else:
        print(" there was no winner")
        
    # exit on close
    wn.exitonclick()

#   Calling main function
main()
