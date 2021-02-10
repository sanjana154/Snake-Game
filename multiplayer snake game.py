#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import turtle as t
c1=t.Turtle()
c1.shape('square')
c1.color('red')
c1.speed(0)
c1.penup()
c1.hideturtle()

c2=t.Turtle()
c2.shape('square')
c2.color('blue')
c2.setheading(180)
c2.speed(0)
c2.penup()
c2.hideturtle()

leaf=t.Turtle()
leaf_shape=((0,0), (14,2), (18,6), (20,20), (6,18), (2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.speed(0)
leaf.penup()
leaf.hideturtle()

text=t.Turtle()
text.write('Press space to start',align='center',font=('Arial',16,'bold'))
text.hideturtle()

score=t.Turtle()
score.speed(0)
score.hideturtle()

game=False

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = c1.pos()
    (x2,y2) = c2.pos()
    outside =         x<left_wall or x2<left_wall or         x>right_wall or x2>right_wall or         y>top_wall or y2>top_wall or         y<bottom_wall or y2<bottom_wall
    return outside

def game_over():
    c1.color('yellow')
    c2.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("GAME OVER!", align='center',font=('Arial',30,'normal'))

def display_score(current_score):
    score.clear()
    score.penup()
    x = (t.window_width()/2)-50
    y = (t.window_height()/2)-50
    score.setpos(x,y)
    score.write(str(current_score), align='right',font=('Arial',30, 'bold'))


def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    leaf.showturtle()

def start():
    global game
    if game:
        return
    game=True
    score=0
    text.clear()
    
    c1speed=1
    c2speed=1
    len=3
    len2=3
    c1.shapesize(1,len,1)
    c2.shapesize(1,len2,1)
    c1.showturtle()
    c2.showturtle()
    display_score(score)
    place_leaf()
    
    while True:
        c1.forward(c1speed)
        c2.forward(c2speed)
        if c1.distance(leaf)<20:
            place_leaf()
            len = len+1
            c1.shapesize(1,len,1)
            c1speed = c1speed+1
            score=score+10
            display_score(score)
        if leaf.distance(c2)<20:
            place_leaf()
            len2 = len2+1
            c2.shapesize(1,len2,1)
            c2speed = c2speed+1
            score=score+10
            display_score(score)
        if outside_window():
            game_over()
            break
        
           
    
    
    

def up():
    if c1.heading()==0 or c1.heading()==180:
        c1.setheading(90)
def up2():
    if c2.heading()==0 or c2.heading()==180:
        c2.setheading(90)
def down():
    if c1.heading()==0 or c1.heading()==180:
        c1.setheading(270)
def down2():
    if c2.heading()==0 or c2.heading()==180:
        c2.setheading(270)
def left():
    if c1.heading()==90 or c1.heading()==270:
        c1.setheading(180)
def left2():
    if c2.heading()==90 or c2.heading()==270:
        c2.setheading(180)
def right():
    if c1.heading()==90 or c1.heading()==270:
        c1.setheading(0)
def right2():
    if c2.heading()==90 or c2.heading()==270:
        c2.setheading(0)

t.bgcolor('yellow')
t.onkey(start,'space')
t.onkey(up,'Up')
t.onkey(down,'Down')
t.onkey(left,'Left')
t.onkey(right,'Right')
t.onkey(up2,'w')
t.onkey(down2,'s')
t.onkey(left2,'a')
t.onkey(right2,'d')
t.listen()
t.mainloop()


# In[ ]:





# In[ ]:




