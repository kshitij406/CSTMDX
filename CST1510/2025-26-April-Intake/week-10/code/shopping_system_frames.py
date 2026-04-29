from tkinter import *

root = Tk()
root.title('Sample solution for week 13')
root.geometry('750x520')

# ------------------------Main frame -----------------------------
left_frame = LabelFrame(master=root, relief = FLAT, borderwidth = 3, bg='light grey', width=400)
left_frame.grid(row=0, column=0, padx=5, pady=5)

# ------------------------Left frame -----------------------------
frame1_1 = LabelFrame(master=left_frame, relief = FLAT, borderwidth = 3, bg='light grey')
frame1_1.pack(padx=5, pady=5)
l1 = Label(master=frame1_1, text=f"Welcome")
l1.pack()

frame1_2 = LabelFrame(master=left_frame, relief = FLAT, borderwidth = 3, bg='light grey')
frame1_2.pack(padx=5, pady=5)
l1 = Label(master=frame1_2, text=f"Category1")
l1.grid(column=0, row=0, pady=5, padx=5)
l1 = Label(master=frame1_2, text=f"Category2")
l1.grid(column=1, row=0, pady=5, padx=5)


# ------------------------ All Items to display on left frame --------------------------------------
frame1_2 = LabelFrame(master=left_frame, text='Items', relief = RAISED, borderwidth = 3, bg='light grey')
frame1_2.pack(padx=5, pady=5)


for i in range(2):
    for j in range(4):
        frame = Frame(master = frame1_2,relief = RAISED,borderwidth = 3)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}", width=10, height=10)
        label.pack()

# ------------------------ Right side of the frame --------------------------------------
right_frame = LabelFrame(master=root, relief = RAISED, borderwidth = 3,bg='light grey')
right_frame.grid(row=0, column=1, padx=5, pady=5)

frame2_1 = LabelFrame(master=right_frame, text='order', relief = FLAT, borderwidth = 3, bg='light grey')
frame2_1.pack(padx=5, pady=5)


# --------------------- Basket ---------------------------------
l2 = Label(master=frame2_1, text=f"Current Order", width=20, height=2)
l2.pack()

frame2_2 = LabelFrame(master=right_frame, relief = FLAT, borderwidth = 3, bg='light grey')
frame2_2.pack(padx=5, pady=5)

l2 = Label(master=frame2_2, text=f"Discount code:")
l2.grid(column=0, row=0)
l2 = Label(master=frame2_2, text=f" CODE0000001 ")
l2.grid(column=1, row=0)

frame2_3 = LabelFrame(master=right_frame, text='ordered item', relief = FLAT, borderwidth = 3, bg='light grey')
frame2_3.pack(padx=5, pady=5)
l2 = Label(master=frame2_3, text=f"Row {0}\nColumn {1}")
l2.pack()
l2 = Label(master=frame2_3, text=f"Row {0}\nColumn {1}")
l2.pack()
l2 = Label(master=frame2_3, text=f"Row {0}\nColumn {1}")
l2.pack()

frame2_4 = LabelFrame(master=right_frame, text='order_text', relief = FLAT, borderwidth = 3, bg='light grey')
frame2_4.pack(padx=5, pady=5)

order = '''
Subtotal:\t\t 37.61
Discount sales:\t5.00
Total sale tax:\t2.25
------------------------------------
TOTAL:\t34.86'''

l2 = Label(master=frame2_4, text=order)
l2.pack()

frame2_5 = LabelFrame(master=right_frame,text='Payment: ', relief = FLAT, borderwidth = 3, bg='light grey')
frame2_5.pack(padx=5, pady=5)

l2 = Label(master=frame2_5, text=f"Continue to payment")
l2.pack()


root.mainloop()