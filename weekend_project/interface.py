from tkinter import *
from page1 import *
import webbrowser
def callback(url):
    webbrowser.open_new(url)

root= Tk()
def myclick():
    for i in list9:
        Label(root, text = "* "+i).pack()
    root.mainloop()
'''
def myclick():
    for indx in range(len(list9)):
        Label(root, text = "* "+list9[indx]).pack()
        link1.bind("<Button-1>", lambda e: callback(list8[indx]))
        indx+=1
    root.mainloop()


#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))'''

mylabel = Label(root,text="hello world!")
mybutton=Button(root,text="click me !",padx=50,pady=50,command=myclick)
mylabel.pack()
mybutton.pack()

root.mainloop()