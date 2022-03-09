#importing the needed files for this interface
from tkinter import *
from page1 import *
import webbrowser

def callback(url):
    '''just calls a browser'''
    webbrowser.open_new(url)

def click():
    '''click function for when the button is clicked'''
    for i in list9:
        Label(Tk(), text = "* "+i).pack()
    Tk().mainloop()

'''
THIS SOME PART OF CODE THAT I AM WORKING ON 
def myclick():
    for indx in range(len(list9)):
        Label(root, text = "* "+list9[indx]).pack()
        link1.bind("<Button-1>", lambda e: callback(list8[indx]))
        indx+=1
    Tk().mainloop()


#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))'''

mylabel = Label(Tk(),text="hello world!")
mybutton=Button(Tk(),text="click me !",padx=50,pady=50,command=click)
mylabel.pack()
mybutton.pack()

Tk().mainloop()