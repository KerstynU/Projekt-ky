from turtle import Turtle, Screen
import random
 
tommy = Turtle()
tommy.shape("turtle")
 
colors = ["azure2", "brown4", "chartreuse", "coral1", "red", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4", "blue4", "pink"]
rotation = [0, 90, 180, 270]
speed = 1
 
for number in range(200):
    random_color = random.choice(colors)
    tommy.pencolor(random_color)

    if number <= 10:
        tommy.pensize(number)
 
    tommy.forward(30)
    tommy.right(random.choice(rotation))
 
    tommy.speed(speed)
    speed += 1
 
my_screen = Screen()
my_screen.exitonclick()
