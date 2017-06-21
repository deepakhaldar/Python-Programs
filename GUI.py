from tkinter import *

def func():
    print("Work work work work!!!")

root = Tk() # Creates a blank window

menu = Menu(root, tearoff=False)
root.config(menu=menu)

fileMenu=Menu(menu,tearoff=False)
menu.add_cascade(label='File', menu=fileMenu) #To make a drop down menu
fileMenu.add_command(label='New', command= func)
fileMenu.add_command(label='Open', command=func)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.destroy)


editMenu=Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='redo', command= func)

root.mainloop()
