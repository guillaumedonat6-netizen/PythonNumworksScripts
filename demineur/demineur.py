from time import *
from ion import *
from kandinsky import *
from random import *

L_Terrain=[]
LN_Terrain=[]
L_D_Terrain=[]
L_Bombs=[]
L_Sus=[]
TT=20
D=10
T=0

def Grille(D):
  global L_Bombs,L_D_Terrain,L_Terrain,LN_Terrain,TT
  
  for i in range(60,259,TT):
    for e in range(0,219,TT):
      L_Terrain.append((i,e))
  fill_rect(0,0,320,222,color(0,100,0))
  for i in L_Terrain:
    D_Tile(i[0],i[1])
  for i in range(D):
    C=choice(L_Terrain)
    L_Terrain.remove(C)
    L_Bombs.append(C)
  for i in L_Terrain:
    N=0
    x,y=i[0],i[1]
    for dx in range(0,3):
      for dy in range(0,3):
        if (x+TT*(dx-1),y+TT*(dy-1))in L_Bombs:
          N+=1
    LN_Terrain.append((x,y,N))
  for i in L_Terrain:
    x,y=i[0],i[1]
    for dx in range(0,3):
      for dy in range(0,3):
        if (x+TT*(dx-1),y+TT*(dy-1),0) in LN_Terrain:
          for E in range(9):
            if (x,y,E)in LN_Terrain:
                LN_Terrain.remove((x,y,E))
                L_D_Terrain.append((x,y,E))
                break
            
  for i in L_D_Terrain:
    D_Tile(i[0],i[1])
    
    
    
  
  L_Terrain=[]
  
def D_P(x,y):
  fill_rect(x,y,2,TT,"orange")
  fill_rect(x,y,TT,2,"orange")
  fill_rect(x,y+TT,TT,-2,"orange")
  fill_rect(x+TT,y,-2,TT,"orange")
  draw_string(str(" "),10,10)
  for i in range(9):
    if (x,y,i)in L_D_Terrain:
      draw_string(str(i),10,10)
  
def D_Tile(x,y):
  for i in range(9):
    if (x,y,i)in L_D_Terrain:
      C=color(160-16*i,60-6*i,40-4*i)
      fill_rect(x,y,TT,TT,C)
      return
  if (x,y)in L_Sus:
    fill_rect(x,y,TT,TT,color(0,150,0))
  else:
    fill_rect(x,y,TT,TT,color(0,255,0))


def Play():
  global T,V
  x,y=60,0
  D_P(x,y)
  while True:
    if keydown(KEY_UP) and y>0:
      D_Tile(x,y)
      y-=TT
      D_P(x,y)
    if keydown(KEY_DOWN) and y<220-TT:
      D_Tile(x,y)
      y+=TT
      D_P(x,y)
    if keydown(KEY_RIGHT)and x<260-TT:
      D_Tile(x,y)
      x+=TT
      D_P(x,y)
    if keydown(KEY_LEFT)and x>60:
      D_Tile(x,y)
      x-=TT
      D_P(x,y)
    if keydown(KEY_BACKSPACE)and not((x,y)in L_Sus):
      L_Sus.append((x,y))
      D_Tile(x,y)
      D_P(x,y)
      
    if keydown(KEY_OK):
      if ((x,y) in L_Bombs) and not((x,y)in L_Sus):
        for i in L_Bombs:
          if (i[0],i[1])in L_Sus:
            fill_rect(i[0],i[1],TT,TT,color(150,0,0))
          else:
            fill_rect(i[0],i[1],TT,TT,"red")
        sleep(1)
        while not keydown(KEY_OK):
          sleep(0.1)
        break
      elif not((x,y) in L_Sus):
        V=0
        F=False
        for i in range(9):
          if (x,y,i)in LN_Terrain:
            V=i
            F=True
            break
        if F:
          LN_Terrain.remove((x,y,V))
          L_D_Terrain.append((x,y,V))
          D_Tile(x,y)
          D_P(x,y)
      elif (x,y)in L_Sus:
        L_Sus.remove((x,y))
        D_Tile(x,y)
        D_P(x,y)
    if len(LN_Terrain)==0:
      for i in L_Bombs:
          if (i[0],i[1])in L_Sus:
            fill_rect(i[0],i[1],TT,TT,color(0,0,150))
          else:
            fill_rect(i[0],i[1],TT,TT,"blue")
      sleep(1)
      while not keydown(KEY_OK):
        sleep(0.1)
      V+=1
      break
    T+=0.1
    draw_string(str(T)[:4],270,10)
    sleep(0.1)

V=0
while True:
  L_Terrain=[]
  LN_Terrain=[]
  L_D_Terrain=[]
  L_Bombs=[]
  TT=20
  D=10
  T=0
  L_Sus=[]
  Grille(D)
  draw_string(str(V)[:4],10,190)
  Play()
