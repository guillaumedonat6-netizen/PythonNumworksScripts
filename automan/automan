from kandinsky import *
from time import sleep
from ion import *
from random import choice,randint

class Manager:
  def __init__(self,x,y,O):
    self.L_Convey=[]
    self.L_Machine=[]
    self.L_Mining=[]
    self.L_Item=[]
    self.Map=[]
    self.x,self.y,self.O=x,y,O
    self.items=[0,0,0,0,0]
    L1=[]
    for i in range(0,220,10):
      L1=[]
      for e in range(0,220,10):
        T=choice([-1,1,2])
        L1.append(T)
        if T==-1:
          fill_rect(i,e,10,10,color(150,105,50))
        if T==1:
          fill_rect(i,e,10,10,color(50,50,50))
        if T==2:
          fill_rect(i,e,10,10,color(100,100,100))
      self.Map.append(L1)
    L1=[]
  def Draw(self):
    for i in self.L_Convey:
      i.Draw()
    for i in self.L_Item:
      i.Draw()
    for i in self.L_Machine:
      i.Draw()
    for i in self.L_Mining:
      i.Draw()
    fill_rect(self.x,self.y,10,10,color(75,75,0))
    fill_rect(self.x+2,self.y+2,6,6,color(200,200,0))
    
  def Update(self):
    for I in self.L_Item:
      for C in self.L_Convey:
        if (I.x,I.y)==(C.x,C.y):
          I.x,I.y=I.x+C.d[0]*10,I.y+C.d[1]*10
          break
      for M in self.L_Machine:
        if (I.x,I.y)==(M.x,M.y):
          M.items[I.i]=M.items[I.i]+1
          self.L_Item.remove(I)
          break
      if (I.x,I.y)==(self.x,self.y):
        self.items[I.i]=self.items[I.i]+1
        self.L_Item.remove(I)
      if self.Get_Block(I.x//10,I.y//10)[0]=="Map":
        self.L_Item.remove(I)
    for M in self.L_Machine:
      if M.ir==0:
        if M.items[1]>=2 and M.items[2]>=1:
          M.items[1]=M.items[1]-2
          M.items[2]=M.items[2]-1
          M.items[0]=M.items[0]+1
      if M.ir==3:
        if M.items[1]>=2:
          M.items[1]=M.items[1]-2
          M.items[3]=M.items[3]+1
      if M.ir==4:
        if M.items[2]>=2 and M.items[3]>=2:
          M.items[2]=M.items[2]-2
          M.items[3]=M.items[3]-2
          M.items[4]=M.items[4]+1
      if M.items[M.ir]>0:
        for i in self.FindConvey(M,M.items[M.ir]):
          self.L_Item.append(Item(i.x,i.y,M.ir))
          M.items[M.ir]=M.items[M.ir]-1
    for Min in self.L_Mining:
      for i in self.FindConvey(Min,1):
        if not(self.Map[Min.x//10][Min.y//10]==-1):
          self.L_Item.append(Item(i.x,i.y,self.Map[Min.x//10][Min.y//10]))
    for o in range(len(self.O)):
      if not(self.O[o]<=self.items[o]):
        return False
    return True
      
  def T_Draw(self,x,y):
    T=self.Map[x][y]
    if T==-1:
      fill_rect(x*10,y*10,10,10,color(150,105,50))
    if T==1:
      fill_rect(x*10,y*10,10,10,color(50,50,50))
    if T==2:
      fill_rect(x*10,y*10,10,10,color(100,100,100))
  
  def Get_Block(self,x,y):
    for i in self.L_Convey:
      if (i.x,i.y)==(x*10,y*10):
        return ("Conveyor",i)
    for i in self.L_Machine:
      if (i.x,i.y)==(x*10,y*10):
        return("Machine",i)
    for i in self.L_Mining:
      if (i.x,i.y)==(x*10,y*10):
        return("Minner",i)
    if (self.x,self.y)==(x*10,y*10):
      return ("Core",self)
    return ("Map",self.Map[x][y])
  
  def FindConvey(self,M,n):
    LCnear=[]
    for C in self.L_Convey:
      for i in range(0,3):
        for e in range(0,3):
          if (M.x+(1-i)*10,M.y+(1-e)*10)==(C.x,C.y):
            LCnear.append(C)
    for I in self.L_Item:
      for c in LCnear:
        if (I.x,I.y)==(c.x,c.y):
          LCnear.remove(c)
    Lr=[]
    for i in range(n):
      if not(LCnear==[]):
        Lr.append(choice(LCnear))
        LCnear.remove(Lr[len(Lr)-1])
      LCnear=[]
    return Lr    

class Minner:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def Draw(self):
    fill_rect(self.x,self.y+3,10,4,color(100,100,100))
    fill_rect(self.x+3,self.y,4,10,color(100,100,100))
    fill_rect(self.x+2,self.y+2,6,6,color(150,150,150))

class Item:
  def __init__(self,x,y,i):
    self.x=x
    self.y=y
    self.i=i
    
  def Draw(self):
    if self.i==0:
      fill_rect(self.x+2,self.y+2,6,6,color(255,255,0))
    if self.i==1:
      fill_rect(self.x+2,self.y+2,6,6,color(0,0,0))
    if self.i==2:
      fill_rect(self.x+2,self.y+2,6,6,color(150,150,150))
    if self.i==3:
      fill_rect(self.x+2,self.y+2,6,6,color(0,0,200))
    if self.i==4:
      fill_rect(self.x+2,self.y+2,6,6,color(0,200,200))

class Machine:
  def __init__(self,x,y,ir):
    self.x=x
    self.y=y
    self.ir=ir
    self.items=[0,0,0,0,0]
  
  def Draw(self):
    fill_rect(self.x,self.y,10,10,color(150,150,150))
    fill_rect(self.x+1,self.y+1,8,8,color(175,175,175))
    if self.ir==0:
      fill_rect(self.x+3,self.y+3,4,4,color(200,200,0))
    if self.ir==3:
      fill_rect(self.x+3,self.y+3,4,4,color(0,0,200))
    if self.ir==4:
      fill_rect(self.x+3,self.y+3,4,4,color(0,200,200))

class Conveyor:
  def __init__(self,x,y,d):
    self.x=x
    self.y=y
    self.d=d
  
  def Draw(self):
    fill_rect(self.x,self.y,10,10,color(75,75,75))
    if self.d[1]==-1:
      for i in range(3):
        fill_rect(self.x,self.y+i,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+4,self.y+i,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+8,self.y+i,2,2,color(100,100,100))
    elif self.d[1]==1:
      for i in range(3):
        fill_rect(self.x,self.y+6+i,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+4,self.y+6+i,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+8,self.y+6+i,2,2,color(100,100,100))
    if self.d[0]==-1:
      for i in range(3):
        fill_rect(self.x+i,self.y,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+i,self.y+4,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+i,self.y+8,2,2,color(100,100,100))
    elif self.d[0]==1:
      for i in range(3):
        fill_rect(self.x+6+i,self.y,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+6+i,self.y+4,2,2,color(100,100,100))
      for i in range(3):
        fill_rect(self.x+6+i,self.y+8,2,2,color(100,100,100))


Obj=[]
Dif=float(input("Enter dificulty :"))
for i in range(5):
  Obj.append(int(randint(100,400)*Dif))

fill_rect(0,0,320,222,color(0,0,0))

Mn=Manager(randint(1,20)*10,randint(1,20)*10,Obj)

def Get_Name(i):
  if i==0:
    return "or"
  if i==1:
    return "charbon"
  if i==2:
    return "pierre"
  if i==3:
    return "graphite"
  if i==4:
    return "tsungene"
  return "nothing"

def Get_Recepice(i):
  if i==0:
    return [0,2,1,0,0]
  if i==3:
    return [0,2,0,0,0]
  if i==4:
    return [0,0,2,2,0]
  return [0,0,0,0,0]
    
  

def D_P(x,y):
  fill_rect(x*10,y*10,10,2,color(150,150,0))
  fill_rect(x*10,y*10,2,10,color(150,150,0))
  fill_rect(x*10+8,y*10,2,10,color(150,150,0))
  fill_rect(x*10,y*10+8,10,2,color(150,150,0))

def D_side(x,y):
  fill_rect(220,0,100,222,"black")
  B=Mn.Get_Block(x,y)
  draw_string(B[0],225,10)
  draw_string("x:"+str(x+1),230,30)
  draw_string("y:"+str(y+1),280,30)
  if B[0]=="Conveyor":
    draw_string("Direction",225,50)
    draw_string("x:"+str(B[1].d[0]),240,70)
    draw_string("y:"+str(B[1].d[1]),240,90)
  if B[0]=="Minner":
    draw_string("Product",225,50)
    draw_string(Get_Name(Mn.Map[x][y]),230,70)
  if B[0]=="Machine":
    draw_string("Product",225,50)
    draw_string(Get_Name(B[1].ir),230,70)
    draw_string("Needs",225,90)
    for i in range(len(B[1].items)):
      draw_string(str(B[1].items[i])+"/"+str(Get_Recepice(B[1].ir)[i]),230,110+i*20)
  if B[0]=="Core":
    draw_string("Goal",225,50)
    for i in range(len(B[1].O)):
      draw_string(str(B[1].items[i])+"/"+str(B[1].O[i]),230,70+20*i)      
  if B[0]=="Map":
    draw_string("Type",225,50)
    draw_string(str(Get_Name(Mn.Map[x][y])),230,70)
    

def Game():
  x=0
  y=0
  Tr=10
  Mn.Draw()
  D_P(x,y)
  Win=False
  Tr2=4
  while not Win:
    if keydown(KEY_NINE):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(1,-1)))
    if keydown(KEY_EIGHT):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(0,-1)))
    if keydown(KEY_SEVEN):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(-1,-1)))
    if keydown(KEY_FOUR):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(-1,0)))
    if keydown(KEY_SIX):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(1,0)))
    if keydown(KEY_ONE):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(-1,1)))
    if keydown(KEY_TWO):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(0,1)))
    if keydown(KEY_THREE):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Convey.append(Conveyor(x*10,y*10,(1,1)))
    if keydown(KEY_FIVE):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Mining.append(Minner(x*10,y*10))
    if keydown(KEY_LEFTPARENTHESIS):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Machine.append(Machine(x*10,y*10,0))
    if keydown(KEY_DIVISION):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Machine.append(Machine(x*10,y*10,3))
    if keydown(KEY_PLUS):
      if Mn.Get_Block(x,y)[0]=="Map":
        Mn.L_Machine.append(Machine(x*10,y*10,4))
    if keydown(KEY_BACKSPACE):
      T=Mn.Get_Block(x,y)
      if T[0]=="Conveyor":
        Mn.L_Convey.remove(T[1])
      if T[0]=="Machine":
        Mn.L_Machine.remove(T[1])
      if T[0]=="Minner":
        Mn.L_Mining.remove(T[1])
      Mn.T_Draw(x,y)
    if keydown(KEY_DOWN) and y<21:
      Mn.T_Draw(x,y)
      y+=1
      D_side(x,y)
    if keydown(KEY_RIGHT) and x<21:
      Mn.T_Draw(x,y)
      x+=1
      D_side(x,y)
    if keydown(KEY_UP) and y>0:
      Mn.T_Draw(x,y)
      y-=1
      D_side(x,y)
    if keydown(KEY_LEFT) and x>0:
      Mn.T_Draw(x,y)
      x-=1
      D_side(x,y)
    if Tr2<=0:
      Tr2=4
      Win=Mn.Update()
      Mn.Draw()
      D_P(x,y)
      D_side(x,y)
    Tr2-=1
    Tr-=1
    if Tr<=20:
      Tr=20
      D_side(x,y)
    sleep(0.05)
  
  Mn.Update()
  Mn.Draw()
  D_P(x,y)
  D_side(x,y)

Mn.Draw()
Game()
draw_string("Sucess",120,90)
