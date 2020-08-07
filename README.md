# About the game
TurtleMove game is basically a luck-based game. In this game two-players (Red & Blue), using their own turtle (object) play the game.

## How to play:

The game is played in the predefined grid having some boundaries.

1) Both players move the turtle for a unit distance.

2) Now both players flip the coin:

        i) if HEAD, then take a right turn

       ii) else take a left turn

3) Now repeat 1 & 2, till both turtles lie in the boundary

## Implementation in Turtle Python

First, a turtle screen object is created for the grid boundary.

Now two turtles (Red & Blue) are created, one for each player.

Both turtles are moved a unit distance( turtle_obj.forward(50) )

Turn is decided, Using random.randrange(0, 2) i.e. 0 for left and 1 for the right.

after every move, the position of each turtle is checked, if any turtle crosses the boundary, then that turtle loses the game.

## Screenshot of the game

Start Of game
![alt text](https://github.com/iamjpsonkar/TurtleMove/blob/master/init%20game.jpg)


If Blue won
![alt text](https://github.com/iamjpsonkar/TurtleMove/blob/master/end%20game.jpg)

