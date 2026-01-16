from time import *
from ion import *
from kandinsky import *
from random import *

class cards:
  def __init__(self):
    print("init cards")
  
  def Gouverneur(self,x,y):
    fill_rect(x,y,100,100,color(0,0,200))
    fill_rect(x+20,y+10,60,50,color(250,225,150))
    fill_rect(x+10,y+70,80,30,color(225,0,0))
    fill_rect(x+30,y+60,40,10,color(0,0,0))
    fill_rect(x+40,y+70,20,30,color(0,0,0))
    fill_rect(x+40,y+60,20,10,color(250,225,150))
    fill_rect(x+20,y+10,10,10,color(0,0,200))
    fill_rect(x+70,y+10,10,10,color(0,0,200))
    fill_rect(x+20,y+50,10,10,color(0,0,200))
    fill_rect(x+70,y+50,10,10,color(0,0,200))
    fill_rect(x+10,y+70,10,10,color(0,0,200))
    fill_rect(x+80,y+70,10,10,color(0,0,200))
    fill_rect(x+30,y+10,40,10,color(200,200,200))
    fill_rect(x+20,y+20,10,10,color(200,200,200))
    fill_rect(x+70,y+20,10,10,color(200,200,200))
  def Economiste(self,x,y):
    fill_rect(x,y,100,100,color(225,225,0))
    fill_rect(x+20,y+10,60,50,color(250,225,150))
    fill_rect(x+20,y+10,10,10,color(225,225,0))
    fill_rect(x+70,y+10,10,10,color(225,225,0))
    fill_rect(x+20,y+50,10,10,color(225,225,0))
    fill_rect(x+70,y+50,10,10,color(225,225,0))
    fill_rect(x+30,y+60,40,10,color(0,100,250))
    fill_rect(x+10,y+70,80,30,color(0,0,250))
    fill_rect(x+10,y+70,10,10,color(225,225,0))
    fill_rect(x+80,y+70,10,10,color(225,225,0))
    fill_rect(x+60,y+80,10,10,color(0,100,250))
    fill_rect(x+20,y+70,10,10,color(0,100,250))
    fill_rect(x+70,y+70,10,10,color(0,100,250))
    fill_rect(x+30,y+10,40,10,color(250,225,160))
    fill_rect(x+20,y+20,10,10,color(250,225,160))
    fill_rect(x+70,y+20,10,10,color(250,225,160))
  def Fou(self,x,y):
    fill_rect(x,y,100,100,color(225,0,0))
    fill_rect(x+20,y+20,60,50,color(250,225,150))
    fill_rect(x+20,y+20,10,10,color(225,0,0))
    fill_rect(x+70,y+20,10,10,color(225,0,0))
    fill_rect(x+20,y+60,10,10,color(225,0,0))
    fill_rect(x+70,y+60,10,10,color(225,0,0))
    fill_rect(x+20,y+80,20,10,color(0,0,225))
    fill_rect(x+30,y+70,20,10,color(0,0,225))
    fill_rect(x+20,y+90,20,10,color(0,50,200))
    fill_rect(x+40,y+80,20,10,color(0,50,200))
    fill_rect(x+50,y+70,20,10,color(0,50,200))
    fill_rect(x+60,y+80,20,10,color(0,100,150))
    fill_rect(x+40,y+90,20,10,color(0,100,150))
    fill_rect(x+60,y+90,20,10,color(0,125,125))
    fill_rect(x+20,y+30,10,10,color(0,250,0))
    fill_rect(x+30,y+20,10,10,color(0,225,0))
    fill_rect(x+40,y+10,10,20,color(0,175,0))
    fill_rect(x+50,y+10,10,20,color(0,125,0))
    fill_rect(x+60,y+20,10,10,color(0,75,0))
    fill_rect(x+70,y+30,10,10,color(0,50,0))
  def Militaire(self,x,y):
    fill_rect(x,y,100,100,color(0,75,0))
    fill_rect(x+20,y+10,60,50,color(250,225,150))
    fill_rect(x+30,y+60,40,10,color(0,150,0))
    fill_rect(x+20,y+10,10,10,color(0,75,0))
    fill_rect(x+70,y+10,10,10,color(0,75,0))
    fill_rect(x+20,y+50,10,10,color(0,75,0))
    fill_rect(x+70,y+50,10,10,color(0,75,0))
    fill_rect(x+10,y+70,80,30,color(0,150,0))
    fill_rect(x+10,y+70,10,10,color(0,75,0))
    fill_rect(x+80,y+70,10,10,color(0,75,0))
    fill_rect(x+20,y+70,10,10,color(150,0,0))
    fill_rect(x+70,y+70,10,10,color(150,0,0))
    fill_rect(x+10,y+80,10,10,color(150,0,0))
    fill_rect(x+80,y+80,10,10,color(150,0,0))
    fill_rect(x+40,y+70,20,30,color(220,220,220))
    fill_rect(x+40,y+60,20,10,color(250,225,150))
  def Scientifique(self,x,y):
    fill_rect(x,y,100,100,color(150,150,150))
    fill_rect(x+20,y+20,60,50,color(250,225,150))
    fill_rect(x+20,y+60,10,10,color(150,150,150))
    fill_rect(x+70,y+60,10,10,color(150,150,150))
    fill_rect(x+30,y+10,40,10,color(0,0,0))
    fill_rect(x+20,y+20,60,10,color(0,0,0))
    fill_rect(x+20,y+30,10,10,color(0,0,0))
    fill_rect(x+70,y+30,10,10,color(0,0,0))
    fill_rect(x+10,y+40,10,10,color(0,0,0))
    fill_rect(x+80,y+40,10,10,color(0,0,0))  
    fill_rect(x+40,y+70,20,10,color(250,225,150))
    fill_rect(x+20,y+80,60,20,color(217,217,217))
    fill_rect(x+30,y+70,10,20,color(225,225,225))
    fill_rect(x+60,y+70,10,20,color(225,225,225))
    fill_rect(x+20,y+80,10,20,color(225,225,225))
    fill_rect(x+70,y+80,10,20,color(225,225,225))
    fill_rect(x+10,y+90,10,10,color(225,225,225))
    fill_rect(x+80,y+90,10,10,color(225,225,225))


def Game():
  fill_rect(0,0,320,222,"black")
  L_Q_Gouv=[{"q":"Le peuple reclame plus de liberte financiere. Devons nous accepter ?","o":(1,0,-1),"n":(-1,0,2)},{"q":"Une tempete arrive. Devons nous proteger le peuple ?","n":(-2,0,1),"o":(2,0,-1)},{"q":"Un vernisage d\'une exposition est en cour. Devons nous y aller ?","o":(1,0,0),"n":(0,0,0)},{"q":"Une mine d\'or a ete decouverte ! Devons nous garder l\'argent ?","o":(-1,0,4),"n":(2,2,1)}]
  L_Q_Mili=[{"q":"Les banques ont trop d\'argent. Donnez en a l\'armee !","o":(0,2,-2),"n":(0,-2,1)},{"q":"Les pays voisin sont puissant. Faisont une mobilisation generale !","o":(-1,2,0),"n":(0,-1,0)},{"q":"Un fou semble deranger les habitants et pretend connaitre l\'avenir. Doit on l\'arreter ?","o":(-2,1,0,"Fou"),"n":(1,-1,0)},{"q":"La scientifique ne me laisse pas utiliser le labo pour creer une arme. Ai-je le droit d\'y aller ?","o":(0,8,0,"Fin_Bombe"),"n":(0,-1,1)}]
  L_Q_Eco=[{"q":"Nous pourrions creer des taxes de douane pour gagner plus d\'argent. Etes-vous d\'accord ?","o":(-1,0,2),"n":(0,0,0)},{"q":"Les bourses s'effondre ! Devons nous acheter plus d\'actions ?","o":(0,0,-2),"n":(0,0,1)},{"q":"Vous devriez mettre de l\'argent de cote, cela pourrai rapporter gros.","o":(0,0,3),"n":(0,0,1)}]
  L_P_total=15+15+10
  Peuple=5
  Armee=5
  Banque=5
  C=cards()
  
  while True:
    fill_rect(0,150,320,100,"black")
    C_type=randint(0,L_P_total)
    if 0<=C_type and C_type<15:
      C.Gouverneur(150,40)
      Q_N=randint(0,70)
      Qs={}
      if 0<=Q_N and Q_N<20:
        Qs=L_Q_Gouv[0]
      if 20<=Q_N and Q_N<40:
        Qs=L_Q_Gouv[1]
      if 40<=Q_N and Q_N<60:
        Qs=L_Q_Gouv[2]
      if 60<=Q_N and Q_N<=70:
        Qs=L_Q_Gouv[3]
      draw_string(format(Qs["q"]),0,150,"white","black")
      
    if 15<=C_type and C_type<30:
      C.Militaire(150,40)
      Q_N=randint(0,55)
      Qs={}
      if 0<=Q_N and Q_N<20:
        Qs=L_Q_Mili[0]
      if 20<=Q_N and Q_N<40:
        Qs=L_Q_Mili[1]
      if 40<=Q_N and Q_N<50:
        Qs=L_Q_Mili[2]
      if 50<=Q_N and Q_N<=55:
        Qs=L_Q_Mili[3]
      draw_string(format(Qs["q"]),0,150,"white","black")
      
    if 30<=C_type and C_type<40:
      C.Economiste(150,40)
      Q_N=randint(0,70)
      Qs={}
      if 0<=Q_N and Q_N<30:
        Qs=L_Q_Eco[0]
      if 30<=Q_N and Q_N<40:
        Qs=L_Q_Eco[1]
      if 40<=Q_N and Q_N<=70:
        Qs=L_Q_Eco[2]
      draw_string(format(Qs["q"]),0,150,"white","black")
        
    Choix="N"
    fill_rect(250,40,10,100,color(0,0,0))
    fill_rect(140,40,10,100,color(0,0,0))
    Peuple,Armee,Banque=Modify((Peuple,Armee,Banque),(0,0,0))
    while True:
      if keydown(KEY_LEFT):
        Choix="n"
        fill_rect(140,40,10,100,color(255,0,0))
        fill_rect(250,40,10,100,color(0,0,0))
      if keydown(KEY_RIGHT):
        Choix="o"
        fill_rect(140,40,10,100,color(0,0,0))
        fill_rect(250,40,10,100,color(0,255,0))
      sleep(0.1)
      if keydown(KEY_OK) and (Choix!="N"):
        break
    Peuple,Armee,Banque=Modify((Peuple,Armee,Banque),Qs[Choix])
    print(Peuple,Armee,Banque)
    sleep(0.5)

def format(T):
  Txt=""
  N=0
  for i in T:
    N+=1
    Txt+=i
    if N>=25 and i==" ":
      N=0
      Txt+="\n"
  return Txt

def Modify(Var,Mod):
  Var1=Var[0]
  Var2=Var[1]
  Var3=Var[2]
  
  fill_rect(0,0,320,40,"black")
  fill_rect(10,40,10,100,"black")
  fill_rect(60,40,10,100,"black")
  fill_rect(120,40,10,100,"black")
  
  fill_rect(10,40+(10-Var1)*10,10,int(Var1*10),"white")
  fill_rect(60,40+(10-Var2)*10,10,int(Var2*10),"white")
  fill_rect(120,40+(10-Var3)*10,10,int(Var3*10),"white")
  
  if Var1+Mod[0]>=10:
    Mod=(10-Var1,Mod[1],Mod[2])
  if Var2+Mod[1]>=10:
    Mod=(Mod[0],10-Var2,Mod[2])
  if Var3+Mod[2]>=10:
    Mod=(Mod[0],Mod[1],10-Var3)
  
  
  if Mod[0]>0:
    C1="green"
  elif Mod[0]<0:
    C1="red"
  else:
    C1="black"
  if Mod[1]>0:
    C2="green"
  elif Mod[1]<0:
    C2="red"
  else:
    C2="black"
  if Mod[2]>0:
    C3="green"
  elif Mod[2]<0:
    C3="red"
  else:
    C3="black"
  
  fill_rect(10,40+(10-Var1-Mod[0])*10,10,int(Mod[0]*10),C1)
  fill_rect(60,40+(10-Var2-Mod[1])*10,10,int(Mod[1]*10),C2)
  fill_rect(120,40+(10-Var3-Mod[2])*10,10,int(Mod[2]*10),C3)
  
  Var1=Var1+Mod[0]
  Var2=Var2+Mod[1]
  Var3=Var3+Mod[2]
  
  return (Var1,Var2,Var3)
Game()
