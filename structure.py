# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()			 

# Open window having dimension 100x100
root.geometry('1000x800') 

label= Label(root, text = "Resize your image here!",font=("Arial",27)).place(x=320,y=10)

# Create a Button

btn = Button(root, text = 'Select File', bd = '5',bg='Blue',font=("Arial",20))
btn.place(x=420,y=100)

root.mainloop()
				 
