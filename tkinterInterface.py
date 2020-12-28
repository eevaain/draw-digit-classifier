#Import libraries
from tkinter import *
import pyscreenshot as ImageGrab
import os

#Window
window = Tk()
window.title('Digits Classifier')
window.geometry('500x340+800-400')

#Create the drawing tool
def paint(event):
   x1, y1 = (event.x - 12), (event.y - 12)
   x2, y2 = (event.x + 12), (event.y + 12)
   drawingBoard.create_oval( x1, y1, x2, y2, fill = "white", outline = "")

#Canvas Box
drawingBoard = Canvas(window, width = 256, height = 256)
drawingBoard.pack()

def rectangle():
   drawingBoard.create_rectangle(0, 0, 256, 256, fill="black", outline = "")
   drawingBoard.bind("<B1-Motion>", paint)
rectangle()

#Drawing tool bottom message
message = Label(window, text = "Press and Drag Left Mouse Button to draw. Do not move window." )
message.pack(side = BOTTOM )

#Delete button
def delete():
   drawingBoard.delete(rectangle())

btn=Button(window, text="Clear Canvas!", fg='black', command = delete)
btn.place(x=350, y=50)
btn.pack()

#Saving the image variables

def saveImg():
   images_folder = "HandWrittenImages/"
   im = ImageGrab.grab(bbox=(929, 333, 1185, 589)) # X1,Y1,X2,Y2
   print ("saved....")
   im.save(images_folder+('image.png'))
   print("clear screen and redraw...")
   os.system('python MLcode.py')

#Predict drawing button
btn=Button(window, text="Predict Drawing!", fg='black', command = saveImg)
btn.place(x=350, y=100)
btn.pack()

drawingBoard.winfo_geometry()

window.mainloop()

