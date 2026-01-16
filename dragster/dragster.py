from kandinsky import *
from ion import *
from time import *

Shift=0

Max_rpm=2000

Rpm=0

Speed=0

Dist=0

t1=0

sleep(1)

while True:
  if keydown(KEY_OK):
    if not(keydown(KEY_RIGHT)) and Shift<8:
      Shift+=1
      if Shift==1 and t1==0:
        t1=monotonic()
        Max_rpm=3000
        Max_rpm+=2000+(Shift*400)
      Max_rpm+=2000+(Shift*400)
      Rpm-=1000
      sleep(0.1)
    elif keydown(KEY_RIGHT) and Shift>0:
      if -int(((Rpm-Max_rpm)/Max_rpm)*100)>=25:
        fill_rect(0,0,320,222,"black")
        draw_string("Engine burnt",100,100)
        break
      else:
        if Shift<8:
          Shift+=1
          if Shift==1 and t1==0:
            t1=monotonic()
          Max_rpm=3000
          Max_rpm+=2000+(Shift*400)
          Max_rpm+=2000+(Shift*400)
          Rpm-=2250
          sleep(0.1)
    if Rpm<0:
      Rpm=0
  if keydown(KEY_RIGHT):
    p=1+(50-int(Shift*4))*(2*Rpm/Max_rpm)
    Rpm+=p
    if Shift==0:
      if Rpm>2000:
        Rpm=2000
    elif Rpm>Max_rpm:
      Rpm-=p
      Rpm+=(50*((10-Shift)/10)*(Max_rpm/Rpm))/4
  else:
    Rpm-=150
    if Rpm<0:
      Rpm=0
  if Shift>0:
    C_speed=(((Rpm/2)/60)/100)*(Shift/3)
    Speed=(Speed+C_speed)/2
    Dist+=Speed
    if Dist>5000:
      break
  fill_rect(210,150,120,10,"white")
  draw_string(str(int(Rpm)),10,10)
  draw_string(str(int(Shift)),10,40)
  draw_string(str(Speed*100),10,80)
  draw_string(str(Dist),10,120)
  if Shift>0:
    draw_string(str(monotonic()-t1),100,10)
  C="green"
  if int((Rpm/Max_rpm)*100)>=100:
    C="red"
  elif int((Rpm/Max_rpm)*100)>=95:
    C="orange"
  elif int((Rpm/Max_rpm)*100)>=90:
    C="yellow"
  fill_rect(10+2*int((Rpm/Max_rpm)*100),150,200-2*int((Rpm/Max_rpm)*100),10,"black")
  fill_rect(10,150,2*int((Rpm/Max_rpm)*100),10,C)
  sleep(0.01)
print(str(monotonic()-t1))
