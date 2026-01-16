from kandinsky import *
from random import *

def min(L):
  Mtemp=L[0]
  for i in L:
    if Mtemp>i:
      Mtemp=i
  return Mtemp

class Point:
  def __init__(self,x,y,N):
    self.x=x
    self.y=y
    self.N=N
    self.RdL=[]
  def Draw(self):
    fill_rect(int(self.x-1),int(self.y-1),3,3,"black")
  def GetRoadTo(self,PA):
    for i in self.RdL:
      if i.GetNPoint()==PA:
        return i
  

class Road:
  def __init__(self,P1,P2,N,M):
    self.P1=P1
    self.P2=P2
    self.M=M
    self.N=N
    self.Dist=(((P1.x-P2.x)**2+(P1.y-P2.y)**2)**(1/2))*M
    self.P1.RdL.append(self)
  def GetNPoint(self):
    return self.P2
  def Draw(self,C):
    distx=self.P2.x-self.P1.x
    disty=self.P2.y-self.P1.y
    for i in range(int(self.Dist)):
      pro=i/self.Dist
      fill_rect(int(self.P1.x+pro*distx),int(self.P1.y+pro*disty),2,2,(C[0]-255*((self.M-1)/10),C[1]-255*((self.M-1)/10),C[2]-255*((self.M-1)/10)))
    self.P1.Draw()
    self.P2.Draw()

def Get_S1_dist(PD,PA,D):
    LPath=[PD]
    while not (PD==PA):
        LDTemp = []
        LRTemp  = []
        if len(PD.RdL)==1:
          LDTemp=[PD.RdL[0].Dist]
          LRTemp=[PD.RdL[0]]
        else:
          for i in PD.RdL:
            if not(i.GetNPoint() in LPath):
              LRTemp.append(i)
              LDTemp.append(i.Dist)
        if LDTemp==[]:
          LDTemp=[PD.RdL[0].Dist]
          LRTemp=[PD.RdL[0]]
        D+=min(LDTemp)
        PD=LRTemp[LDTemp.index(min(LDTemp))].GetNPoint()
        LPath.append(PD)
    return LPath,D
        
def Get_S2_dist(PD,PA,D):
    LPath=[PD]
    while not (PD==PA):
      LDTemp_1 = []
      LRTemp_1  = []
      LDTemp_2 = []
      LRTemp_2  = []
      LD_1_Temp = []
      LR_1_Temp = []
      LDtot = []
      PD2 = 0
      if len(PD.RdL)==1:
        D+=PD.RdL[0].Dist
        PD=PD.RdL[0].GetNPoint()
        LPath.append(PD)
      else:
          for i1 in PD.RdL:
            LD_1_Temp.append(i1.Dist)
            LR_1_Temp.append(i1)
            PD2 = i1.GetNPoint()
            for i2 in PD2.RdL:
              LDTemp_2.append(i1.Dist+i2.Dist)
              LRTemp_2.append(i2)
            LDTemp_1.append(LDTemp_2)
            LRTemp_1.append(LRTemp_2)
            LDTemp_2 = []
            LRTemp_2  = []
          for dL in LDTemp_1:
            if not(dL==[]):
              Mintemp_1 = min(dL)
              LDtot.append(Mintemp_1)
          Mintemp_2=min(LDtot)
          D+=LD_1_Temp[LDtot.index(Mintemp_2)]
          PD=LR_1_Temp[LDtot.index(Mintemp_2)].GetNPoint()
          LR_1_Temp[LDtot.index(Mintemp_2)].Draw((255,255,0))
          LPath.append(PD)
          LD_1_Temp=[]
          LR_1_Temp=[]
    return LPath,D

def Draw_Path(P,C):
  for i in range(len(P)-1):
    P[i].GetRoadTo(P[i+1]).Draw(C)
  
