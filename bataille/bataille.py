from ion import *
from kandinsky import *
from time import *

LBP1,LTP1,LBP2,LTP2,SP1,SP2,W,B,C,Sur=[],[],[],[],0,0,0,16,0,False
Colors=[("orange","red","green"),("orange","pink","purple"),("grey","blue","green")]

def Board():
  for i in range(49,270,20):
    fill_rect(i,0,2,222,"black")
  for i in range(0,230,20):
    fill_rect(49,i,222,2,"black")
def Format_3(S):
  for i in range(3):
    if not(len(S)>=3):
      S="0"+S
  return S
def Draw_B(L):
  for i in L:
    fill_rect(i[0]*20+51,i[1]*20+2,18,18,Colors[C][2])
def UnDraw_B(L):
  for i in L:
    fill_rect(i[0]*20+51,i[1]*20+2,18,18,"white")
def Draw_T(T,B):
  for i in T:
    if i in B:
      fill_rect(i[0]*20+51,i[1]*20+2,18,18,Colors[C][2])
    else:
      fill_rect(i[0]*20+51,i[1]*20+2,18,18,Colors[C][1])


def Place_B(L):
  global B
  fill_rect(0,0,320,222,color(100,100,255))
  fill_rect(50,0,220,222,"white")
  Board()
  xb,yb=0,0
  fill_rect(xb+51,yb+2,18,18,Colors[C][0])
  draw_string(Format_3(str(B-len(L))),10,10)
  while not(len(L)==B):
    if keydown(KEY_OK) and (not(xb,yb)in L):
      L.append((xb,yb))
      Draw_B(L)
      draw_string(Format_3(str(B-len(L))),10,10)
    if keydown(KEY_RIGHT) and xb<10:
      fill_rect(xb*20+51,yb*20+2,18,18,"white")
      xb+=1
      Draw_B(L)
      fill_rect(xb*20+51,yb*20+2,18,18,Colors[C][0])
    if keydown(KEY_LEFT) and xb>0:
      fill_rect(xb*20+51,yb*20+2,18,18,"white")
      xb-=1
      Draw_B(L)
      fill_rect(xb*20+51,yb*20+2,18,18,Colors[C][0])
    if keydown(KEY_UP) and yb>0:
      fill_rect(xb*20+51,yb*20+2,18,18,"white")
      yb-=1
      Draw_B(L)
      fill_rect(xb*20+51,yb*20+2,18,18,Colors[C][0])
    if keydown(KEY_DOWN) and yb<10:
      fill_rect(xb*20+51,yb*20+2,18,18,"white")
      yb+=1
      Draw_B(L)
      fill_rect(xb*20+51,yb*20+2,18,18,Colors[C][0])
    sleep(0.1)
  fill_rect(xb*20+51,yb*20+2,18,18,"white")
  for i in range(5):
    Draw_B(L)
    sleep(0.05)
    UnDraw_B(L)
    sleep(0.05)

def Tir_B(L,B,S):
  fill_rect(0,0,320,222,color(50,50,255))
  fill_rect(50,0,220,222,"white")
  Board()
  Draw_T(L,B)
  xt,yt=0,0
  fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][0])
  draw_string(Format_3(str(16-S)),10,10)
  while True:
    if keydown(KEY_OK) and not((xt,yt)in L):
      L.append((xt,yt))
      if ((xt,yt) in B) and not(Check(L,B)):
        S+=1
        for i in range(5):
          fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][2])
          sleep(0.05)
          fill_rect(xt*20+51,yt*20+2,18,18,"white")
          sleep(0.05)
        Draw_T(L,B)
        draw_string(Format_3(str(16-S)),10,10)
        continue
      else:
        for i in range(5):
          fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][1])
          sleep(0.05)
          fill_rect(xt*20+51,yt*20+2,18,18,"white")
          sleep(0.05)
        break
    if keydown(KEY_RIGHT) and xt<10:
      fill_rect(xt*20+51,yt*20+2,18,18,"white")
      xt+=1
      Draw_T(L,B)
      fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][0])
    if keydown(KEY_LEFT) and xt>0:
      fill_rect(xt*20+51,yt*20+2,18,18,"white")
      xt-=1
      Draw_T(L,B)
      fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][0])
    if keydown(KEY_UP) and yt>0:
      fill_rect(xt*20+51,yt*20+2,18,18,"white")
      yt-=1
      Draw_T(L,B)
      fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][0])
    if keydown(KEY_DOWN) and yt<10:
      fill_rect(xt*20+51,yt*20+2,18,18,"white")
      yt+=1
      Draw_T(L,B)
      fill_rect(xt*20+51,yt*20+2,18,18,Colors[C][0])
    sleep(0.1)
  return S

def Check(T,B):
  for i in B:
    if not(i in T):
      return False
  return True

def Win(W,S1,S2):
  global B
  if W==1 and Sur:
    S1+=2
  elif W==2 and Sur:
    S2+=2
  fill_rect(0,0,320,222,"black")
  draw_string("Player "+str(W)+" Win",95,20)
  fill_rect(119,191,22,-82,"grey")
  fill_rect(120,190,20,-80,"white")
  fill_rect(120,190,20,-int((80/B)*S1),Colors[C][2])
  fill_rect(179,191,22,-82,"grey")
  fill_rect(180,190,20,-80,"white")
  fill_rect(180,190,20,-int((80/B)*S2),Colors[C][1])
  draw_string("Score P1 :",10,60)
  draw_string(Format_3(str(S1)),40,80)  
  draw_string("Score P2 :",210,60)
  draw_string(Format_3(str(S2)),240,80)  
  
  while not keydown(KEY_OK):
    fill_rect(120,79,80,20,"black")
    draw_string("Press Ok",120,200)
    if W==1:
      Couronne(120,80)
    else:
      Couronne(180,80)
    sleep(0.2)
    fill_rect(120,80,80,20,"black")
    if W==1:
      Couronne(120,79)
    else:
      Couronne(180,79)
    sleep(0.2)
    fill_rect(120,79,80,20,"black")
    fill_rect(120,200,80,20,"black")
    if W==1:
      Couronne(120,78)
    else:
      Couronne(180,78)
    sleep(0.2)
    fill_rect(120,78,80,20,"black")
    if W==1:
      Couronne(120,77)
    else:
      Couronne(180,77)
    sleep(0.2)
    fill_rect(120,77,80,20,"black")
    draw_string("Press Ok",120,200)
    if W==1:
      Couronne(120,78)
    else:
      Couronne(180,78)
    sleep(0.2)
    fill_rect(120,78,80,20,"black")
    if W==1:
      Couronne(120,79)
    else:
      Couronne(180,79)
    sleep(0.2)
  Menu()
    

def Couronne(x,y):
  fill_rect(x,y,20,20,"yellow")
  fill_rect(x,y,9,2,"black")
  fill_rect(x+2,y+2,6,4,"black")
  fill_rect(x+4,y+6,2,2,"black")
  fill_rect(x+20,y,-9,2,"black")
  fill_rect(x+18,y+2,-6,4,"black")
  fill_rect(x+16,y+6,-2,2,"black")
  fill_rect(x,y+20,2,-4,"black")
  fill_rect(x+18,y+20,2,-4,"black")
  fill_rect(x,y+20,6,-2,"black")
  fill_rect(x+20,y+20,-6,-2,"black")


def Init():
  global LBP1,LBP2,LTP1,LTP2,SP1,SP2,W,B,Sur
  LBP1,LBP2,LTP1,LTP2,SP1,SP2,W,Sur=[],[],[],[],0,0,0,False
  for i in range(0,200):
    fill_rect(160-i,0,2*i,2*i,"black")
  draw_string("Player 1",120,110)
  while not keydown(KEY_OK):
    pass
  for i in range(1,255,2):
    fill_rect(0,0,320,222,color(int(i/100),int(i/100),i))
  Place_B(LBP1)
  for i in range(0,200):
    fill_rect(160-i,0,2*i,2*i,"black")
  draw_string("Player 2",120,110)
  while not keydown(KEY_OK):
    pass
  for i in range(1,255,2):
    fill_rect(0,0,320,222,color(int(i/100),int(i/100),i))
  Place_B(LBP2)
  for i in range(0,200):
    fill_rect(160-i,0,2*i,2*i,"black")
  while True:
    for i in range(0,200):
      fill_rect(160-i,0,2*i,2*i,"black")
    draw_string("Player 1",120,110)
    while not keydown(KEY_OK):
      if keydown(KEY_BACKSPACE):
        Sur=True
        Win(1,SP1,SP2)
    for i in range(1,255,2):
      fill_rect(0,0,320,222,color(int(i/100),int(i/100),i))
    SP1=Tir_B(LTP1,LBP2,SP1)
    if Check(LTP1,LBP2):
      W=1
      break
    for i in range(0,200):
      fill_rect(160-i,0,2*i,2*i,"black")
    draw_string("Player 2",120,110)
    while not keydown(KEY_OK):
      if keydown(KEY_BACKSPACE):
        Sur=True
        Win(2,SP1,SP2)
    for i in range(1,255,2):
      fill_rect(0,0,320,222,color(int(i/100),int(i/100),i))
    SP2=Tir_B(LTP2,LBP1,SP2)
    if Check(LTP2,LBP1):
      W=2
      break
  for i in range(0,200):
    fill_rect(160-i,0,2*i,2*i,"black")
  Win(W,SP1,SP2)
  
def Menu():
  global B,C
  sleep(1)
  B=16
  fill_rect(0,0,320,222,"grey")
  N=0
  draw_string("Bataille Navale",80,20)
  while True:
    if keydown(KEY_UP) and N>0:
      N-=1
    if keydown(KEY_DOWN) and N<2:
      N+=1
    if N==0:
      draw_string("Jouer",130,80)
      draw_string("Nombre de Bateau",80,120,"black","grey")
      draw_string("  "+Format_3(str(B))+"  ",120,140,"black","grey")
      draw_string("Couleurs",120,160,"black","grey")
      draw_string("  "+str(Colors[C])+"    ",10,180,"black","grey")
      if keydown(KEY_OK):
        sleep(0.1)
        break
    if N==1:
      if keydown(KEY_LEFT)and B>2: 
        B-=1
        sleep(0.05)
      if keydown(KEY_RIGHT) and B<120:
        B+=1
        sleep(0.05)
      draw_string("Jouer",130,80,"black","grey")
      draw_string("Nombre de Bateau",80,120)
      draw_string("< "+Format_3(str(B))+" >",120,140)
      draw_string("Couleurs",120,160,"black","grey")
      draw_string("  "+str(Colors[C])+"    ",10,180,"black","grey")
    if N==2:
      if keydown(KEY_LEFT) and C>0:
        C-=1
        sleep(0.05)
      if keydown(KEY_RIGHT) and C<len(Colors)-1:
        C+=1
        sleep(0.05)
      draw_string("Jouer",130,80,"black","grey")
      draw_string("Nombre de Bateau",80,120,"black","grey")
      draw_string("  "+Format_3(str(B))+"  ",120,140,"black","grey")
      draw_string("Couleurs",120,160)
      draw_string("< "+str(Colors[C])+" >",10,180)
      
    sleep(0.05)
  Init()
Menu()
