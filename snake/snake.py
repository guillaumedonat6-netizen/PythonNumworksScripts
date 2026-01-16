from kandinsky import *
from ion import *
from time import *
from random import *

#Created by Boa's World
#version 1.3.7

y=110
x=160
x_p=0
y_p=0
L_pos=[(-10,-10),(-10,-10),(-10,-10),(-10,-10),(-10,-10)]
Mvt=""
Score=0
C_Mur=0
C_Pomme=0
L_Mur=[]
lat=0
Time=0
M_score=1
speed=1

def UnDraw():
  for i in L_pos:
    fill_rect(i[0],i[1],10,10,"white")
def Draw():
  x=1
  for i in L_pos:
    fill_rect(i[0],i[1],10,10,color(255,100+(2*x),0+(2*x)))
    x+=1    
def Check():
  global x,y,x_p,y_p,Score,C_Mur,M_score
  if (x,y) in L_Mur:
    return True
  elif (x,y) in L_pos:
    return True
  if len(L_pos)>=35:
    fill_rect(0,0,320,222,"black")
    for i in range(len(L_pos)-5):
      L_pos.pop()
      Draw()
      fill_rect(x,y,10,10,"red")
      sleep(0.05)
      fill_rect(0,0,320,222,"black")
      fill_rect(x,y,10,10,"red")
      sleep(0.05)
    fill_rect(0,0,320,222,"white")
    fill_rect(x_p,y_p,10,10,color(0,200,0))
    Mur()
    Mur()
    C_Mur+=2
    Score+=10*M_score
  if (Time/30)>3:
    Score+=150
    M_score+=1
  elif (Time/30)>1:
    Score+=50
    M_score+=1
  return False 
def P_Check():
  global x_p,y_p,L_pos,x,y,Score,C_Pomme
  if get_pixel(x+5,y+5)==color(0,200,0):
    fill_rect(x_p,y_p,10,10,"white")
    L_pos=[(x,y)]+L_pos
    Score+=2*M_score
    C_Pomme+=1
    Pomme()  
def Pomme():
  global x_p,y_p,L_Mur,L_pos
  x_p=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300])
  y_p=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
  while ((x_p,y_p)in L_Mur) or((x_p,y_p) in L_pos):
    x_p=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300])
    y_p=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
  fill_rect(x_p,y_p,10,10,color(0,200,0))
def Mur():
  global L_Mur,x,y,L_pos
  L=[(x,y),(x+10,y+10),(x+10,y),(x+10,y),(x-10,y-10),(x-10,y),(x,y-10)]
  xx=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300])
  yy=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
  while ((xx,yy) in L)or((xx,yy) in L_Mur) or ((xx,yy) in L_pos):
    xx=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300])
    yy=choice([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
  L_Mur.append((xx,yy))
  for i in L_Mur:
    fill_rect(i[0],i[1],10,10,"grey")

def Game():
  global x,y,x_p,y_p,L_pos,Mvt,Score,C_Mur,C_Pomme,L_Mur,lat,Time,M_score,speed
  Pomme()
  Draw()
  
  while True:
    if keydown(KEY_UP) or Mvt=="Up":
      Mvt="Up"
      UnDraw()
      L_pos.pop()
      y-=int(10)
      if y<0:
        break
      if Check():
        break
      L_pos=[(x,y)]+L_pos
      P_Check()
      Draw()
      fill_rect(x,y,10,10,"red")
    if keydown(KEY_DOWN) or Mvt=="Down":
      Mvt="Down"
      UnDraw()
      L_pos.pop()
      y+=int(10)
      if y>210:
        break
      if Check():
        break
      L_pos=[(x,y)]+L_pos
      P_Check()
      Draw()
      fill_rect(x,y,10,10,"red")
    if keydown(KEY_LEFT) or Mvt=="Left":
      Mvt="Left"
      UnDraw()
      L_pos.pop()
      x-=int(10)
      if x<0:
        break
      if Check():
        break
      L_pos=[(x,y)]+L_pos
      P_Check()
      Draw()
      fill_rect(x,y,10,10,"red")
    if keydown(KEY_RIGHT) or Mvt=="Right":
      Mvt="Right"
      UnDraw()
      L_pos.pop()
      x+=int(10)
      if x>310:
        break
      if Check():
        break
      L_pos=[(x,y)]+L_pos
      P_Check()
      Draw()
      fill_rect(x,y,10,10,"red")
    if keydown(KEY_EXP):
      Score+=1
      L_pos=[(x,y)]+L_pos
    sleep((0.1+lat)/speed)
    Time+=(0.1+lat)/speed
  Draw()
  for i in range(10):
    fill_rect(0,0,320,222,color(255-i*10,255-i*10,255-i*10))
    sleep(0.5/10)
  fill_rect(0,0,320,222,"grey")
  draw_string("Score : "+str(Score),100,90)
  draw_string("Pomme : "+str(C_Pomme),100,110)
  draw_string("Mur : "+str(C_Mur),100,130)

fill_rect(0,0,320,222,"grey")
Cursor = 1
NCursor = 1
fill_rect(100,90,10,10,"white")
draw_string("Game",120,90)
draw_string("Option",120,110)
while True:
  sleep(0.1)
  if keydown(KEY_UP) and Cursor>1:
    Cursor -= 1
  elif keydown(KEY_DOWN) and Cursor<2:
    Cursor += 1
  if Cursor==1:
    fill_rect(100,90,10,10,"white")
    fill_rect(100,110,10,10,"grey")
  elif Cursor==2:
    fill_rect(100,90,10,10,"grey")
    fill_rect(100,110,10,10,"white")
  if keydown(KEY_OK):
    if Cursor == 1:
      fill_rect(0,0,320,222,"white")
      Game()
      fill_rect(0,0,320,222,"grey")
      Cursor = 1
      NCursor = 1
      fill_rect(100,90,10,10,"white")
      draw_string("Game",120,90)
      draw_string("Option",120,110)
    else :
      fill_rect(0,0,320,222,"grey")
      draw_string("What do you want to change",40,70)
      draw_string("Latency",120,90)
      draw_string("Speed",120,110)
      draw_string("Back",120,130)
      fill_rect(100,90,10,10,"white")
      sleep(0.1)
      while not(keydown(KEY_OK)):
        if keydown(KEY_DOWN) and NCursor<3 :
          NCursor+=1
        elif keydown(KEY_UP) and NCursor>1:
          NCursor-=1
        if NCursor==1:
          fill_rect(100,90,10,10,"white")
          fill_rect(100,110,10,10,"grey")
          fill_rect(100,130,10,10,"grey")
        elif NCursor==2:
          fill_rect(100,90,10,10,"grey")
          fill_rect(100,110,10,10,"white")
          fill_rect(100,130,10,10,"grey")
        elif NCursor==3:
          fill_rect(100,90,10,10,"grey")
          fill_rect(100,110,10,10,"grey")
          fill_rect(100,130,10,10,"white")
        sleep(0.1)
      if NCursor==1:
        lat=int(input("Give new latency : "))
        fill_rect(0,0,320,222,"grey")
        draw_string("Game",120,90)
        draw_string("Option",120,110)
        sleep(0.1)
      elif NCursor==2:
        speed=int(input("Give new speed : "))
        fill_rect(0,0,320,222,"grey")
        draw_string("Game",120,90)
        draw_string("Option",120,110)
        sleep(0.1)
      elif NCursor==3:
        Cursor=1
        fill_rect(0,0,320,222,"grey")
        draw_string("Game",120,90)
        draw_string("Option",120,110)
        sleep(0.1)
