from tkinter import *

root = Tk()
def click():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()

button = Button(root, text="Click", command = click)


button.pack()
root.mainloop()
