from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.highscore = 0
        with open("leaderboard.txt") as leaderboard:
            content = leaderboard.readline()
            self.highscore = content
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
        self.goto(270, 220)
        self.write(f"Highscore:{self.highscore}", align="center", font=("Courier", 20, "bold"))

    def l_points(self):
        self.l_score+=1
        self.update_scoreboard()
    def r_points(self):
        self.r_score+=1
        self.update_scoreboard()


    def highscore_mechanism(self):
        if self.l_score>int(self.highscore):
            self.highscore = self.l_score
            with open("leaderboard.txt","w") as leaderboard:
                leaderboard.write(f"{self.highscore}")
        elif self.r_score> int(self.highscore):
            self.highscore=self.r_score
            with open("leaderboard.txt","w") as leaderboard:
                leaderboard.write(f"{self.highscore}")

        with open("leaderboard.txt") as leaderboard:
            content = leaderboard.readline()
            self.highscore = content