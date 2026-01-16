from kandinsky import *
from ion import *
from time import *

T,L=0,[]

def Draw(L):  
  for x in range(0,len(L)-1):
    for y in range(0,len(L[x])-1):
      C=255-255*L[x][y]
      C=color(C,C,C)
      fill_rect(x*T,y*T,T,T,C)

def UpChar(X,Y,L,x,y):
  C=255-255*L[X][Y]
  C=color(C,C,C)
  fill_rect(X*T,Y*T,T,T,C)
  X,Y=X+x,Y+y
  C=255-255*L[X][Y]
  C=color(C,C,C)
  fill_rect(X*T,Y*T,T,T,"red")
  fill_rect(X*T,Y*T,T-(1+int(T/5)),T-(1+int(T/5)),C)
  return X,Y

def Edit(L):
  fill_rect(0,0,320,222,"white")
  Draw(L)
  x,y=1,1
  x,y=UpChar(x,y,L,0,0)
  while not keydown(KEY_EXE):
    if keydown(KEY_BACKSPACE):
      fill_rect(0,0,320,222,"white")
      x,y=UpChar(x,y,L,0,0)
    if keydown(KEY_RIGHT) and x<int((320-T)/T):
      x,y=UpChar(x,y,L,1,0)
    if keydown(KEY_LEFT) and x>1:
      x,y=UpChar(x,y,L,-1,0)
    if keydown(KEY_UP) and y>1:
      x,y=UpChar(x,y,L,0,-1)
    if keydown(KEY_DOWN) and y<int((220-T)/T):
      x,y=UpChar(x,y,L,0,1)
    if keydown(KEY_OK):
      if L[x][y]==1:
        L[x][y]=0
      else:
        L[x][y]=1
      x,y=UpChar(x,y,L,0,0)
      sleep(0.05)
    sleep(0.1)

def Update(L):
  for X in range(1,len(L)-1):
    for Y in range(1,len(L[X])-1):
      C=0
      for i in range(3):
        if get_pixel((X-1)*T,(Y-1+i)*T)==color(0,0,0):
          C+=1
      for i in range(3):
        if get_pixel((X+1)*T,(Y-1+i)*T)==color(0,0,0):
          C+=1
      for i in range(2):
        if get_pixel((X)*T,(Y-1+(2*i))*T)==color(0,0,0):
          C+=1
      if L[X][Y]==0:    
        if C==3:
          L[X][Y]=1
      else:
        if C==2 or C==3:
          L[X][Y]=1
        else:
          L[X][Y]=0
      fill_rect(0,220,int((X/(len(L)-1)+0.01*(Y/(len(L[X])-1)))*320)+T,2,"green")

def Init(L):
  L=[]
  for X in range(0,int(320/T)):
    L1=[]
    for Y in range(0,int(220/T)):
      L1.append(0)
    L.append(L1)
    L1=[]
  return L
    
  

def Game():
  global L,Lcopy
  Edit(L)
  Draw(L)
  sleep(0.5)
  while not keydown(KEY_EXE):
    Update(L)
    fill_rect(0,220,320,222,"red")
    Draw(L)
    fill_rect(0,220,320,222,"white")

def Sintp():
  global T
  T=input("Size : ")
  if T=="" or T==" ":
    T=10
  else:
    T=int(T)

Sintp()
while True:
  try:
    L=Init(L)
    break
  except(MemoryError):
    print("Increase the Size given")
    Sintp()
while True:
  try:
    Game()
    sleep(0.5)
  except(MemoryError):
    print("Increase the Size given")
    Sintp()
