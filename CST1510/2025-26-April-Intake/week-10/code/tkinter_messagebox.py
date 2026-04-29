from tkinter import messagebox

messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")


answer = messagebox.askokcancel("Question","Do you want to open this ?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")

if answer == True:
    print('Yeah me too!!')
elif answer == False:
    print('Thank you for visiting us!!')
elif answer == None:
    print('Good bye!!')

