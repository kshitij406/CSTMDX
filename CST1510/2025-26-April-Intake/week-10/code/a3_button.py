from tkinter import *

root = Tk()
root.title('Label')
root.geometry("300x100+350+250")


def button_func():
    print('Click!')

# creating widgets
label = Label(root, text = "Press the button: ")
button = Button(root, text = "Button", bg='light gray', relief=RAISED, command=button_func)

# attaching widgets
label.pack(side=LEFT, padx=5, pady=10)
button.pack(side=LEFT, padx=5, pady=10)


root.mainloop()



