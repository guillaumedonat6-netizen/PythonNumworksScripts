from time import *
from ion import *
from kandinsky import *
from random import *

def key1_Inp(K):
  t0=monotonic()
  while True:
    if keydown(K):
      t1=monotonic()
      return (t1-t0)

def key2_Inp(K1,K2):
  t0=monotonic()
  P1,P2=False,False
  while not(P1 and P2):
    if keydown(K1):
      t1=monotonic()
      P1=True
    if keydown(K2):
      t2=monotonic()
      P2=True
  return t1-t0,t2-t0

def key_Slider(K1,X,Y,C1,C2,ABS):
  I=choice([1,-1])
  V=0
  fill_rect(X-51,Y-3,104,8,"black")
  fill_rect(X-50,Y-2,102,2,"yellow")
  fill_rect(X-10,Y-2,22,2,"red")
  while True:
    if V>=50:
      I=-1
    if V<=-50:
      I=1
    if keydown(K1):
      break
    fill_rect(X+V,Y,2,4,C2)
    V+=I
    fill_rect(X+V,Y,2,4,C1)
    sleep(0.0025)
  Nv=1-(V/50)
  if ABS/
    return ((Nv)**2)**(1/2)
  else:
    return Nv

def key_Name(K):
  if KEY_DIVISION==K:
    return "/"
  if KEY_MINUS==K:
    return "-"
  if KEY_RIGHTPARENTHESIS==K:
    return ")"
  if KEY_MULTIPLICATION==K:
    return "*"
  if KEY_SEVEN==K:
    return "7"
  if KEY_FOUR==K:
    return "4"
  if KEY_FIVE==K:
    return "5"
  if KEY_ONE==K:
    return "1"
  

def Run(V):
  fill_rect(0,0,320,222,"green")
  fill_rect(0,90,320,42,color(215,0,0))
  fill_rect(0,110,320,2,"white")
  fill_rect(0,90,320,2,"white")
  fill_rect(0,90+42-2,320,2,"white")
  fill_rect(20,90,2,42,"white")
  fill_rect(320-20,90,2,42,"white")
  xp1,xp2=0,0
  LKP1=[KEY_SEVEN,KEY_FIVE,KEY_FOUR,KEY_ONE]
  LKP2=[KEY_DIVISION,KEY_MULTIPLICATION,KEY_RIGHTPARENTHESIS,KEY_MINUS]
  PKP1,PKP2=0,0
  KP1,KP2=0,0
  WinP1=True
  fill_rect(22+xp1,94,14,14,"blue")
  fill_rect(22+xp2,94+20,14,14,"orange")
  for i in range(3):
    draw_string(str(3-i),150,40)
    sleep(1)
  draw_string("Go",150,40)
  sleep(1)
  draw_string("Go",150,40,"green","green")
  while not(xp1>278 or xp2>278):
    while ((PKP1==KP1) or (PKP2==KP2)):
      KP1,KP2=choice(LKP1),choice(LKP2)
    PKP1,PKP2=KP1,KP2
    draw_string(key_Name(KP1),10,10)
    draw_string(key_Name(KP2),10,160)
    tp1,tp2=key2_Inp(KP1,KP2)
    if tp1<tp2:
      tp1=V
      tp2=((1-(tp2/tp1))**8)*V
    else:
      tp2=V
      tp1=((1-(tp1/tp2))**8)*V
    print(tp1,tp2)
    draw_string(key_Name(KP1),10,10,"green","green")
    draw_string(key_Name(KP2),10,160,"green","green")
    while (tp1>0 or tp2>0):
      tp1-=1
      tp2-=1
      if tp1>0:
        fill_rect(22+xp1,94,1,14,color(215,0,0))
        xp1+=1
        if xp1>278:
            break
        fill_rect(22+xp1,94,14,14,"blue")
      if tp2>0:
        fill_rect(22+xp2,94+20,1,14,color(215,0,0))
        xp2+=1
        if xp2>278:
          break
        fill_rect(22+xp2,94+20,14,14,"orange")
      sleep((0.025/((abs(tp1)+abs(tp2)+1)/10)))
  if xp2+1==xp1:
    if tp1>tp2:
      WinP1=True
    else:
      WinP1=False
  if WinP1:
    draw_string("P1 Win",130,40)
  else:
    draw_string("P2 Win",130,40)


def LongJump(N,V,PV):
  Score=[0,0]
  S1,S2=0,0
  for i in range(2):
    fill_rect(0,0,320,222,"green")
    fill_rect(238,105,74,54,"brown")
    fill_rect(0,120,300,11*2,color(215,0,0))
    fill_rect(240,107,70,50,"yellow")
    fill_rect(10,120,2,22,"white")
    fill_rect(215,120,2,22,"white")    
    fill_rect(10,124,14,14,"blue")
    draw_string("P"+str(i+1)+" Turn",130,40)
    sleep(2)
    draw_string("P"+str(i+1)+" Turn",130,40,"green","green")
    xp=10
    vxp=0
    draw_string("Go",140,40)
    sleep(1)
    draw_string("Go",140,40,"green","green")
    while xp<203:
      T=key_Slider(KEY_FOUR,130,40,"white","green",True)
      vxp+=PV*T
      for i in range(V):
        fill_rect(10+xp,124,1,14,color(215,0,0))
        xp+=1
        fill_rect(10+xp,124,14,14,"blue")
        if xp>203:
          break
        sleep(0.1/(vxp))
    draw_string("Jump",130,40)
    sleep(0.5)
    draw_string("Jump",130,40,"green","green")
    a=35+89*key_Slider(KEY_FOUR,130,40,"white","green",False)
    D=(((a/360)*vxp)**2)-(4*-1*vxp)
    if S1==0:
      S1=(-((a/360)*vxp)-(D)**(1/2))/(-2)
    else:
      S2=(-((a/360)*vxp)-(D)**(1/2))/(-2)
  if S1>S2:
    Score[0]+=1
  else:
    Score[1]+=1
  print(Score,S1,S2)
