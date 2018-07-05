from tkinter import *
import tkinter as tk

# Question number ::2
dictionary = {}

def d_update(x, y):
    dictionary.update({y:int(x)})  # Please note that these x and y vars are private to this function.  They are not the x and y vars as defined below.
    print(dictionary)

root = Tk()
root.title("Phone Diary")
root.geometry('300x200')
x = StringVar()  # Creating the variables that will get the user's input.
y = StringVar()
fr = tk.Frame(root)
fr.pack()
label_1 = Label(fr, text="Enter your Mobile Number!!", bg="BLACK", fg="white", width='25')
label_2 = Label(fr, text="Enter your Name!!", bg="BLACK", fg="white", width='25')
entry_1 = Entry(fr, textvariable=x, width='25')
entry_2 = Entry(fr, textvariable=y, width='25')

label_1.grid(row=0)
label_2.grid(row=3)

entry_1.grid(row=2, column=0)
entry_2.grid(row=4, column=0)

but = Button(fr, text="CreAte!!", bg="Black", fg="white", width='25', command=lambda :d_update(x.get(), y.get()))
# Note the use of lambda and the x and y variables.
but.grid(row=6, column=0)

root.mainloop()

# Question Number ::1


data = {'IndexKey_1 (Prakhar)': 706524968 , 'IndexKey_2 (Shruti)': 7896541237 , 'IndexKey_3 (Tapas)': 8796542541}
for key in data.keys():
    print(key)
pyt = Tk()
pyt.title(" Phone_diary GUI")
Label(pyt, text = "--------------------PHone DetAilS---------------------").grid(row=0,ipadx = 10,ipady = 10)
Label(pyt, text = data).grid(row=1,ipadx = 10,ipady = 10)


pyt.mainloop()