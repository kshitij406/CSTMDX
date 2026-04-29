from tkinter import *


root = Tk()
root.title('Label Frame')
root.geometry("700x300+100+100")

# creating Frame
label = LabelFrame(text="Frame", width=500, height=200)

# attach widget
label.pack(side=TOP, padx=40, pady=10)


root.mainloop()