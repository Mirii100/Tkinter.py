import tkinter
from tkinter import *
from tkinter import  messagebox
top =Tk()
# buttons in tkinter
w=Button(top,bg='green',text='hello world ',padx=20,pady=20, activebackground="red")
# place method is used to place button widget on windows and takes two arguments
w.place(x=50,y=50)
def main():
        msg=messagebox.showinfo('hae','how are yu called?')
        print('how is you?  ')
b=Button(top,bg='red',text='im doing tkimter in gui',command=main,activebackground='blue')
b.place(x=20,y=10)
c=Button(top,text='text',fg='purple',padx=20,pady=20)
c.place(x=30,y=30)
# canvas
ww=Canvas(top,bg='brown',height=250,width=200)
coord =19,50,240,210
arc=ww.create_arc(coord,start=0,extent=150,fill='blue')
# pack is for showing canvas  to the window
ww.pack()
# checkbutton
check1=IntVar()
check2 =IntVar()
l1=Label(top,text='gender :',name='ge')
l1.pack()
ch=Checkbutton(top,text='male',name='gen',variable=check1,\
               onvalue=1,offvalue=0,height=1,width=10)
ch1=Checkbutton(top,text='female',name='ge',variable=check2,\
               onvalue=1,offvalue=0,height=1,width=10)
ch.pack()
ch1.pack()
# entry
l=Label(top,text='usename',bg='green')
l.pack(side=LEFT)
e=Entry(top,bd=5)
e.pack(side=LEFT)









top.mainloop()