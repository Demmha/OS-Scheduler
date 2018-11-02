from tkinter import *

def onvalue_change(self):
    if algo.get() == OPTIONS[2]:
        L4.pack()
        E4.pack()
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
    except Exception as error:
            messagebox.showerror("Error", repr(error))

window = Tk()
window.title("Os scheduler")
window.geometry("300x250")

L1 = Label(window, text="Input File Name").pack()

filename = StringVar()
E1 = Entry(window, textvariable = filename).pack()

L2 = Label(window, text="Choose Algorithm").pack()

OPTIONS = ["HPF", "FCFS", "RR", "SRTN"]

algo = StringVar(window)
algo.set(OPTIONS[0])

algolist = OptionMenu(window, algo, *OPTIONS, command = on_value_change).pack()

L3 = Label(window, text="Context Switching Time").pack()

t1 = StringVar()
E2 = Entry(window, textvariable = t1).pack()

t2 = StringVar()
L4 = Label(window, text="Time Quantum")
E4 = Entry(window, textvariable = t2)

b1 = Button(window, text ="Done", command = validate).pack(side = BOTTOM)

window.mainloop()