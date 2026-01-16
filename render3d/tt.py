from render3d import *

P01=Point(50,50,0,(255,0,0))
P02=Point(50,200,0,(255,.0,0))
P03=Point(200,50,0,(255,0,0))
P04=Point(200,200,0,(255,0,0))
P11=Point(50,50,-100,(255,0,0))
P12=Point(50,200,-100,(255,0,0))
P13=Point(200,50,-100,(255,0,0))
P14=Point(200,200,-100,(255,0,0))

P11.Draw()
P12.Draw()
P13.Draw()
P14.Draw()

Face(P11,P12,P13,P14,2,True,True)
Face(P01,P02,P11,P12,2,True,True)
Face(P03,P04,P13,P14,2,True,True)
Face(P01,P03,P11,P13,2,True,True)
Face(P04,P02,P14,P12,2,True,True)


P01.Draw()
P02.Draw()
P03.Draw()
P04.Draw()

Line(P01,P03)
Line(P01,P02)
Line(P02,P04)
Line(P04,P03)

Line(P11,P13,"black",True)
Line(P11,P12,"black",True)
Line(P12,P14,"black",True)
Line(P14,P13,"black",True)

Line(P11,P01,"black",True)
Line(P12,P02,"black",True)
Line(P13,P03,"black",True)
Line(P14,P04,"black",True)

