from turtle import *
speed(10)

color("green", "blue")


begin_fill()
while True:
    forward(300)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()
