from tkinter import *
win = Tk()

win.geometry("600x300")
win.resizable(0,0)
win.title("Midterm in OOP")

Lbl=Label(win, text="Enter your fullname:", fg="Red")
Lbl.place(x=50, y=100)

s1=StringVar()
s2=StringVar()

def Click():
    s2.set(s1.get())
Ent1=Entry(win,font=("verdana",15), width=20, bd=5, textvariable=s1)
Ent1.place(x=300, y=100)

Ent2=Entry(win,font=("verdana",15),width=20, bd=5, textvariable=s2)
Ent2.place(x=300, y=150)

Btn=Button(win, text="Click to display your Fullname", fg="Red", command=lambda:Click())
Btn.place(x=50, y=150)

win.mainloop()