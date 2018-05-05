from Tkinter import *

import tkFileDialog

import tkMessageBox

from tkColorChooser import askcolor

import datetime

import webbrowser

from tkFileDialog import askopenfilename, asksaveasfilename





def line():

    lin = "_" * 60

    text.insert(INSERT,lin)

    

def date():

    data = datetime.date.today()

    text.insert(INSERT,data)

   

def normal():

    text.config(font = ("Arial", 10))



def bold():

    text.config(font = ("Arial", 10, "bold"))



def underline():

    text.config(font = ("Arial", 10, "underline"))



def italic():

    text.config(font = ("Arial",10,"italic"))

    

def font():

    (triple,color) = askcolor()

    if color:

       text.config(foreground=color)



def kill():

    root.destroy()



def about():

    pass



def opn():

    text.delete(1.0 , END)

    file = open(askopenfilename() , 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT,txt)

    else:

        pass

    

def save():

    filename = asksaveasfilename()

    if filename:

        alltext = text.get(1.0, END)                      

        open(filename, 'w').write(alltext) 



def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 



def paste():

    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Error Nothing to paste ")



def clear():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)



def clearall():

    text.delete(1.0 , END)



def background():

    (triple,color) = askcolor()

    if color:

       text.config(background=color)

       

def about():

    ab = Toplevel(root)

    txt = "Raghav tiwari text editor "

    la = Label(ab,text=txt,foreground='blue')

    la.pack()




root = Tk()

root.title("Notepad")

menu = Menu(root)



filemenu = Menu(root)

root.config(menu = menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="open", command=opn)

filemenu.add_command(label="Save", command=save)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=kill)



modmenu = Menu(root)

menu.add_cascade(label="Modify",menu = modmenu)

modmenu.add_command(label="Copy", command = copy)

modmenu.add_command(label="paste", command=paste)

modmenu.add_separator()

modmenu.add_command(label = "Clear", command = clear)

modmenu.add_command(label = "clearall", command = clearall)







insmenu = Menu(root)

menu.add_cascade(label="insert",menu= insmenu)

insmenu.add_command(label="Date",command=date)

insmenu.add_command(label="Line",command=line)







        

formatmenu = Menu(menu)

menu.add_cascade(label="Format",menu = formatmenu)

formatmenu.add_cascade(label="Color", command = font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normal',command=normal)

formatmenu.add_radiobutton(label='bold',command=bold)

formatmenu.add_radiobutton(label='underline',command=underline)

formatmenu.add_radiobutton(label='italic',command=italic)



persomenu = Menu(root)

menu.add_cascade(label="Personalize",menu=persomenu)

persomenu.add_command(label="background", command=background)

                 

helpmenu = Menu(menu)

menu.add_cascade(label="help", menu=helpmenu)

helpmenu.add_command(label="Info", command=about)


text = Text(root, height=30, width=60, font = ("Arial", 10))









scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)                  

text.config(yscrollcommand=scroll.set)           

scroll.pack(side=RIGHT, fill=Y)

text.pack()





root.resizable(0,0)

root.mainloop()
