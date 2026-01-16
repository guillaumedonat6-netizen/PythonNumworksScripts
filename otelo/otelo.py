from kandinsky import *
from time import *
from ion import *

def Grille():
  for i in range(50,271,22):
    fill_rect(i,0,1,220,(0,75,0))
  for i in range(0,222,22):
    fill_rect(50,i,220,1,(0,75,0))

def Vic():
  R,J=0,0
  for i in range(50,271,22):
    for e in range(0,222,22):
      if get_pixel(i+10,e+10)==(0,0,0):
        R+=1
      if get_pixel(i+10,e+10)==(255,255,255):
        J+=1
  if R<J:
    draw_string("White win : "+str(J)+">"+str(R),100,100)
  elif R>J:
    draw_string("Black win : "+str(R)+">"+str(J),100,100)
  elif R==J:
    draw_string("Tie : "+str(R)+"="+str(J),100,100)
  
  
def D_P_Chooser(x,y):
  fill_rect(x+1,y+1,21,2,"orange")
  fill_rect(x+1,y+1,2,21,"orange")
  fill_rect(x+1,y+20,21,2,"orange")
  fill_rect(x+20,y+1,2,21,"orange")
  
def Cell_R_Draw(x,y):
  C=get_pixel(x+10,y+10)
  fill_rect(x+1,y+1,21,21,C)
def Cell_Draw(x,y,C):
  fill_rect(x+1,y+1,21,21,C)

def Change_C(x,y,C):
  X,Y=x,y
  L_R_D_TT=[]
  L_Temp=[] 
  C_read = None
  while not(C_read==C):
    X+=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break  
    L_Temp.append((X,Y))
    if X>=270:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[] 
  C_read = None
  X=x
  while not(C_read==C):
    X-=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if X<=50:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  X=x
  Y=y
  while not(C_read==C):
    Y-=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y<=0:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  Y=y
  while not(C_read==C):
    Y+=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y>=220:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  X=x
  Y=y
  while not(C_read==C):
    Y-=22
    X-=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y<=0:
      L_Temp=[]
      break
    if X<=50:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  X=x
  Y=y
  while not(C_read==C):
    Y+=22
    X-=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y>=220:
      L_Temp=[]
      break
    if X<=50:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  X=x
  Y=y
  while not(C_read==C):
    Y+=22
    X+=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y>=220:
      L_Temp=[]
      break
    if X>=270:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  C_read=None
  X=x
  Y=y
  while not(C_read==C):
    Y-=22
    X+=22
    C_read=get_pixel(X+10,Y+10)
    if C_read==(0,203,0):
      L_Temp=[]
      break
    L_Temp.append((X,Y))
    if Y<=0:
      L_Temp=[]
      break
    if X>=270:
      L_Temp=[]
      break
  L_R_D_TT.append(L_Temp)
  L_Temp=[]
  for i in L_R_D_TT:
    for e in i:
      Cell_Draw(e[0],e[1],C)

def Game():
  fill_rect(0,0,320,222,(200,200,200))
  fill_rect(50,0,220,220,(00,200,00))
  draw_string("P1",10,10)
  xp,yp=50,0
  Max_p=96
  T_p1=True
  Grille()
  Cell_Draw(50+22*5,0+22*5,(0,0,0))
  Cell_Draw(50+22*4,0+22*4,(0,0,0))
  Cell_Draw(50+22*4,0+22*5,(255,255,255))
  Cell_Draw(50+22*5,0+22*4,(255,255,255))
  D_P_Chooser(xp,yp)
  while True:
    if Max_p<=0:
      break
    if keydown(KEY_RIGHT) and xp<248:
      Cell_R_Draw(xp,yp)
      xp+=22
      D_P_Chooser(xp,yp)
    if keydown(KEY_LEFT) and xp>50:
      Cell_R_Draw(xp,yp)
      xp-=22
      D_P_Chooser(xp,yp)
    if keydown(KEY_DOWN) and yp<198:
      Cell_R_Draw(xp,yp)
      yp+=22
      D_P_Chooser(xp,yp)
    if keydown(KEY_UP) and yp>0:
      Cell_R_Draw(xp,yp)
      yp-=22
      D_P_Chooser(xp,yp)
    if keydown(KEY_OK) and (get_pixel(xp+10,yp+10))==(0,203,0):
      Max_p-=1
      if T_p1:
        Cell_Draw(xp,yp,(0,0,0))
        D_P_Chooser(xp,yp)
        T_p1=not T_p1
        Change_C(xp,yp,(0,0,0))
        draw_string("P1",10,10)
      else:
        Cell_Draw(xp,yp,(255,255,255))
        D_P_Chooser(xp,yp)
        T_p1=not T_p1
        Change_C(xp,yp,(255,255,255))
        draw_string("P2",10,10)
      sleep(0.1)
    sleep(0.1)
  Vic()


Game()
