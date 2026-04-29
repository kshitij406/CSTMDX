from tkinter import *

root = Tk()
root.title('Image example when the image is in another file')
root.geometry("250x100+250+350")
photo = PhotoImage(file='netflix.png')
photo_label = Label(root, image=photo)
label = Label(root, text='Well done', justify=LEFT, font=('Braggadocio', 20, 'bold'))


photo_label.grid(row=0, column=0)
label.grid(row=0, column=1)

root.mainloop()


# =================== Image scaled =============================
from tkinter import *

root = Tk()
root.title('Image example when the image is in another file')
root.geometry("250x100+250+350")
photo = PhotoImage(file='like.gif')
photo = photo.subsample(2,2)
photo_label = Label(root, image=photo)


label = Label(root, text='Well done', justify=LEFT, font=('Braggadocio', 20, 'bold'))

photo_label.grid(row=0, column=0)
label.grid(row=0, column=1)

root.mainloop()




