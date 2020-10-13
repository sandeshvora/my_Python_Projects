import os
from tkinter import *
def Rename():
    folderpath=r''+path.get()
    counter =1
    for filename in os.listdir(folderpath):
        os.rename(folderpath+'\\'+filename,folderpath+'\\'+word.get()+str(counter)+'.'+ext.get())
        counter=counter+1
    ent.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)

root=Tk()
root.title('File Renamer')
root.geometry('300x250')
path=StringVar()

Label(root, text = 'Paste file Path', font=('TIMES NEW ROMAN',12)).pack()
ent= Entry(root,textvariable=path,font=('TIMES NEW ROMAN',12))
ent.pack()

word=StringVar()
Label(root, text = 'Give new file name', font=('TIMES NEW ROMAN',12)).pack()
ent2= Entry(root,textvariable=word,font=('TIMES NEW ROMAN',12))
ent2.pack()

ext=StringVar()
Label(root, text = 'Give Extension', font=('TIMES NEW ROMAN',12)).pack()
ent3= Entry(root,textvariable=ext,font=('TIMES NEW ROMAN',12))
ent3.pack()

Button(root,text='Change Name',command= Rename).pack()
root.mainloop()

