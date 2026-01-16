from math import *
S_type=str(input("Type de suite (a,g) : "))

if S_type=="a":
  S_mode=str(input("Mode de construction\n (1: U0+n*R, 2: Up+(n-p)*R) : "))
  U0=0
  R=0
  if S_mode=="1":
    U0=float(input("Donnez U0 : "))
    R=(input("Donnez R : "))
    print("La suite est : "+"Un="+str(U0)+"+n*"+str(R))
  else:
    Up=float(input("Donnez Up : "))
    P=int(input("Donnez p : "))
    R=(input("Donnez R : "))
    U0=Up-R*P
    print("La suite est : "+"Un="+str(Up)+"+(n-"+str(P)+")*"+str(R))
    print("La suite est : "+"Un="+str(U0)+"+n*"+str(R))
  print("")
  boucle=True
  while boucle:
    S_action=str(input("Quelle action\n (1: info, 2: Somme, 3: calcul, 4: Search, 5: exit):"))
    if S_action=="5":
      boucle=False
    if S_action=="4":
      R_mode=input("1:Calcul <=, 2:Calcul >=, 3:Somme <= : ")
      if R_mode=="1":
        Ur=float(input("Donnez la valeur a\n atteindre/depasser : "))
        N=0
        Us=float(eval(str(U0)+"+"+str(N)+"*"+str(R)))
        while Us<=Ur:
          N+=1
          Us=float(eval(str(U0)+"+"+str(N)+"*"+str(R)))
        print("Atteint\n n="+str(N)+" pour Un="+str(Us))
        N-=1
        Us=float(eval("("+str(R)+"**"+str(N)+")*"+str(U0)))
        print("Au rang precedant\n n="+str(N)+" pour Un="+str(Us))
      if R_mode=="2":
        Ur=float(input("Donnez la valeur a\n atteindre/depasser : "))
        N=0
        Us=float(eval(str(U0)+"+"+str(N)+"*"+str(R)))
        while Us>=Ur:
          N+=1
    if S_action=="3":
      N=int(input("Donnez le rang n : "))
      Calcul=float(eval(str(U0)+"+"+str(N)+"*"+str(R)))
      print("U"+str(N)+" vaut : "+str(Calcul))
    if S_action=="2":
      N=int(input("Donnez le rang n : "))
      Un=float(eval(str(U0)+"+"+str(N)+"*"+str(R)))
      Somme=float((N+1)*((U0+Un)/2))
      print("La somme du rang 0 a "+str(N)+"est de : \n "+str(Somme))
    if S_action=="1":
      print("La suite est : "+"Un="+str(U0)+"+n*"+str(R))
      print("U0 : "+str(U0))
      print("R : "+str(R))
    print("")
if S_type=="g":
  S_mode=str(input("Mode de construction\n (1: (Q**n)*U0, 2: (Q**(n-p))*Up : "))
  U0=0
  Q=0
  if S_mode=="1":
    U0=float(input("Donnez U0 : "))
    Q=(input("Donnez Q : "))
    print("La suite est : Un=("+str(Q)+"**n)*"+str(U0))
  else:
    Up=float(input("Donnez Up : "))
    P=int(input("Donnez P : "))
    Q=(input("Donnez Q : "))
    U0=(Q**(-P))*Up
    print("La suite est : Un=("+str(Q)+"**(n-"+str(P)+")*"+str(Up))
    print("La suite est : Un=("+str(Q)+"**n)*"+str(U0))
  print("")
  boucle=True
  while boucle:
    S_action=str(input("Quelle action\n (1: info, 2: somme,\n 3: calcul, 4: Search,5: exit) : "))
    if S_action=="5":
      boucle=False
      continue
    if S_action=="4":
      R_mode=input("1:Calcul <=, 2:Calcul >=, 3:Somme <= : ")
      if R_mode=="1":
        Ur=float(input("Donnez la valeur a\n atteindre/depasser : "))
        N=0
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        while Us<=Ur:
          N+=1
          Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        print("Atteint\n n="+str(N)+" pour Un="+str(Us))
        N-=1
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        print("Au rang precedant\n n="+str(N)+" pour Un="+str(Us)) 
      if R_mode=="2":
        Ur=float(input("Donnez la valeur a\n atteindre/depasser : "))
        N=0
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        while Us>=Ur:
          N+=1
          Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        print("Atteint\n n="+str(N)+" pour Un="+str(Us))
        N-=1
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        print("Au rang precedant\n n="+str(N)+" pour Un="+str(Us))
      if R_mode=="3":
        Sr=float(input("Donnez la somme a\n atteindre/depasser : "))
        N=0
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        S=Us
        while S<=Sr:
          N+=1
          Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
          S+=Us
        print("Atteint\n n="+str(N)+" pour Un="+str(S))
        N-=1
        Us=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
        S-=Us
        print("Au rang precedant\n n="+str(N)+" pour Un="+str(S))
    if S_action=="3":
      N=int(input("Donnez le rang n : "))
      Calcul=float(eval("("+str(Q)+"**"+str(N)+")*"+str(U0)))
      print("U"+str(N)+" vaut : "+str(Calcul))
    if S_action=="2":
      N=int(input("Donnez le rang n : "))
      Somme=float(U0*((1-Q**(N+1))/(1-Q)))
      print("La somme du rang 0 a "+str(N)+" est de : \n"+str(Somme))
    if S_action=="1":
      print("La suite est : Un=("+str(Q)+"**n)*"+str(U0))
      print("U0 : "+str(U0))
      print("Q : "+str(Q))
    print("")
