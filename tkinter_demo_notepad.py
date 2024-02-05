from tkinter import *
root=Tk()
def does():
    filewin =Toplevel(root)
    button=Button(filewin,text='do nothing ')
    button.pack()

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='new',command=does)
filemenu.add_command(label='open',command=does)
filemenu.add_command(label='save',command=does)
filemenu.add_command(label='close',command=does)
filemenu.add_command(label='save as',command=does)
filemenu.add_command(label='hello',command=does)
filemenu.add_separator()
filemenu.add_command(label='save',command=does)
menubar.add_cascade(label='file',menu=filemenu)
editmenu=Menu(menubar,tearoff=0)
filemenu.add_separator()
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='help',command=does)
menubar.add_cascade(label='help',menu=helpmenu)
filemenu.add_separator()
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label='edit',command=does)
editmenu.add_cascade(label='edit',menu=editmenu)




root.config(menu=menubar)
root.mainloop()