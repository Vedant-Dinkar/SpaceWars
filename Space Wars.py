import multiprocessing
import turtle
import math
import random
import time
import urllib.request
import os


          


#THERE ARE SOME LINES WHERE IT IS REQUIRED TO CHANGE THE LOCATION OF THE PICTURE FILE. PLEASE MAKE CHANGES TO THE FILE LOCATIONS AFTER DOWNLOADING THEM.
#LINES ARE MARKED ONE LINE BEFORE BY "#LOCATION" WITH AN INDENT.
#TRY NOT TO GIVE TOO MANY CONTROLS AT ONE TIME.
#IF THE PROGRAM IS SHOWING ERROR AFTER OS QUESTION THEN TRY REMOVING SOUND OPTION.
#THIS PROGRAM WAS MADE ON MAC OS, SOME STATEMENTS MIGHT BE BROKEN ON OTHER OSs.



difficulty=0
tym=0
fire=0
frvrlp=1
abscissa=0
firing=0
spd=8
m=0
n=0
hits=0
evade=0
evadechance=0
g=0
health=100
bossnumber=1
score=0
a=0
b=0
eatk=0
rocketlife=200




name=input("Hello there! What's your name?\n")
time.sleep(1)
if name=="Voldemort" :
    print("So you are YouKnowWho?",)
else :
    print("So you are ", name,"?",)

yon=int(input("1 = Yes,   2 = No\n"))
while yon==2 or yon!=1:
    name=input("Hello there! What's your name?\n")
    time.sleep(1)
    if name=="Voldemort" :
        print("So you are YouKnowWho?",)
    else :
        print("So you are ", name,"?",)
    yon=int(input("1 = Yes,   2 = No\n"))



time.sleep(1)
operatingsystem=int(input("What OS are you in?  1 = Windows.  2 = Mac.  3 = Linux.\n"))
while operatingsystem != 1 and operatingsystem != 2 and operatingsystem != 3 :
    print("\nPlease enter a valid number.")
    time.sleep(2)
    operatingsystem=int(input("What OS are you in?  1 = Windows.  2 = Mac.  3 = Linux.\n"))





if operatingsystem == 1 :
                                 #LOCATION
    import winsound
    playsound("/Users/aksharadinkar/Downloads/Music.mp3")
if operatingsystem == 2 :
    import subprocess
                                 #LOCATION
    subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Music.mp3"])

if operatingsystem == 3 :
    import subprocess
                                 #LOCATION
    subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Music.mp3"])
       


















screen = turtle.Screen()
screen.setup(width=1000, height=600)
turtle.bgcolor("Black")
time.sleep(2)
text=turtle.Turtle()
text.hideturtle()
text.speed(0)
text.penup()
text.begin_fill()
text.color("#ff6600","#ff6600")
text.setheading(0)
text.goto(-10,-20)
text.pendown() #MID
text.forward(20)
text.left(90)
text.forward(115)
text.left(90)
text.forward(20)
text.left(90)
text.forward(115)
text.end_fill()
text.penup() #CROSS 
text.goto(-40,60)
text.begin_fill()
text.pendown()
text.setheading(0)
text.forward(80)
text.right(90)
text.forward(15)
text.right(90)
text.forward(80)
text.right(90)
text.forward(15)
text.end_fill()
text.penup() #LEFT
text.goto(-45,80)
text.begin_fill()
text.pendown()
text.setheading(0)
text.forward(15)
text.right(90)
text.forward(80)
text.right(90)
text.forward(15)
text.right(90)
text.forward(80)
text.end_fill()
text.penup() #RIGHT
text.goto(45,80)
text.begin_fill()
text.pendown()
text.setheading(180)
text.forward(15)
text.left(90)
text.forward(80)
text.left(90)
text.forward(15)
text.left(90)
text.forward(80)
text.end_fill()
text.penup()











#I-SEE STUDIOS
time.sleep(2)
text.goto(-55,-100)
text.color("white","white")
text.write(" Icy", font=("Futura", 50, "bold"))
text.goto(-53,-150)
text.write("Studios", font=("Futura", 30, "italic"))
text.goto(-370,-280)
text.write("CopyrightTM @2015-2020. All rights reserved.                                                                                                                                                                                                                                         ~Vedantisthebest on Scratch.", font=("Times New Roman", 7, "bold")) 
print("\n                                                                                                            Icy Studios")
time.sleep(6)
text.clear()
time.sleep(0.5)






#GAME NAME
level=turtle.Turtle()
level.hideturtle()
gamelogo=turtle.Turtle()
missile=turtle.Turtle()
missile.hideturtle()
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/BOOM.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/SPACEWARS.gif"))
                             #LOCATION
gamelogo.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/SPACEWARS.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/Controls.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/Missile.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/SpaceShip.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/EnemyMissile.gif"))

print("\n                                                                                                             Space Wars")





#DECLARATION TO PREVENT LAG
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(abscissa,-160)
circle = turtle.Turtle()
rct=turtle.Turtle()
aim=turtle.Turtle()
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/Rocket.gif"))
                             #LOCATION
screen.addshape(os.path.expanduser("/Users/aksharadinkar/Downloads/Aim.gif"))
aim.hideturtle()
aim.penup()
aim.speed(10)
enatk=turtle.Turtle()










levelwriter=turtle.Turtle()
levelwriter.hideturtle()
levelwriter.speed(0)
levelwriter.pendown()
circle.hideturtle()
rct.hideturtle()
load=turtle.Turtle()
fload=turtle.Turtle()
load.hideturtle()
fload.hideturtle()
load.penup()
fload.penup()
load.color("white","white")
load.speed(0)
fload.speed(0)
load.goto(-420,-270)
load.setheading(0)
load.pendown()
load.showturtle()
text.goto(-380, -270)
text.write("Loading...", font=("Futura", 20))
for i in range(9):
    
    load.pendown
    load.forward(1.2)
    load.left(3.6)
    print("\nLoading... ( 0",i+1, ")%")

boom=turtle.Turtle()
boom.hideturtle()
boom.penup()
attack=turtle.Turtle()
attack.hideturtle()
attack.color("cyan", "blue")
attack.penup()
attack.goto(abscissa, -160)

    
enhlth=turtle.Turtle()
enhlth.speed(0)
enhlth.penup()
enhlth.hideturtle()
enhlth.goto(410, 200)


myhlth=turtle.Turtle()
myhlth.speed(0)
myhlth.penup()
myhlth.hideturtle()
myhlth.goto(410, -200)



enemy=turtle.Turtle()
enemy.penup()
enemy.hideturtle()
enemy.speed(0)
enemy.goto(0, 200)
enemy.speed(1)
scor=turtle.Turtle()
scor.penup()
scor.hideturtle()
scor.goto(-440, 260)
scorewriter=turtle.Turtle()
scorewriter.hideturtle()
scorewriter.penup()
    
    
fload.goto(-420, -270)
fload.setheading(0)
fload.pendown()
fload.showturtle()

for j in range(91):
    load.pendown()
    fload.pendown()
    load.forward(1.2)
    fload.forward(1.2)
    load.left(3.6)
    fload.left(3.6)
    print("\nLoading... (", j+10, ")%")
text.clear()        
load.clear()
fload.clear()
load.penup()
fload.penup()
load.hideturtle()
fload.hideturtle()
controls=turtle.Turtle()
time.sleep(2)
gamelogo.penup()
gamelogo.hideturtle()
                             #LOCATION
controls.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/Controls.gif"))
missile.penup()
                             #LOCATION
missile.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/Missile.gif"))
                             #LOCATION
enemy.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/SpaceShip.gif"))


time.sleep(6)
controls.hideturtle()



enboom=turtle.Turtle()
enboom.hideturtle()
enboom.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/BOOM.gif"))
enboom.penup()
enboom.speed(0)





myhlth.color("yellow", "yellow")
enhlth.color("#00ff00", "#00ff00")




def timeelapsed():
    global tym
    time.sleep(1)
    tym+=1
    
def timecounter():
    while tym<10000 :
        timeelapsed()
        print(tym)







                             #LOCATION
screen.bgpic("/Users/aksharadinkar/Downloads/Space.gif")








                             
print("Hello there Captain", name,"! We are heading towards the Andromeda Galaxy!", end='')
time.sleep(3)
print("\nWhat was that!")
time.sleep(3)
print("\nThat must have been Varth Dader! Shoot him down using UP ARROW and Aim using LEFT CLICK.")
time.sleep(5)
print("\nDEFEAT OPPONENTS TO INCREASE YOUR SCORE. EACH MISSILE COUNTS TO INCREASE IN DIFFICULTY.")
time.sleep(5)
                             #LOCATION
t.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/Rocket.gif"))
t.showturtle()
                             #LOCATION
boom.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/BOOM.gif"))
                             #LOCATION
enatk.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/EnemyMissile.gif"))







                             #LOCATION
aim.shape(os.path.expanduser("/Users/aksharadinkar/Downloads/Aim.gif"))
enatk.hideturtle()
enatk.penup()
rokthealth=turtle.Turtle()
rokthealth.penup()
rokthealth.hideturtle()




comments=turtle.Turtle()
comments.hideturtle()
comments.penup()
comments.speed(0)
comments.goto(-420, 120)



def PlayerControls():
    def get_mouse_click_coor(p, q) :
        global m,n
        if q>0 :
            n=(q//10)*10
        m=(p//10)*10    
        aim.goto(m,n)
        aim.showturtle()
        
        




    rct.speed(0)
    rct.showturtle()
    rct.penup()
    rct.goto(-460, -260)
    rct.color("black", "cyan") 
    rct.begin_fill()
    for e in range(2) :
        rct.forward(150)
        rct.left(90)
        rct.forward(220/3)
        rct.left(90)
    rct.end_fill()
        
    rct.hideturtle()
    scor.penup()
    scor.speed(0)
    scor.goto(-450, -235)
    scor.color("black", "black")
    scor.write("Score : ", font=("Cooper", 20, "bold"))
    scorewriter.goto(-380, -235)
    scorewriter.write("0", font=("Cooper", 20, "bold"))

    enemy.showturtle()
    enemy.speed(0)
    level.speed(0)
    level.penup()
    level.goto(-450, -255)
    level.color("black", "black")
    level.write("Level : ", font=("Cooper", 20, "bold"))
    levelwriter.penup()
    levelwriter.goto(-380, -255)
    levelwriter.write("1", font=("Cooper", 20, "bold"))

    rokthealth.speed(0)
    rokthealth.goto(-450, -215)
    rokthealth.color("black", "black")
    rokthealth.write("Health : ", font=("Cooper", 20, "bold"))
    rokthealth.goto(-375, -215)
    rokthealth.write("200", font=("Cooper", 20, "bold"))



    comment=1


    comments.color("#00ff00", "#00ff00")


        

            





    def up() :
        t.setheading(90)
        t.forward(5)
        
        
        
        
    def down():
        t.setheading(270)
        t.forward(5)



    def left():
        global abscissa
        if abscissa > -300 and firing==0:
            t.setheading(180)
            abscissa-=spd
            t.forward(spd)
            
        else :
            abscissa+=0
         


    def right():
        global abscissa
        if abscissa < 300 and firing==0:
            t.setheading(0)
            abscissa+=spd
            t.forward(spd)
            

           
        
            
    def centre():
        t.showturtle()
        t.goto(0,-160)

        



    



    def hit() :
           global comment, firing, hits, evade, difficulty, eatk, evadechance, g, health, n, score, bossnumber, rocketlife
           
           
           if firing==0 :
               firing=1
               if difficulty<80:
                   difficulty+=0.5
                   missile.speed(0)
                   missile.goto(abscissa, -160)
                   missile.speed(3)
                   boom.speed(0)
                   
                   evadechance=random.randint(0,10-difficulty//10)
                   
                   if evadechance==0 or evadechance==1 :
                       comments.clear()
                       g=random.randint(-360, 360)
                       enemy.speed(0)
                       enemy.goto(g,200)
                       if m not in range (g-20, g+20) and n in range (180, 220) :
                           comments.write("Evade", font=("Cooper", 30, "bold"))
                           
                   
                   missile.showturtle()
                   missile.goto(m,n)
                   missile.hideturtle()
                   boom.goto(m,n)
                   boom.showturtle()
                   
                   if m in range (g-20, g+20) and n in range (180,220):
                       health-=random.randint(50,100)
                       hlth=random.randint(50,100)
                       health-=hlth
                       score+=5
                       scorewriter.clear()
                       scorewriter.write(score, font=("Cooper", 20, "bold"))
                       
                       comments.clear()
                       comment=random.randint(0,5)
                       if comment==0:      
                            comments.write("Impressive!", font=("Cooper", 30, "bold"))
                            
                       if comment==1:
                            comments.write("Excellent!", font=("Cooper", 30, "bold"))
                            
                       if comment==2:
                            comments.write("BAM!", font=("Cooper", 30, "bold"))
                            
                       if comment==3:
                            comments.write("DESTROYED!", font=("Cooper", 30, "bold"))
                            
                       if comment==4:
                            comments.write("Fantastic!", font=("Cooper", 30, "bold"))
                            
                       if comment==5:
                            comments.write("Awesome!", font=("Cooper", 30, "bold"))
                          
                       if health <= 0 :
                           bossnumber+=1
                           health=(bossnumber-1)*50+100
                           score+=bossnumber*25 + 50
                           scorewriter.clear()
                           scorewriter.write(score, font=("Cooper", 20, "bold"))
                           levelwriter.clear()
                           levelwriter.goto(-380, -255)
                           levelwriter.write(bossnumber, font=("Cooper", 20, "bold"))
                           difficulty+=5
                           
                       if bossnumber==11 :
                           print("Congratulations", name, "Varth Dader has been defeated! Your final score was", score, "Points. Impressive!")          
                           enemy.hideturtle()
                           turtle.clear()
                           print("You Win! Your final score was", score, "Points. At Level", bossnumber,".")
                           text.speed(0)
                           text.penup()
                           text.goto(-20,0)
                           text.color("#00ff00")
                           text.write("You Win!", font=("Cooper", 40, "bold"))
                       enhlth.clear()
                       enhlth.write(hlth*-1, font=("Cooper", 30, "italic"))
                       time.sleep(1)
                       enhlth.clear()
                       comments.clear()
                       
                   else :
                       if score>=5 :
                           score-=5
                           scorewriter.clear()
                           scorewriter.write(score, font=("Cooper", 20, "bold"))     
                    
                   evade=0
                   firing=0
                   time.sleep(0.8)
                   boom.hideturtle()
                   comments.clear()
                   
                   
                               
               else :
                   missile.speed(0)
                   missile.goto(abscissa, -160)
                   missile.speed(3)
                   boom.speed(0)
                   
                   evadechance=random.randint(0,10-difficulty//10)
                   
                   if evadechance==0 or evadechance==1 :
                       comments.clear()
                       g=random.randint(-360, 360)
                       enemy.speed(0)
                       enemy.goto(g,200)
                       if m not in range (g-20, g+20) and n in range (180, 220) :
                           comments.write("Evade", font=("Cooper", 30, "bold"))
                          
                  
                   missile.showturtle()
                   missile.goto(m,n)
                   missile.hideturtle()
                   boom.goto(m,n)
                   boom.showturtle()
                   if m in range (g-20, g+20) and n in range (180,220):
                       health-=random.randint(50,100)
                       hlth=random.randint(50,100)
                       health-=hlth
                       score+=5
                       scorewriter.clear()
                       scorewriter.write(score, font=("Cooper", 20, "bold"))
                       
                       comments.clear()
                       comment=random.randint(0,5)
                       if comment==0:      
                            comments.write("Impressive!", font=("Cooper", 30, "bold"))
                            
                       if comment==1:
                            comments.write("Excellent!", font=("Cooper", 30, "bold"))
                            
                       if comment==2:
                            comments.write("BAM!", font=("Cooper", 30, "bold"))
                            
                       if comment==3:
                            comments.write("DESTROYED!", font=("Cooper", 30, "bold"))
                            
                       if comment==4:
                            comments.write("Fantastic!", font=("Cooper", 30, "bold"))
                            
                       if comment==5:
                            comments.write("Awesome!", font=("Cooper", 30, "bold"))
                           
                       
                       if health <= 0 :
                           bossnumber+=1
                           health=(bossnumber-1)*50+100
                           score+=bossnumber*25 + 50
                           scorewriter.clear()
                           scorewriter.write(score, font=("Cooper", 20, "bold"))
                           levelwriter.clear()
                           levelwriter.goto(-380, -255)
                           levelwriter.write(bossnumber, font=("Cooper", 20, "bold"))
                           
                       if bossnumber==11 :
                           
                           print("Congratulations", name, "Varth Dader has been defeated! Your final score was", score, "Points. Impressive!")          
                           enemy.hideturtle()
                           
                           turtle.clear()
                           print("You Win! Your final score was", score, "Points. At Level", bossnumber,".")
                           text.speed(0)
                           text.penup()
                           text.goto(-20,0)
                           text.color("#00ff00")
                           text.write("You Win!", font=("Cooper", 40, "bold"))

                       enhlth.clear()
                       enhlth.write(hlth*-1, font=("Cooper", 30, "italic"))
                       time.sleep(1)
                       enhlth.clear()
                       comments.clear()
                       
                   else :
                       if score>=5 :
                           score-=5
                           scorewriter.clear()
                           scorewriter.write(score, font=("Cooper", 20, "bold"))
                    
                   evade=0
                   firing=0
                   time.sleep(0.8)
                   boom.hideturtle()
                   comments.clear()
                   
     



    def spdplus():
        global spd
        if spd<11 :
            spd+=3
            




    def spdminus():
        global spd
        if spd>5:
            spd-=3








    turtle.listen()

    turtle.onscreenclick(get_mouse_click_coor)
    turtle.onkey(hit, "Up")
    turtle.onkey(right, "Right")
    turtle.onkey(left, "Left")



def EnemyControls() :
    def enemyhit():
        global rocketlife
        time.sleep(random.randint(5,15))
        enatk.speed(0)
        enatk.goto(g,200)
        
        eatk=random.randint(0,2)
        if eatk==0 or eatk==1 :
            
           enatk.showturtle()
           
           enatk.speed(1+difficulty//10)
           xcord=abscissa
           enboom.goto(xcord,-160)
           enatk.goto(xcord,-160)
           time.sleep(0.2)
           enboom.showturtle()
           
           enatk.hideturtle()
           
           if xcord in range (abscissa-10, abscissa+10) :
               rocketlife-=(difficulty//10*4+8)
               rokthealth.clear()
               rokthealth.goto(-450, -215)
               rokthealth.write("Health : ", font=("Cooper", 20, "bold"))
               rokthealth.goto(-375, -215)
               rokthealth.write(rocketlife, font=("Cooper", 20, "bold"))
               if rocketlife<=0 :
                   t.hideturtle()
                   turtle.clear()
                   print("You lose... Your final score was", score, "Points. At Level", bossnumber,".")
                   text.speed(0)
                   text.penup()
                   text.goto(-20,0)
                   text.color("red")
                   text.write("You Lose...", font=("Cooper", 40, "bold"))

           myhlth.clear()
           myhlth.write((difficulty//10*4+8)*(-1), font=("Cooper", 30, "italic"))
           time.sleep(1)
           myhlth.clear()
           time.sleep(0.5)
           enboom.hideturtle()



def Gaana() :
    gaanaloop=0
    while gaanaloop <1:
        if operatingsystem == 1 :
            import winsound
                                     #LOCATION            
            playsound("/Users/aksharadinkar/Downloads/GameMusic.mp3")
                                     #LOCATION            
            playsound("/Users/aksharadinkar/Downloads/Pacman.mp3")
                                     #LOCATION            
            playsound("/Users/aksharadinkar/Downloads/Digimon.mp3")
        if operatingsystem == 2 :
            import subprocess
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/GameMusic.mp3"])
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Pacman.mp3"])
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Digimon.mp3"])
        if operatingsystem == 3 :
            import subprocess
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/GameMusic.mp3"])
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Pacman.mp3"])
                                     #LOCATION
            subprocess.call(["afplay", "/Users/aksharadinkar/Downloads/Digimon.mp3"])            
    
p1=multiprocessing.Process(target=PlayerControls)
p2=multiprocessing.Process(target=EnemyControls)
p3=multiprocessing.Process(target=Gaana)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

turtle.done()

