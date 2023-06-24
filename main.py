from turtle import Turtle, Screen
from turtle_race import MyRaceCourse

my_turtle = Turtle()
my_screen = Screen()

# Turtle Race project #
new_race = MyRaceCourse(this_screen=my_screen)
new_race.screen_adjustment(set_width=600, set_height=500)
new_race.race_setup(total_turtles=8)
