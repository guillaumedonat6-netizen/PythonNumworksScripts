from time import *
from ion import *
from kandinsky import *
from random import *

def DrA1(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")

def DrA2(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")

def DrA3(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")

def DrA4(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+30,10,10,"white")

def DrA5(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+30,10,10,"white")

def DrA6(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+30,10,10,"white")

def DrA7(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+50,10,10,"white")

def DrA8(x,y):
  fill_rect(70+60*x,21+60*y,60,60,"black")
  fill_rect(70+60*x+10,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+10,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+50,21+60*y+30,10,10,"white")
  fill_rect(70+60*x+10,21+60*y+50,10,10,"white")
  fill_rect(70+60*x+30,21+60*y+50,10,10,"white")

def DrawAll(L):
  fill_rect(70,21,60*3,60*3,color(255,255,255))
  DrA1(L[0][0],L[0][1])
  DrA2(L[1][0],L[1][1])
  DrA3(L[2][0],L[2][1])
  DrA4(L[3][0],L[3][1])
  DrA5(L[4][0],L[4][1])
  DrA6(L[5][0],L[5][1])
  DrA7(L[6][0],L[6][1])
  DrA8(L[7][0],L[7][1])

def DrawL(L,x,y):
  if (L.index([x,y]))==0:
    DrA1(x,y)
  if (L.index([x,y]))==1:
    DrA2(x,y)
  if (L.index([x,y]))==2:
    DrA3(x,y)
  if (L.index([x,y]))==3:
    DrA4(x,y)
  if (L.index([x,y]))==4:
    DrA5(x,y)
  if (L.index([x,y]))==5:
    DrA6(x,y)
  if (L.index([x,y]))==6:
    DrA7(x,y)
  if (L.index([x,y]))==7:
    DrA8(x,y)
  

def DrP(x,y):
  fill_rect(70+60*x,21+60*y,60,2,"red")
  fill_rect(70+60*x,21+60*y,2,60,"red")
  fill_rect(70+60*(x+1),21+60*y,-2,60,"red")
  fill_rect(70+60*x,21+60*(y+1),60,-2,"red")
  
def UDrP(x,y):
  fill_rect(70+60*x,21+60*y,60,2,"black")
  fill_rect(70+60*x,21+60*y,2,60,"black")
  fill_rect(70+60*(x+1),21+60*y,-2,60,"black")
  fill_rect(70+60*x,21+60*(y+1),60,-2,"black")

LDrA=[]
def Init():
  global LDrA
  fill_rect(0,0,320,222,"grey")
  LDrA=[]
  N=0
  XY=(0,0)
  while not(N==8):
    XY=[randint(0,2),randint(0,2)]
    if XY not in LDrA:
      LDrA.append(XY)
      N+=1
  DrawAll(LDrA)

def Move():
  x,y=0,0
  DrP(x,y)
  while True:
    if keydown(KEY_RIGHT) and x<2:
      UDrP(x,y)
      x+=1
      DrP(x,y)
    if keydown(KEY_LEFT) and x>0:
      UDrP(x,y)
      x-=1
      DrP(x,y)
    if keydown(KEY_DOWN) and y<2:
      UDrP(x,y)
      y+=1
      DrP(x,y)
    if keydown(KEY_UP) and y>0:
      UDrP(x,y)
      y-=1
      DrP(x,y)
    if keydown(KEY_OK) and ([x,y] in LDrA):
      if get_pixel(70+60*(x+1)+5,21+60*(y)+5)==color(255,255,255):
        fill_rect(70+60*x,21+60*y,60,60,"white")
        LDrA[LDrA.index([x,y])][0]+=1
        DrawL(LDrA,x+1,y)
        DrP(x,y)
      if get_pixel(70+60*(x-1)+5,21+60*(y)+5)==color(255,255,255):
        fill_rect(70+60*x,21+60*y,60,60,"white")
        LDrA[LDrA.index([x,y])][0]-=1
        DrawL(LDrA,x-1,y)
        DrP(x,y)
      if get_pixel(70+60*(x)+5,21+60*(y+1)+5)==color(255,255,255):
        fill_rect(70+60*x,21+60*y,60,60,"white")
        LDrA[LDrA.index([x,y])][1]+=1
        DrawL(LDrA,x,y+1)
        DrP(x,y)
      if get_pixel(70+60*(x)+5,21+60*(y-1)+5)==color(255,255,255):
        fill_rect(70+60*x,21+60*y,60,60,"white")
        LDrA[LDrA.index([x,y])][1]-=1
        DrawL(LDrA,x,y-1)
        DrP(x,y)

    sleep(0.1)

Init()
Move()
