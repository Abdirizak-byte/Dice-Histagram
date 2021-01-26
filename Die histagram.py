import random
from graphics import *

def roller():
    rollone = random.randrange(1,7)
    rolltwo = random.randrange(1,7)
    totalroll = rollone + rolltwo
    return totalroll

rolls = []
for i in range(1000):
    rolls.append(roller())

bins = []
for b in range(11):
    bins.append(0)

for n in rolls:
    for y in range(11):
        if n == y + 2:
            bins[y] += 1
            
win = GraphWin("Rollin", 500,500)
win.setCoords(-15,-15,100,100)

xaxis = Line(Point(10,0), Point(100,0))
xaxis.draw(win)
yaxis = Line(Point(10,0), Point(10,100))
yaxis.draw(win)

Text(Point(-5, 55), "Freq").draw(win)
for i in range(11):
    Text(Point(5,i*10), i*25).draw(win)

Text(Point(55, -10), "Dice Roll").draw(win)
for i in range(2,13):
    Text(Point(i*10,-5), i).draw(win)
    
for i in range(2,13):
    bar = Rectangle(Point(8*i-4,0),Point(4+8*i,bins[i-2]/2.5))
    bar.setFill("Brown")
    bar.draw(win)
print(bins)

win.getMouse()
win.close()
roller()
