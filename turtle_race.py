from turtle import Turtle, colormode
import random as r


class MyRaceCourse:
    def __init__(self, this_screen):
        """Constructor for MyRaceCourse class. Initializes the turtle Screen for use"""
        self.my_screen = this_screen

    def screen_adjustment(self, set_width, set_height):
        """Screen dimensions adjustment method to modify the size of the panel window."""
        self.my_width = set_width
        self.my_height = set_height
        self.my_screen.setup(width=set_width, height=set_height)

    def racer_colour(self):
        """Returns a random Tuple for (r, g, b) format colour coding."""
        my_colour = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        return my_colour

    def racer_movement(self, racers, finish_line):
        """Returns the index of the Racing Turtles list upon simulating the random movement logic."""
        moving_racer = r.randint(0, len(racers) - 1)
        race = True
        while race:
            racers[moving_racer].forward(r.randint(5,10))
            if racers[moving_racer].xcor() >= finish_line:
                race = False
                self.my_screen.bye()
            else:
                moving_racer = r.randint(0, len(racers) - 1)
        return moving_racer

    def race_setup(self, total_turtles):
        """The main setup for the race. Sets up the turtles in place, prompts for Betting, Simulate the race and determine the Winner."""
        race_turtles = [Turtle(shape="turtle") for _ in range(total_turtles)]
        factor = (self.my_height - 50) / total_turtles
        value = - ((total_turtles - 1) * factor) / 2
        for my_turtle in race_turtles:
            colormode(255)
            my_turtle.color(self.racer_colour())
            my_turtle.penup()
            my_turtle.goto(x=(-(self.my_width / 2) + 15), y=value)
            value += factor
        user_turtle = self.my_screen.numinput(title="Turtle Bet",
                                              prompt="Choose your turtle to bet on (No. order from bottom): ",
                                              maxval=total_turtles, minval=1)
        user_bet = self.my_screen.numinput(title="Turtle Bet", prompt="Set the bet amount: ", minval=0, default=0)
        winner_turtle = self.racer_movement(race_turtles, (self.my_width / 2)) + 1
        if winner_turtle == user_turtle:
            print(f"Hurray! Your Turtle no. {int(user_turtle)} won the race. You won ₹{user_bet} amount.")
        else:
            print(f"Turtle no. {winner_turtle} won! \nYour Turtle (no. {int(user_turtle)}) lost the race. You loose ₹{user_bet} amount.")
