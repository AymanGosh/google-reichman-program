from turtle import *


color("green", "blue")


begin_fill()
while True:
    forward(50)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
write("may the force be with you!", align="right")
exitonclick()
