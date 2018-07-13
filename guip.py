#1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *
root = Tk()
root.title("Displaying Text")
root.geometry('200x200')
textL = Label(root, text = 'HELLO WORLD')
textL.pack()
exitB = Button(root,text ='EXIT',width = 10,command = root.destroy)
exitB.pack()


#2.Write a python program to in the same interface as above and create a action when the button is click it will display some text.

from tkinter import *

def display_text():
    #to display content on terminal
    print("hey")
    #to display content in new window
    r = Tk()
    r.title("ACTION PERFORMED")
    r.geometry('500x500')
    rL = Label(r,text = "Finally,button clicked and action performed")
    rL.pack()
    r.mainloop()
  
root = Tk()
root.title("Displaying Text")
root.geometry('200x200')
textL = Label(root, text = 'HELLO WORLD')
textL.pack()

DispB = Button(root , text = "click",width = 10,command = display_text)
DispB.pack()
exitB = Button(root,text ='EXIT',width = 10,command = root.destroy)
exitB.pack()


#3.Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

from tkinter import *
root = Tk()
root.title("CONCEPT OF FRAMES")
root.configure(background = 'orange')
root.geometry('500x500')

def change():
    lblL.config(text="UPDATED : Transforming Dreams Into Reality")
    
    

frame1 = Frame(root,bg = 'green')
frame1.pack(fill = X)
lblL = Label(frame1,text='INITIALLY : Grphic Era',bg = 'green')
lblL.pack()


updateB = Button(root,text = 'CLICK',width = 10,command = change)
updateB.pack()

exitB = Button(root,text ='EXIT',width = 10,command = root.destroy)
exitB.pack()

#4.Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *
root = Tk()
root.title("TAKING INPUT")
root.geometry('500x500')

def TakeInput():
    with open('try.txt') as f:
        data = f.readlines()
        print(data)
        
    
lblB = Button(root,text='CLICK',width = 10,command = TakeInput)
lblB.pack()

exitB = Button(root,text ='EXIT',width = 10,command = root.destroy)
exitB.pack()

root.mainloop()


