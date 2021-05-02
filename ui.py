from tkinter import *   
import os  
from PIL import ImageTk,Image
import tkinter.font as font
  
top = Tk()  
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("back1.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(top)
e.pack(fill=BOTH, expand=YES)  

def helloCallBack():
    os.system('recognize.py')

def picture():
    os.system('takeapic.py')

myFont = font.Font(size=15)

b = Button(top,text = "Recognize the Face",bg="black",fg="red",command=helloCallBack,height=4,width=18) 
b['font']=myFont

b1=Button(top,text="Take a picture",bg="black",fg="red",command=picture,height=4,width=18)
b1['font']=myFont

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom



  
b.place(x=450,y=400)  
b1.place(x=200,y=400)
app=FullScreenApp(top)
top.mainloop()  