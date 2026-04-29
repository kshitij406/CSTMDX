from tkinter import *

window1 = Tk()
window1.title('grid 1 ')

frame1 = LabelFrame(master=window1, width=50, height=50, bg='light blue')
frame1.grid(row=0, column=0, padx=5, pady=5)
frame2 = LabelFrame(master=window1, width=50, height=50, bg='blue')
frame2.grid(row=0, column=1, padx=5, pady=5)
frame3 = LabelFrame(master=window1, width=50, height=50, bg='dark blue')
frame3.grid(row=1, column=0, padx=5, pady=5)
frame3 = LabelFrame(master=window1, width=50, height=50, bg='light blue')
frame3.grid(row=1, column=1, padx=5, pady=5)
window1.mainloop()


'''Example of a grid where at each cell is a label pack in '''
window2 = Tk()
window2.title('grid 2 ')

frame1 = LabelFrame(master=window2, relief = RAISED, borderwidth = 3, bg='light blue')
frame1.grid(row=0, column=0, padx=5, pady=5)
l1 = Label(master=frame1, text=f"Row {0}\nColumn {0}")
l1.pack()

frame2 = LabelFrame(master=window2, width=50, height=50, bg='blue')
frame2.grid(row=0, column=1, padx=5, pady=5)
l2 = Label(master=frame2, text=f"Row {0}\nColumn {1}")
l2.pack()

frame3 = LabelFrame(master=window2, width=50, height=50, bg='dark blue')
frame3.grid(row=1, column=0, padx=5, pady=5)
l2 = Label(master=frame3, text=f"Row {1}\nColumn {1}")
l2.pack()

frame4 = LabelFrame(master=window2, width=50, height=50, bg='light blue')
frame4.grid(row=1, column=1, padx=5, pady=5)
l3 = Label(master=frame4, text=f"Row {1}\nColumn {1}")
l3.pack()

window2.mainloop()


window = Tk()
window.title('grid 3 ')
for i in range(5):
    for j in range(3):
        frame = Frame(master = window,relief = RAISED,borderwidth = 3)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()