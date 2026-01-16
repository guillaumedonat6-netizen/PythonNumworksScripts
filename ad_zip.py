from random import *

def Search(L,x):
  c=1
  M=""
  ms=""
  Lms=[]
  for i in range(len(L)-(x-1)):
    ms=""
    for e in range(x):
      ms+=L[i+e]
    if L.count(ms)>c and not(ms in Lms):
      c=L.count(ms)
      M=ms
    Lms.append(ms)
  return c,M

def Compress(Hm,X,xmax):
  for X in range(X):
    Nm,Mm=0,""
    print("Search")
    for i in range(2,xmax):
      N,M=Search(Hm["str"],i)
      if N>=Nm:
        if len(M)>len(Mm):
          Nm,Mm=N,M
    Hm["LM"].append(Mm)
    print("Stops")
    if "" == Hm["LM"][len(Hm["LM"])-1]:
      print("Blank stop")
      break
    if len(Hm["LM"][len(Hm["LM"])-1])>= len(Hm["str"]):
      print("Len stop")
      break
    print("Replace")
    Hm["str"]=Hm["str"].replace(Mm,str(len(Hm["LM"])+2))
    print("Len(Hm[LM]):",len(Hm["LM"]),"Len(Hm[str]:",len(Hm["str"])," Mm:",Hm["LM"][len(Hm["LM"])-1]," Nm:",Nm)
  return Hm

def UnCompress(Hm):
  while len(Hm["LM"])>0:
    Hm["str"]=Hm["str"].replace(str(len(Hm["LM"])+2),Hm["LM"][len(Hm["LM"])-1])
    Hm["LM"].pop()
    #print(Hm["LM"],Hm["str"])
  return Hm["str"]

def Generate(x):
  bS=""
  for i in range(x):
    bS+=choice(["1","0"])
  return {"str":bS,"LM":[]}
