from math import *
from kandinsky import *
from time import *

VIEW_x=320
VIEW_y=222
VIEW_z=250


def Col_Lim(C):
  if C<0:
    return 0
  while C>255:
    C-=255
  return C

class Point:
  def __init__(self,x,y,z,C):
    self.x,self.y,self.z=x,y,z
    self.c=C
    self.C=color(Col_Lim(C[0]*(1-abs(z/VIEW_z))),Col_Lim(C[1]*(1-abs(z/VIEW_z))),Col_Lim(C[2]*(1-abs(z/VIEW_z))))
    self.px,self.py=Project(self.x,self.y,self.z)
  def Draw(self):
    T=11+10*(self.z/VIEW_z)
    fill_rect(int(self.px-T/2),int(self.py-T/2),int(T),int(T),color(self.C[0],self.C[1],self.C[2]))
  def UnDraw(self):
    T=11+10*(self.z/VIEW_z)
    fill_rect(int(self.px-T/2),int(self.py-T/2),int(T),int(T),color(self.C[0],self.C[1],self.C[2]))
  

def Origin(x,y,z):
  xx=(VIEW_x/2)-(VIEW_x-x)
  yy=(VIEW_y/2)-(VIEW_y-y)
  zz=(VIEW_z)-(VIEW_z-z)
  return xx,yy,zz

def Project(x,y,z):
  P=Origin(x,y,z)
  xx=x+(P[0])*(z/VIEW_z)
  yy=y+(P[1])*(z/VIEW_z)
  return xx,yy

def Line(P1,P2,CF=True,TF=False):
  distx=(P2.px-P1.px)
  disty=(P2.py-P1.py)
  distz=abs(P2.z)-abs(P1.z) 
  dist=sqrt((P1.px-P2.px)**2+(P1.py-P2.py)**2)
  if CF==True:
    distR=(P2.C[0]-P1.C[0])
    distG=((P2.C[1]-P1.C[1]))
    distB=((P2.C[2]-P1.C[2]))
  else:
    c=CF
  for i in range(dist):
    progress=i/dist
    if not(TF):
      T=11+10*((P1.z-progress*distz)/VIEW_z)
    else:
      T=1
    if CF==True:
      c=color(P1.C[0]+progress*distR,P1.C[1]+progress*distG,P1.C[2]+progress*distB)
    fill_rect(int(P1.px+progress*distx-T/2),int(P1.py+progress*disty-T/2),int(T),int(T),c)

def Face(P1,P2,P3,P4,D=1,CF=True,TF=False):
  distx2_1,distx4_3=P2.px-P1.px,P4.px-P3.px
  disty2_1,disty4_3=P2.py-P1.py,P4.py-P3.py
  distz2_1,distz4_3=abs(P2.z)-abs(P1.z),abs(P4.z)-abs(P3.z)
  distCR2_1,distCG2_1,distCB2_1=P2.C[0]-P1.C[0],P2.C[1]-P1.C[1],P2.C[2]-P1.C[2]
  distCR4_3,distCG4_3,distCB4_3=P4.C[0]-P3.C[0],P4.C[1]-P3.C[1],P4.C[2]-P3.C[2]
  Col_Lim(distCR2_1)
  Col_Lim(distCB2_1)
  Col_Lim(distCG2_1)
  Col_Lim(distCR4_3)
  Col_Lim(distCB4_3)
  Col_Lim(distCG4_3)
  PN3=Point(P3.x,P3.y,P3.z,P3.c)
  PN1=Point(P1.x,P1.y,P1.z,P1.c)
  for i in range(100*D+2):
    pr=i/((100*D))
    PN3=Point(P3.x+pr*distx4_3,P3.y+pr*disty4_3,P3.z-pr*distz4_3,(255,255,255))
    PN1=Point(P1.x+pr*distx2_1,P1.y+pr*disty2_1,P1.z-pr*distz2_1,(255,255,255))
    PN3.C=(P3.C[0]+pr*distCR4_3,P3.C[1]+pr*distCG4_3,P3.C[2]+pr*distCB4_3)
    PN1.C=(P1.C[0]+pr*distCR2_1,P1.C[1]+pr*distCG2_1,P1.C[2]+pr*distCB2_1)
    PN1.px=P1.px+pr*distx2_1
    PN1.py=P1.py+pr*disty2_1
    PN3.px=P3.px+pr*distx4_3
    PN3.py=P3.py+pr*disty4_3
    Line(PN3,PN1,CF,TF)
    
