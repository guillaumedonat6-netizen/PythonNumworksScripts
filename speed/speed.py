from random import randint
from kandinsky import *
from time import *
from ion import *
from numpy import *
  
def Game(x):
  LT=[]
  for e in range(x):
    fill_rect(0,0,320,222,"black")
    for i in range(4):
      sleep(1)
      fill_rect(20+i*60,20,40,40,"red")
      fill_rect(20+i*60,80,40,40,"red")
      fill_rect(20+i*60,140,40,40,"red")
    
    sleep(randint(1,6))
  
    for i in range(5):
      fill_rect(20+i*60,20,40,40,"green")
      fill_rect(20+i*60,80,40,40,"green")
      fill_rect(20+i*60,140,40,40,"green")
    
    T1=monotonic()
    while not keydown(KEY_OK):
      pass
    Tf=monotonic()-T1
    draw_string("Time : "+str(Tf),160-len("Time : "+str(Tf))*5,195)
    LT.append(Tf)
    sleep(1)
  A=array(LT)
  fill_rect(0,0,320,222,"black")
  draw_string("Mean Time :"+str(mean(A)),160-5*len("Mean Time :"+str(mean(A))),70)
  draw_string("Max Time :"+str(max(A)),160-5*len("Max Time :"+str(max(A))),100)
  draw_string("Min Time :"+str(min(A)),160-5*len("Max Time :"+str(min(A))),130)
  draw_string("Median Time :"+str(median(A)),160-5*len("Median Time :"+str(median(A))),160)
  
  print("max :",max(A)," min :",min(A))
  print("mean :",mean(A)," median :",median(A))
