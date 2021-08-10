from tkinter import *
from functools import partial

root = Tk()
root.title("Yes, this is a calculator!")

anstext = StringVar()
l = Label(root, textvariable=anstext).grid(row=0, column=0, columnspan=4)

# The entry area used as display for input
e = Entry(root, font='24' ,width=41, borderwidth=10)
e.grid(row=1, column=0, columnspan=4)


n =0  #for inputting char at the end instead of at pos 0
eq = ['0']  #list of all working pieces

# clicking function of operators
def opclick(i):
    global n
    global eq
    eq.append(i)
    e.insert(n, i)
    n += 1

# clicking function of backspace (del one char)
def backspace():
    global eq
    e.delete(len(e.get()) - 1)
    #for deciding if number should be popped or just reduced by last digit
    if eq[-1].isnumeric():
        if int(eq[-1])>=10:
            eq[-1] = str(int(eq[-1])//10)
        elif len(eq)==1:
            eq[0] = '0'
        else:
            eq.pop()
    else:
        eq.pop()

    if len(eq)<2:
        anstext.set(eq[0])
    elif len(eq)>2:
        calculate()
    print(eq)


# clicking function of equal to sign/gives ans
def equal():
    global anstext
    global e
    eq.clear()
    eq.append(anstext.get())
    e.delete(0,END)
    e.insert(0,anstext.get())

#calculating the answers
def calculate():
    res= ''
    if eq[1] == '+':
        res = int(eq[0]) + int(eq[2])
    elif eq[1] == '-':
        res = int(eq[0]) - int(eq[2])
    elif eq[1] == '*':
        res = int(eq[0]) * int(eq[2])
    elif eq[1] == '/':
        res = int(eq[0]) / int(eq[2])

    anstext.set(res)

# clicking function of numbers
def click(i):
    global n
    e.insert(n,i)
    n+=1
    if not eq[-1].isnumeric():
        eq.append(str(i))
    else:
        eq[-1] = str(int(eq[-1]) * 10 + i)
    if len(eq)>=2:
        calculate()
    else:
        temp = anstext.get()
        anstext.set(temp+str(i))
    print(eq)


# clicking function of clear all (del everything/start fresh)
def clrall():
    global eq
    e.delete(0, END)
    eq = ['0']
    anstext.set('')

#creating the grid pattern of number buttons
for i in range(9,0,-1):
    c = 0
    if i%3 == 1:
        c = 2
    elif i%3 == 2:
        c = 1
    but = Button(root, text=i, font='20', height=2 ,width=10, command=partial(click, i)).grid(row=4-(i-1)//3, column=c)

#creating operator buttons
def op(x,y):
    but = Button(root, text=x, font='40', height=2 ,width=10, command=partial(opclick, x)).grid(row=y, column=3)

op('+', 2)
op('-', 3)
op('*', 4)
op('/', 5)

#creating special buttons
zerob= Button(root, text='0', font='20', height=2 ,width=10, command=partial(click, 0)).grid(row=5, column=1)
backspaceb = Button(root, text="Backspace", font='20', height=2 ,width=10, command=backspace).grid(row=5, column=2)
equalb= Button(root, text='=', font='20', height=2 ,width=10,command=equal).grid(row=5, column=0)
clearallb = Button(root, text="Clear All", font='20', height=2, width=43, command=clrall).grid(row=6, column=0, columnspan=4,)



root.mainloop()
