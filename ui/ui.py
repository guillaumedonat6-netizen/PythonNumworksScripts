from kandinsky import *
from ion import *

class UI_manager:
  def __init__(self,nui_max):
    self.Obj_data=[]
    self.nui=0
    self.nui_max=nui_max
    for i in range(nui_max):
      self.Obj_data.append([])
  
  def Change_State(self):
    if self.Obj_data[self.nui][1]=="button":
      if keydown(KEY_OK):
        self.Obj_data[self.nui][1].F()      
      
  def Change_Max_Object(self,Nnui):
    print(Nnui-self.nui_max)
    if Nnui-self.nui_max>0:
      for i in range(Nnui-self.nui_max):
        self.Obj_data.append([])
    else:
      for i in range(self.nui_max-Nnui):
        self.Obj_data.pop()
      self.Obj_data=self.Obj_data[0:Nui]
  
  def Add_Object(self,obj,nui,type):
    self.Obj_data[nui]=[obj,type]
  def Del_Object(self,nui):
    self.Obj_data[nui]=[]
    
  def Draw(self):
    x=0
    for i in self.Obj_data:
      if not(i==[]):
        if not(i[0].Enabled):
          i[0].U_Draw()
        elif x==self.nui:
          if i[1]=="button":
            i[0].O_Draw()
        else:
          i[0].N_Draw()
      x+=1
    
class Button:
  def __init__(self,coords,text,enabled,f,c1,c2,c3):
    self.Coords=coords
    self.Text=text
    self.F=f
    self.Enabled=enabled
    self.C1=c1
    self.C2=c2
    self.C3=c3
    
  def N_Draw(self):
    draw_string(self.Text,self.Coords[0],self.Coords[1],"black",self.C1)
  def O_Draw(self):
    draw_string(self.Text,self.Coords[0],self.Coords[1],"black",self.C2)
  def U_Draw(self):
    draw_string(self.Text,self.Coords[0],self.Coords[1],self.C3,self.C3)
