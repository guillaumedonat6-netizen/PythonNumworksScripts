from math import *
from kandinsky import *

LDisplay=[]
def Display():
  global LDisplay
  fill_rect(0,0,320,222,color(0,0,0))
  for p in range(250):
    for i in LDisplay:
      if 250-p==int(i[0]):
        s=(250-i[0])/10
        fill_rect(int(i[1]-s/2),int(i[2]-s/2),int(s),int(s),color(i[3][0]-i[0],i[3][1]-i[0],i[3][2]-i[0]))
        LDisplay.remove(i)
  LDisplay=[]

class Point:
  def __init__(self,x,y,z,c):
    self.x=x
    self.y=y
    self.z=z
    self.c=c
  def Draw(self):
    LDisplay.append((self.z,self.x,self.y,self.c))
    
class Line:
  def __init__(self,p1,p2):
    self.p1=p1
    self.p2=p2
  def Draw(self,D):
    distance=sqrt((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2)
    distx=self.p2.x-self.p1.x
    disty=self.p2.y-self.p1.y
    distz=self.p2.z-self.p1.z
    distR=self.p2.c[0]-self.p1.c[0]
    distV=self.p2.c[1]-self.p1.c[1]
    distB=self.p2.c[2]-self.p1.c[2]
    
    for i in range(0,int(distance),int(D)):
      Pr=i/distance
      x=self.p1.x+distx*Pr
      y=self.p1.y+disty*Pr
      z=self.p1.z+distz*Pr
      c=color(self.p1.c[0]+distR*Pr,self.p1.c[1]+distV*Pr,self.p1.c[2]+distB*Pr)
      LDisplay.append((z,x,y,c))
