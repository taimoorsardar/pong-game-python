from turtle import Turtle,Screen
from tkinter import Tk,PhotoImage,Label,Button,Toplevel,Canvas
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
from random import choice
from winsound import Beep

#This part makes the starting game window
window = Tk()
window.title('PONG GAME')
window.config(bg="black")
window.geometry("800x800+370+10")
window.resizable(0,0)
backgroundimage=PhotoImage(file="table pong.png")
background=Label(window,image=backgroundimage).pack()


#This part makes the actual game screen in which we play
screen = Screen()
screen.setup(width=800,height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)
screen.bgpic('background.png')
thomas = Turtle()
thomas.penup()

#This part is used to make the center line, set left and right paddles at pre-defined positions
thomas.goto(0,400)
thomas.setheading(270)
thomas.pencolor("white")
thomas.pensize(10)
for i in range(8):
    thomas.pendown()
    thomas.forward(50)
    thomas.penup()
    thomas.forward(50)

my_ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

score_board = Scoreboard()



#_____________________________________Color customization_______________________________

colors_list = ["green","yellow","purple","blue","pink","cyan","red","orange","brown"]
def change_to_yellow():                     #Changes colour of paddles, scoreboard and ball to yellow by '1'
    score_board.color("yellow")
    my_ball.color("yellow")
    r_paddle.color("yellow")
    l_paddle.color("yellow")

def change_to_green():                      #Changes colour of paddles, scoreboard and ball to green by '2'
    score_board.color("green")
    my_ball.color("green")
    r_paddle.color("green")
    l_paddle.color("green")

def change_to_orange():                     #Changes colour of paddles, scoreboard and ball to orange by '3'
    score_board.color("orange")
    my_ball.color("orange")
    r_paddle.color("orange")
    l_paddle.color("orange")


def random_color():                         #Changes colour of paddles, scoreboard and ball to any random colour from 'colors_list' by '0'
    col = choice(colors_list)
    score_board.color(col)
    my_ball.color(col)
    r_paddle.color(col)
    l_paddle.color(col)

#This function makes our control window
def control():
    
    w=Toplevel()
    bg=PhotoImage(file='controls.png')
    w.geometry('800x600+370+150')
  
    w.title('Controls')
    w.resizable(0,0)
    background=Canvas(w,height=600,width=800)
    background.pack()
    background.create_image(0,0,image=bg,anchor='nw')
    
    
    background.create_text(400,70,text='\t\tFOR RIGHT PADDLE\n to move up-> up arrow\tto move down->down arrow',fill='white',font='Arial 14 bold')
    background.create_text(405,20,text='CONTROLS',fill='white',font='Helvetica 20 bold')
    background.create_text(380,120,text='\t    FOR LEFT PADDLE\n to move up-> w   \t   to move down-> s',fill='white',font='Arial 14 bold')
    background.create_text(200,200,text='To pause-> p\nTo resume-> r',fill='white',font='Arial 14 bold')
    background.create_text(600,230,text='CHANGE COLOURS \n to yellow-> 1\n to green-> 2 \n to orange->3 \n to random colour-> 0',fill='white',font='Arial 14 bold')
    background.create_text(220,400,text='Cheat codes \ncode\t\ttrigger\tend\nball invisible\tb\tn\nvanish right\ty\tt\nvanish left\tl\tk',fill='green',font='Helvetica 20 bold')
    background.create_text(580,400,text='Boss Key-> x',fill='white',font='Helvetica 20 bold')
    w.mainloop()

#This function makes our credits window
def credits():
    c=Toplevel()
    cred=PhotoImage(file='credits.png')
    c.geometry('800x600+370+150')
  
    c.title('Credits')
    c.resizable(0,0)
    background=Canvas(c,height=600,width=800)
    Button(c,text='back',command=c.destroy).pack()
    background.pack()
    background.create_image(0,0,image=cred, anchor="nw")
    c.mainloop()

def exit():
    screen.bye()
    window.destroy()



#This function pauses the game by 'p'
def pause():
    global game_is_on
    game_is_on=False


#This function resumes the game by 'r'
def resume():
    global game_is_on
    game_is_on = True
    the_game()



#This function makes the bosskey as 'assignment screen' by 'x'
def create_bosskey():
    pause()
    boss_window=Tk()
    boss_window.minsize(100, 100)
    boss_window.config(bg="black")
    boss_window.geometry("800x914+370+0")
    backgroundimage = PhotoImage(file="thebosskey.PNG")

    background = Label(boss_window, image=backgroundimage)
    Button(boss_window,text='back',command=boss_window.destroy).pack()
    background.pack()
    boss_window.resizable(0,0)
    boss_window.mainloop()
    


#______________Creating Cheat Codes___________
#creating a simple cheat code in which the ball becomes invisible to the other player for 5 seconds by 'b'
cheat_code_timer = 5
def cheat_code_ball():
    my_ball.color("black")

def end_cheat_ball():        #Ends cheat of invisbile ball by 'n'
    my_ball.color("white")

#These are simple cheats to make the right or left paddle invisible to either player as per demand by 'y' and 'l' respectively 
def cheat_right_inviz():
    r_paddle.color("black")
def cheat_left_inviz():
    l_paddle.color("black")

#These are used to END THE CHEATS which make right or left paddle invisible by 't' and 'k' respectively
def cheat_right_end():
    r_paddle.color("white")
def cheat_left_end():
    l_paddle.color("white")


#______Key assignment_________
#From here onward, we use .onkey to set every function to be performed at the press of a specific key
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.onkey(change_to_yellow,"1")
screen.onkey(change_to_green,"2")
screen.onkey(change_to_orange,"3")
screen.onkey(random_color,"0")

screen.onkey(cheat_left_inviz,"l")
screen.onkey(cheat_right_inviz,"y")
screen.onkey(cheat_right_end,"t")
screen.onkey(cheat_left_end,"k")
screen.onkey(cheat_code_ball,"b")
screen.onkey(end_cheat_ball,"n")

screen.onkey(pause,"p")
screen.onkey(resume,"r")
screen.onkey(create_bosskey,"x")


#the_game function runs the game
rep = 1
game_is_on = True

def the_game():
    global rep
    if rep==1:
        window.destroy()
    while game_is_on:
        rep+=1

        sleep(my_ball.TIMECONSTANT)
        screen.update()

        my_ball.move_ball()
        score_board.highscore_mechanism()


        if my_ball.ycor()>280 or my_ball.ycor()<-280:
            my_ball.up_bounce()

        if my_ball.distance(r_paddle) < 50 and my_ball.xcor()>330:
            my_ball.down_bounce()
            my_ball.TIMECONSTANT-=0.01
            Beep(500,100)
        if my_ball.distance(l_paddle) < 50 and my_ball.xcor()<-330:
            my_ball.down_bounce()
            my_ball.TIMECONSTANT -=0.01
            Beep(500,100)
        if my_ball.xcor()> 380 :
            score_board.l_points()
            my_ball.reset_ball()
            Beep(500,100)
        if my_ball.xcor() < -380:
            score_board.r_points()
            my_ball.reset_ball()
            Beep(500,100)

start_button = Button(window,text="Start Game",padx=10,pady=10,bg="black",fg='white',command =the_game ).pack()
controls=Button(window,text='controls',padx=18,pady=10,bg='black',fg='white',command=control).pack()
credits_button=Button(window,text='credits',padx=20,pady=10,bg='black',fg='white',command=credits).pack()
exit_button=Button(window,text='Exit',padx=20,pady=10,bg='black',fg='white',command=exit).pack()

window.mainloop()
screen.exitonclick()