from turtle import *

ALIGNMENT="center"
FONT=("Courier",16,"bold")
FONT_GAME_OVER=("Arial",24,"bold")

class Scoreboard(Turtle):
    
   
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("White")
        self.update_score()
        
        
    def update_score (self):
        
        self.clear()
        self.write(f"Score: {self.score}",False,ALIGNMENT,FONT)
        
    def refresh(self):
        self.score+=1
        self.update_score()
    
    def game_over(self):
        
        self.goto(0,0)
        self.write(f"GAME OVER",False,ALIGNMENT,FONT)
        
        