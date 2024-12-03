import tkinter

import importlib

from tkinter import *

root = tkinter.Tk()
root.configure( bg= 'white')
root.title('Calculator')

x = 0



Label = tkinter.Label(root, text='Calculator')

Label.pack()

frame6 = Frame(root)
frame6.pack()
frame6.configure(bg='gray')


def click1():
    new_value = int(x.get()) *0 + 1 + int(x.get()) *10  # Increment the current value of x
    x.set(new_value)  # Update the StringVar value
    
     
  
def click2():
    new_value = int(x.get()) *0 + 2 + int(x.get()) *10 
    x.set(new_value)  
def click3():
    new_value = int(x.get()) *0 + 3 + int(x.get()) *10
    x.set(new_value) 
def click4():
    new_value = int(x.get()) *0 + 4 + int(x.get()) *10
    x.set(new_value) 
def click5():
    new_value = int(x.get()) *0 + 5 + int(x.get()) *10
    x.set(new_value) 
def click6():
    new_value = int(x.get()) *0 + 6 + int(x.get()) *10
    x.set(new_value) 
def click7():
    new_value = int(x.get()) *0 + 7 + int(x.get()) *10
    x.set(new_value) 
def click8():
    new_value = int(x.get()) *0 + 8 + int(x.get()) *10
    x.set(new_value) 
def click9():
    new_value = int(x.get()) *0 + 9 + int(x.get()) *10
    x.set(new_value) 
def click0():
    new_value = int(x.get()) *0 + 0 + int(x.get()) *10
    x.set(new_value) 


x = StringVar()
x.set(0)


frame2 = Frame(root)
frame2.pack()

button5 = Button(frame2, text='1',command=click1) 
button5.pack(side='left')

button6 = Button(frame2, text='2',command=click2) 
button6.pack(side='left')

button7 = Button(frame2, text='3',command=click3) 
button7.pack(side='left')


frame3 = Frame(root)
frame3.pack()

button8 = Button(frame3, text='4',command=click4) 
button8.pack(side='left')

button9 = Button(frame3, text='5',command=click5) 
button9.pack(side='left')

button10 = Button(frame3, text='6',command=click6) 
button10.pack(side='left')

frame4 = Frame(root)
frame4.pack()

button11 = Button(frame4, text='7',command=click7) 
button11.pack(side='left')

button12 = Button(frame4, text='8',command=click8) 
button12.pack(side='left')

button13 = Button(frame4, text='9',command=click9) 
button13.pack(side='left')

frame5 = Frame(root)
frame5.pack()


button14 = Button(frame5, text='0',command=click0) 
button14.pack(side='bottom')



frame = Frame(root)
frame.pack() 


button = Button(frame, text='+') 
button.pack(side='left')

button2 = Button(frame, text='-') 
button2.pack(side='left')

button3 = Button(frame, text=' : ') 
button3.pack(side='left')

button4 = Button(frame, text='x') 
button4.pack(side='left')



Label = tkinter.Label(frame6, textvariable =(x))

Label.pack()


Label = tkinter.Label(root, text='= ')

Label.pack()

root.mainloop()


