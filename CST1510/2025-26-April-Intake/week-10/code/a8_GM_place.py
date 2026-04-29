from tkinter import *
window = Tk()
window.geometry("400x250")

Username = Label(window, text = "Username")
Username.place(x = 30,y = 50)
email = Label(window, text = "Email").place(x = 30, y = 90)
password = Label(window, text = "Password").place(x = 30, y = 130)

e1 = Entry(window).place(x = 80, y = 50)
e2 = Entry(window).place(x = 80, y = 90)
e3 = Entry(window).place(x = 95, y = 130)

window.mainloop()