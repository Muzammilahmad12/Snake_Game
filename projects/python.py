from turtle import Screen
from main import Snake
from food import Food
from scoreboard import scoreBrd
import time


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


main = Snake()
food = Food()
scoreboard = scoreBrd()

screen.listen()
screen.onkey(main.up,"Up")
screen.onkey(main.down,"Down")
screen.onkey(main.left,"Left")
screen.onkey(main.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    main.move()    
    if main.head.distance(food) < 15:
        food.refresh()
        main.extend()
        scoreboard.IncreaseScore()    
    if main.head.xcor() > 280 or main.head.xcor() < -280 or main.head.ycor() > 280 or main.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()
    for segment in main.segment[1:]:
        if main.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()