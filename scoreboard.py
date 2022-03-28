from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscoredata.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"your score: {self.score} High Score = {self.high_score}", align="center", font=("Arian", 24, "normal"))
        #để tránh các dòng thông báo điểm bị đè lên nhau
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscoredata.txt", mode= "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arian", 24, "normal"))

    def increase_score(self):
        self.score +=1
        # self.clear()#dọn thông báo trước đó
        self.update_scoreboard()








