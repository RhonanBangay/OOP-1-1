from tkinter import *
window = Tk()

window.geometry("400x500+30+20")
window.title("Welcome to Python Programming")


#add Button  widget

btn = Button(window,text = "Click me", fg="Blue")
btn.place(x=35, y=150)

#Add label  widget

lbl = Label(window, text="Student Personal Information",fg = "Blue", bg = "orange")
lbl.place(relx=.5,y=60,anchor="center")

lbl2= Label(window, text="Gender", fg ="red")
lbl2.place(x=50,y=190)

#text field widget

txtfd = Entry(window, bd=2,font=("verdana",15))
txtfd.place(x=100,y=150)

#add radio button

v1 = StringVar()
v2 = StringVar()
v1.set(1)


r1 = Radiobutton(window, text="Male", value =v1)
r1.place(x=50, y=220)

r2 = Radiobutton(window, text="Female",value =v2)
r2.place(x=200, y=220)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox = Checkbutton(window,text="Basketball", variable=v3)
chkbox2 = Checkbutton(window,text="Tennis", variable=v4)
chkbox3 = Checkbutton(window,text="Baseball", variable=v5)

lbl3 = Label(window, text="Sport",fg="red")
lbl3.place(x=50,y=250)
chkbox.place(x=50, y=300)
chkbox2.place(x=150, y=300)
chkbox3.place(x=220, y=300)

lbl4 = Label(window, text = "Course", fg="red")
lbl4.place(x=70, y=350, anchor ="center")

var = StringVar()
data1 = "BSCPE"
data2 = "BSCE"
data3 = "BSCS"
data4 = "BSIT"

lstbox = Listbox(window, height=5, selectmode="single")
lstbox.insert(END,data1,data2,data3,data4)
lstbox.place(x=50,y=365)

window.mainloop()