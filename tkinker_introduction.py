import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidget()

    def createWidget(self):
        self.quitButton=tk.Button(self,text='quit',command=self.quit())
        self.quitButton.grid()


app=Application()
app.master.tittle('sample application')

#app.__getattribute__(self.tk,app)
app.mainloop()