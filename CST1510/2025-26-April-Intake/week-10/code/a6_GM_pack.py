from tkinter import *

root1 = Tk()
root1.title('no 1')

frame1 = LabelFrame(master=root1, width=100, height=20, bg='light blue')
frame1.pack()
frame2 = LabelFrame(master=root1, width=100, height=20, bg='blue')
frame2.pack()
frame3 = LabelFrame(master=root1, width=100, height=20, bg='dark blue')
frame3.pack()

root1.mainloop()

'''
You can set the fill argument in order to specify in which direction you want the frames should fill. 
If you want to fill in the horizontal direction then the option is tk.X, whereas, 
tk.Y is used to fill vertically, and to fill in both directions tk.BOTH is used.
'''
root2 = Tk()
root2.title('no 2')
frame1 = Frame(master=root2, width=100, height=20, bg='light blue')
frame1.pack(fill=X)
frame2 = Frame(master=root2, width=100, height=20, bg='blue')
frame2.pack(fill=X)
frame3 = Frame(master=root2, width=100, height=20, bg='dark blue')
frame3.pack(fill=X)

root2.mainloop()




'''The side and, expand attributs 
In the below example you can see this output is able to expand in both directions.
'''
root3 = Tk()
root3.title('no 3')
frame1 = Frame(master=root3, width=100, height=20, bg='light blue')
frame1.pack(fill=BOTH, side=LEFT, expand=True)
frame2 = Frame(master=root3, width=100, height=20, bg='blue')
frame2.pack(fill=BOTH, side=LEFT, expand=True)
frame3 = Frame(master=root3, width=100, height=20, bg='dark blue')
frame3.pack(fill=BOTH, side=LEFT, expand=True)


root3.mainloop()