from tkinter import *
from tkinter import messagebox
from get_data import get_data
from HPF import HPF
from FCFS import FCFS
from RR import RR
from SRTF import SRTF
from Draw_Graph import Draw_graph
from tkinter import S as nw

def onvalue_change(self):
    if algo.get() == OPTIONS[2]:
        L4.pack()
        E4.pack(anchor=nw)
    else:
        L4.pack_forget()
        E4.pack_forget()


def val_(val):
    try:
        val = float(val)
        if val < 0:
            return 0
        return 1
    except ValueError:
        return 0


def validate():
    try:
        if len(filename.get()) == 0:
            raise IOError("please choose an input file")
        if val_(t1.get()) == 0:
            raise ValueError("Enter a reasonable Context Switching time")
        if (algo.get() == OPTIONS[2]) and (val_(t2.get()) == 0):
            raise ValueError("Enter a reasonable Time Quantum")
        return True
    except Exception as error:
        messagebox.showerror("Error", repr(error))
        return False



def run():
    if not validate():
        return
    pList = get_data(filename.get())
    if algo.get() == OPTIONS[0]:
        List = HPF(pList, float(t1.get()))
    if algo.get() == OPTIONS[1]:
        List = FCFS(pList, float(t1.get()))
    if algo.get() == OPTIONS[2]:
        List = RR(pList, float(t2.get()), float(t1.get()))
    if algo.get() == OPTIONS[3]:
        List = SRTF(pList, float(t1.get()))
    bar1=Draw_graph(List,canvas1)
    bar1.get_tk_widget().pack(fill=BOTH, expand=1)
def reset():
    List=list()
    bar1=bar1=Draw_graph(List,canvas1)
    bar1.get_tk_widget().pack(fill=BOTH, expand=1)


window = Tk()
window.title("Os scheduler")
window.geometry("700x300")
canvas1 = Canvas(window, width=300, height=300)
canvas1.pack(side=RIGHT )

L1 = Label(window,pady=10,text="Input File Name").pack(anchor=nw)

filename = StringVar()
E1 = Entry(window, textvariable = filename).pack(anchor=nw)

L2 = Label(window,pady=10, text="Choose Algorithm").pack(anchor=nw)

OPTIONS = ["HPF", "FCFS", "RR", "SRTN"]
#############################################################33
algo = StringVar(window)
algo.set(OPTIONS[0])

algolist = OptionMenu(window, algo, *OPTIONS, command = onvalue_change).pack(anchor=nw)
#################################################################
'''
v=IntVar()

frame=Frame(window)
frame.pack()
Radiobutton(frame,
              text="HPF",
              padx = 10,
              variable=v,
              value=1).pack(anchor=W,side=LEFT)
Radiobutton(frame,
              text="FCFS",
              padx = 10,
              variable=v,
              value=2).pack(anchor=W,side=LEFT)
Radiobutton(frame,
              text="RR",
              padx = 10,
              variable=v,
              value=3).pack(anchor=W,side=LEFT)
Radiobutton(frame,
              text="SRTF",
              padx = 10,
              variable=v,
              value=4).pack(anchor=W,side=LEFT)
'''
########################################################33
L3 = Label(window,pady=10, text="Context Switching Time").pack()

t1 = StringVar()
E2 = Entry(window, textvariable = t1).pack(anchor=nw)

t2 = StringVar()
L4 = Label(window,pady=10, text="Time Quantum")
E4 = Entry(window,textvariable = t2)

b1 = Button(relief= GROOVE,text ="DONE",padx=10,command = run).pack(anchor=nw)


#b2 = Button(relief= GROOVE,text ="RESET",padx=10,justify=LEFT,command = reset).pack()
#canvas1.create_window(200,320,window=b2)
window.mainloop()