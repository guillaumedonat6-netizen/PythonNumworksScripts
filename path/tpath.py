from path import *

P1=Point(10,10,"Depart")
P2=Point(310,210,"Arrive")

P3=Point(50,100,"P3")
P4=Point(125,200,"P4")
P5=Point(225,125,"P5")
P6=Point(175,75,"P6")
P7=Point(150,150,"P5")

P8=Point(100,25,"P8")
P9=Point(150,50,"P9")
P10=Point(100,100,"P10")
P11=Point(250,10,"P11")
P12=Point(275,75,"P12")
P13=Point(225,50,"P13")
P14=Point(300,150,"P14")
#P15=Point()

R1=Road(P1,P3,"R1",2)
R2=Road(P3,P4,"R2",1)
R3=Road(P4,P2,"R3",1)
R4=Road(P4,P5,"R4",1)
R5=Road(P5,P6,"R5",1)
R6=Road(P6,P7,"R6",1)
R7=Road(P7,P3,"R7",1)
R16=Road(P3,P10,"R16",1)

R8=Road(P1,P8,"R8",1)
print(R1.Dist,R8.Dist)
R9=Road(P8,P9,"R9",1)
R11=Road(P10,P6,"R11",1)
R10=Road(P9,P10,"R10",1)
R12=Road(P9,P11,"R12",1)
R14=Road(P11,P12,"R14",1)
R15=Road(P12,P14,"R15",1)
R17=Road(P14,P2,"R17",1)



LR=[R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R14,R15,R16,R17]

for i in LR:
  i.Draw((255,0,0))
  

LPathD,Dd=Get_S2_dist(P1,P2,0)
Draw_Path(LPathD,(0,255,0))
print(Dd)
