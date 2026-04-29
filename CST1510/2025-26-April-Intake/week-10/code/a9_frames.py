from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("700x500+100+100")



def button_clicked():
        showinfo(title='Information',
                 message='Hello, Tkinter!')

frame1 = LabelFrame(root)
frame1.place(x=100, y=50)

# label
label = Label(frame1, text='Hello, Tkinter!')
label.pack(padx = 5, pady=5)

# button
button = Button(frame1, text='Click Me')
button['command'] = button_clicked # another way of adding command on batton
button.pack(padx = 5, pady=5)

# show the frame on the container

root.mainloop()