from time import *
from ion import *
from kandinsky import *
from math import *
from random import *

L=[[0,0,0],[0,0,0],[0,0,0]]
vic=True
Bot=False
Score=[0,0]

def Grille():
  fill_rect(0,0,320,220,"white")
  for X in range(55,320-55,70):
    fill_rect(X,5,2,210,"black")
  fill_rect(320-55,5,2,210,"black")
  for Y in range(5,215,70):
    fill_rect(55,Y,210,2,"black")
  fill_rect(55,215,212,2,"black")    

def Croix(x,y,C):
  for X in range(66):
    for Y in range(66):
      if X==Y or (66-X)==Y:
        fill_rect(x+X+2,y+Y+2,3,3,C)

def Rond(x,y,C):
  for X in range(66):
    for Y in range(66):
      if int(sqrt((X-32)**2+(Y-32)**2))==32:
        fill_rect(x+X+2,y+Y+2,3,3,C)

def Draw(x,y,C):
  if L[x][y]==1:
    Croix(55+70*x,5+70*y,C)
  if L[x][y]==2:
    Rond(55+70*x,5+70*y,C)

def Check(P2):
  global L
  C0=0
  for X in range(3):
    if L[X][0]==L[X][1]==L[X][2] and not(L[X][0]==0):
      if P2:
        for y in range(3):
          Draw(X,y,"green")
      return str(L[X][0])
  for Y in range(3):
    if L[0][Y]==L[1][Y]==L[2][Y] and not(L[0][Y]==0):
      if P2:
        for x in range(3):
          Draw(x,Y,"green")
      return str(L[0][Y])
  if L[0][0]==L[1][1]==L[2][2] and not(L[0][0]==0):
    if P2:
      for I in range(3):
        Draw(I,I,"green")
    return str(L[0][0])
  if L[0][2]==L[1][1]==L[2][0] and not(L[0][0]==0):
    if P2:
      for I in range(3):
        Draw(I,2-I,"green")
    return str(L[0][2])
  for X in range(3):
    for Y in range(3):
      if L[X][Y]==0:
        C0+=1
  if C0==0:
    return "tie"
  else:
    return ""    

def Play(P):
  global L
  x,y=0,0
  if P==1:
    Croix(55+x*70,5+y*70,"red")
  else:
    Rond(55+x*70,5+y*70,"red")
  while True:
    if keydown(KEY_DOWN) and y<2:
      fill_rect(55+x*70+2,5+y*70+2,68,68,"white")
      if not L[x][y]==0:
        Draw(x,y,"black")
      y+=1
      if P==1:
        Croix(55+x*70,5+y*70,"red")
      else:
        Rond(55+x*70,5+y*70,"red")
    if keydown(KEY_UP) and y>0:
      fill_rect(55+x*70+2,5+y*70+2,68,68,"white")
      if not L[x][y]==0:
        Draw(x,y,"black")
      y-=1
      if P==1:
        Croix(55+x*70,5+y*70,"red")
      else:
        Rond(55+x*70,5+y*70,"red")
    if keydown(KEY_RIGHT) and x<2:
      fill_rect(55+x*70+2,5+y*70+2,68,68,"white")
      if not L[x][y]==0:
        Draw(x,y,"black")
      x+=1
      if P==1:
        Croix(55+x*70,5+y*70,"red")
      else:
        Rond(55+x*70,5+y*70,"red")
    if keydown(KEY_LEFT) and x>0:
      fill_rect(55+x*70+2,5+y*70+2,68,68,"white")
      if not L[x][y]==0:
        Draw(x,y,"black")
      x-=1
      if P==1:
        Croix(55+x*70,5+y*70,"red")
      else:
        Rond(55+x*70,5+y*70,"red")
    if keydown(KEY_OK) and L[x][y]==0:
      L[x][y]=P
      fill_rect(55+x*70+2,5+y*70+2,68,68,"white")
      Draw(x,y,"black")
      break
    sleep(0.1)

def Victory(P):
  global vic
  if P=="1":
    sleep(1)
    fill_rect(0,0,320,222,"white")
    Score[0]+=1
    draw_string("Player 1 win "+str(Score),50,110)
    vic=False
  if P=="2":
    sleep(1)
    fill_rect(0,0,320,222,"white")
    Score[1]+=1
    draw_string("Player 2 win "+str(Score),50,110)
    vic=False
  if P=="tie":
    sleep(1)
    fill_rect(0,0,320,222,"white")
    draw_string("Tie",100,110)
    vic=False
  
def Game(P2,Bdif):
  global vic,L,n_Tour
  Grille()
  vic=True
  while vic:
    Play(1)
    Victory(Check(True))
    if not vic:
      break
    if P2:
      Play(2)
    else:
      IA(Bdif)
      print(L)
    Victory(Check(True))
    n_Tour+=1
  sleep(2)

def IA(E):
  global L
  End=False
  if randint(0,10)>E:
    L0=[]
    for X in range(3):
      for Y in range(3):
        if L[X][Y]==0:
          L0.append((X,Y))
    XY=choice(L0)
    L[XY[0]][XY[1]]=2
    Draw(XY[0],XY[1],"black")
    print("random ia",XY[0],XY[1])
    End=True
  else:
    for X in range(3):
      for Y in range(3):
        if L[X][Y]==0:
          L[X][Y]=2
          if Check(False)=="2":
            L[X][Y]=2
            Draw(X,Y,"black")
            End=True
            print("play win")
            break
          L[X][Y]=0
      if End:
        break
    if not End:
      for X in range(3):
        for Y in range(3):
          if L[X][Y]==0:
            L[X][Y]=1
            if Check(False)=="1":
              L[X][Y]=2
              Draw(X,Y,"black")
              End=True
              print("play def",X,Y)
              break
            L[X][Y]=0
        if End:
          break
  if not End:
    L0=[]
    for X in range(3):
      for Y in range(3):
        if L[X][Y]==0:
          L0.append((X,Y))
    if (L[0][0]==1 or L[0][2]==1 or L[2][2]==1 or L[2][0]==1) and (L[0][0]==1 or L[0][2]==1 or L[2][2]==1 or L[2][0]==1) and n_Tour<2:
        if L[0][0]==1 and not(L[2][2]==2):
          print("diag",2,2)
          L[2][2]=2
          Draw(2,2,"black")
          return
        elif L[0][2]==1 and not(L[2][0]==2):
          print("diag",2,0)
          L[2][0]=2
          Draw(2,0,"black")
          return
        elif L[2][0]==1 and not(L[0][2]==2):
          print("diag",0,2)
          L[0][2]=2
          Draw(0,2,"black")
          return
        elif L[2][2]==1 and not(L[0][0]==2):
          print("diag",0,0)
          L[0][0]=2
          Draw(0,0,"black")
          return 
    if L[1][1]==1 and (L[0][0]==0 or L[0][2]==0 or L[2][0]==0 or L[2][2]==0) and n_Tour<2:
      LXY=[]
      for i in [(0,0),(0,2),(2,0),(2,2)]:
        if L[i[0]][i[1]]==0:
          LXY.append(i)      
      XY=choice(LXY)
      print("side",XY[0],XY[1])
      L[XY[0]][XY[1]]=2
      Draw(XY[0],XY[1],"black")
      return 
    if (L[1][1]==0 or L[0][1]==0 or L[1][0]==0 or L[1][2]==0 or L[2][1]==0)and (L[0][1]==1 or L[1][0]==1 or L[1][2]==1 or L[2][1]==1) and n_Tour<2:
      if L[1][1]==0:
        print("middle",1,1)
        L[1][1]=2
        Draw(1,1,"black")
        return 
      else:
        LXY=[]
        for i in [(0,1),(1,0),(1,2),(2,1)]:
          if L[i[0]][i[1]]==0:
            LXY.append(i)      
        XY=choice(LXY)
        print("middle",XY[0],XY[1])
        L[XY[0]][XY[1]]=2
        Draw(XY[0],XY[1],"black")  
        return 
    XY=choice(L0)
    L[XY[0]][XY[1]]=2
    Draw(XY[0],XY[1],"black")
    print("random choice ",XY[0],XY[1])
    
R=input("Play against AI (y/n) :")
BotDif=""
n_Tour=0
if R=="y":
  Bot=False
  BotDif=int(input("Give a level (0-10):"))
else:
  Bot=True
while True:
  Game(Bot,BotDif)
  fill_rect(0,0,320,222,"black")  
  L=[[0,0,0],[0,0,0],[0,0,0]]
  n_Tour=0
  print("<======>")
