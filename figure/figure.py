from math import *
from kandinsky import *

def LineAB(A,B,T,C):
  a1=0
  if not(A[0]-B[0]==0):
    a1=(B[1]-A[1])/(B[0]-A[0])
  p1=A[1]-A[0]*a1
  F1=lambda x:a1*x+p1
  a2=0
  if not(A[1]-B[1]==0):
    a2=(B[0]-A[0])/(B[1]-A[1])
  p2=A[0]-A[1]*a2
  F2=lambda x:a2*x+p2  
  if A[0]>B[0]:
    for i in range(B[0],A[0]):
      fill_rect(i,int(F1(i)),T,T,C)
  else:
    for i in range(A[0],B[0]):
      fill_rect(i,int(F1(i)),T,T,C)
  if A[1]>B[1]:
    for i in range(B[1],A[1]):
      fill_rect(int(F2(i)),i,T,T,C)
  else:
    for i in range(A[1],B[1]):
      fill_rect(int(F2(i)),i,T,T,C)

def LineAL(A,Lx,Ly,T,C):
  B=(A[0]+Lx,A[1]+Ly)
  Line(A,B,T,C)

def CircleAR(A,R,T,C):
  for X in range(A[0]-R,A[0]+R+1):
    for Y in range(A[1]-R,A[1]+R+1):
      if (X>=0 and X<=320) and (Y>=0 and Y<=222):
        d=((A[0]-X)**2)+((A[1]-Y)**2)
        if int(d**(1/2))==R:
          fill_rect(X,Y,T,T,C)

def CircleAD(A,D,T,C):
  R=int(D/2)
  CircleAR(A,R,T,C)

def CircleAB(A,B,T,C):
  R=int((((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2))     
  CircleAR(A,R,T,C)

def DiskAR(A,R,C):
  y1,y2=320,0
  for X in range(A[0]-R,A[1]+R+1):
    for Y in range(A[1]-R,A[1]+R+1):
      if (X>=0 and X<=320) and (Y>=0 and Y<=222):
        d=((A[0]-X)**2)+((A[1]-Y)**2)
        if int(d**(1/2))==R:
          if Y<y1:
            y1=Y
          elif Y>y2:
            y2=Y
    fill_rect(X,y1,1,y2-y1,C)
    y1,y2=320,0

def DiskARR(A,R,R2,C,C2):
  DiskAR(A,R,C)
  DiskAR(A,R2,C2)

def DiskABR(A,B,R2,C,C2):
  R=int((((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2))
  DiskARR(A,R,R2,C,C2)

def DiskABC(A,B,c,C,C2):
  R=int((((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2))
  R2=int((((A[0]-c[0])**2)+((A[1]-c[1])**2))**(1/2))
  DiskARR(A,R,R2,C,C2)

def RectALL(A,L1,L2,T,C,C2):
  fill_rect(A[0],A[1],L1,L2,C)
  fill_rect(A[0]+T,A[1]+T,L1-2*T,L2-2*T,C2)

def RectABL(A,B,L2,T,C,C2):
  L1=int((((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2))
  RectALL(A,L1,L2,T,C,C2)

def RectABC(A,B,c,T,C,C2):
  L1=int((((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2))
  L2=int((((A[0]-c[0])**2)+((A[1]-c[1])**2))**(1/2))
  RectALL(A,L1,L2,T,C,C2)
