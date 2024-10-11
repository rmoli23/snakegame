import turtle
from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake =Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


game_is_on=True   
    
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_segment()
        scoreboard.refresh()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on=False
        
   
        

        
      
    
    


screen.exitonclick()

