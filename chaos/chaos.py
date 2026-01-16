from kandinsky import *
from math import *
from random import *
L_Sommet=[]
L_C=[(0,0,255),(255,0,0),(0,255,0),(0,255,255),(255,255,0),(255,0,255),(150,150,255),(255,150,150),(150,255,150),(150,255,255),(255,255,150),(255,150,255)]
L_CSommet=[]
for i in range(len(L_C)):
  C=choice(L_C)
  L_CSommet.append(C)
  L_C.remove(C)
L_Aire=[]
L_Point=[]
ratio=0


def Triangle(N,A,B,C,ratio=1/2,X=0,Y=0):
  global L_Sommet,L_Point,L_Aire
  L_Sommet=[A,B,C]
  Good=False
  dx=C[0]-B[0]
  dy=B[1]-A[1]
  if (X==0) and (Y==0):  
    while not Good:
      X,Y=randint(0,322),randint(0,222)
      for i in range(dy+1):
        pr=i/dy
        for e in range(dx*pr):
          if not (int(A[0]+((dx*pr)/2-e))>X):
            if (int(A[0]+((dx*pr)/2-e)),int(A[1]+i))==(X,Y):
              Good=True
  Iter(N,X,Y,ratio)


def Square(N,A,B,C,D,ratio=2/3,X=0,Y=0):
  global L_Sommet,L_Point,L_Aire
  L_Sommet=[A,B,C,D]
  Good=False
  dy=A[1]-C[1]
  if dy==0:
    dy=A[1]-B[1]
    if dy==0:
      dy=A[1]-D[1]
  dx=A[0]-C[0]
  if dx==0:
    dx=A[0]-B[0]
    if dx==0:
      dx=A[0]-D[0]
  if (X==0) and (Y==0):  
    while not Good:
      X,Y=randint(0,322),randint(0,222)
      for i in range(dy+1):
        pr=i/dy
        for e in range(dx):
          if not(int(A[0]+e)>X):
            if (int(A[0]+e),int(A[1]+i))==(X,Y):
              Good=True
  Iter(N,X,Y,ratio)


def Iter(N,X,Y,R):
  n=0
  while n<N:
    S=choice(L_Sommet)
    DX,DY=R*sqrt((S[0]-X)**2),R*sqrt((S[1]-Y)**2)
    DX,DY=copysign(DX,S[0]-X),copysign(DY,S[1]-Y)
    NX,NY=S[0]-DX,S[1]-DY
    C=(L_CSommet[L_Sommet.index(S)])
    if not(get_pixel(int(NX),int(NY))==(0,0,0)):
      C=((C[0]+get_pixel(int(NX),int(NY))[0])/2,(C[1]+get_pixel(int(NX),int(NY))[1])/2,(C[2]+get_pixel(int(NX),int(NY))[2])/2)
    fill_rect(int(NX),int(NY),1,1,C)
    X,Y=NX,NY
    n+=1
  D_Sommet()
    
def D_Sommet():
  for i in L_Sommet:
    fill_rect(int(i[0]),int(i[1]),1,1,L_CSommet[L_Sommet.index(i)])

a=450
fill_rect(0,0,320,222,"black")
Triangle(100000,(160,0),(160-a/3,a*sqrt(3)/4),(160+a/3,a*sqrt(3)/4),1/3,100,100)
  
