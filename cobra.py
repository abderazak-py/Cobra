import turtle 
import random
from freegames import square.vector

apple=vector(0,0)
cobra=[vector(10,0)]
aim=vector(0,-10)

def change(z,y):
  aim.x=x
  aim.y=y

def inside(head):
  return -200 < head.x < 190 and -200 < head.y < 190

def move():
  head=cobra[-1].copy()
  head.mmove(aim))
  
if not inside(head) or head in cobra:
  square(head.x,head.y,9,'red')
  return 
  
cobra.append()

if head==cobra:
  print('cobra',len(cobra))
  food.x=randrange(-15,15)*10
  food.y=randrange(-15,15)*10
  
else:
  cobra pop(0)
  
clear()

for body in cobra:
  square(body.x,body.y,9,'green')


square(food.x,food.y,9,'red')
update()
ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')

move()
done()