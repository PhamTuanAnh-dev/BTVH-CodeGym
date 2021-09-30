from turtle import *

t = Turtle()


t.speed(2)

t.up()
t.goto(-300,-250)
t.down()
#=============================  ve hcn
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

#=============================  ve cua ra vao
t.up()
t.goto(-265,-250)
t.down()

t.fillcolor("lime")
t.begin_fill()
for i in range(2):
    t.fd(30)
    t.lt(90)
    t.fd(60)
    t.lt(90)
t.end_fill()

#============================== ve tuong
t.up()
t.goto(-200,-250)
t.down()

t.fillcolor("green")
t.begin_fill()
t.lt(30) 
for i in range(2):
    t.fd(100) 
    t.lt(60) 
    t.fd(150) 
    t.lt(120) 
t.end_fill()
#============================= ve cua so 
t.up()
t.goto(-170,-180)
t.down()

t.fillcolor("pink")
t.begin_fill()
 
for i in range(2):
    t.fd(30) 
    t.lt(60) 
    t.fd(50) 
    t.lt(120) 
t.end_fill()

#============================== ve mai nha 1
t.up()
t.goto(-300,-100)
t.down()

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.fd(60)
    t.rt(61)
t.end_fill()

#============================= ve mai nha 2 
t.up()
t.goto(-248,-70)
t.down()

t.fillcolor("orange")
t.begin_fill()
t.lt(122)
for i in range(2):
    t.fd(100)
    t.rt(60) 
    t.fd(60) 
    t.rt(120) 
t.end_fill()

#============================= ve mat troi 
t.up()
t.goto(200,150)
t.down()

t.fillcolor("yellow")
t.begin_fill()
t.circle(35)
t.end_fill()


#=============================  ve than cay
t.up()
t.goto(150,-250)
t.down() 

t.fillcolor("brown")
t.begin_fill()
t.rt(30)
for i in range(2):
    t.fd(30)
    t.lt(90)
    t.fd(80)
    t.lt(90)
t.end_fill()

#============================= ve la cay
t.up()
t.goto(215,-150)
t.down()  

t.fillcolor("lime")
t.begin_fill()
for i in range(3):
    t.lt(120)
    t.fd(100)
t.end_fill()

t.up()
t.goto(215,-62)
t.down()  

t.fillcolor("lime")
t.begin_fill()
for i in range(3):
    t.lt(120)
    t.fd(100)
t.end_fill()