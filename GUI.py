
import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
from get_data import get_data
from HPF import HPF
from FCFS import FCFS
from RR import RR
from SRTF import SRTF

def check(*args):

    if v.get()==3:
        L4.pack()
        E4.pack()
    else:
        L4.pack_forget()
        E4.pack_forget()


class App:
    # S_T = list()
    # D_T = list()
    # I_D = list()


    def val_(self,val):
        try:
            val = float(val)
            if val < 0:
                return 0
            return 1
        except ValueError:
            return 0

    def validate(self):
        try:
            if len(self.filename.get()) == 0:
                raise IOError("please choose an input file")
            if self.val_(self.t1.get()) == 0:
                raise ValueError("Enter a reasonable Context Switching time")
            if (v.get()==3) and (self.val_(self.t2.get()) == 0):
                raise ValueError("Enter a reasonable Time Quantum")
            return True
        except Exception as error:
            messagebox.showerror("Error", repr(error))
            return False

    def run(self):
        if not self.validate():
            return
        pList = get_data(self.filename.get())
        if v.get()==1:
            List = HPF(pList, float(self.t1.get()))
        if v.get()==2:
            List = FCFS(pList, float(self.t1.get()))
        if v.get()==3:
            List = RR(pList, float(self.t2.get()), float(self.t1.get()))
        if v.get()==4:
            List = SRTF(pList, float(self.t1.get()))
        self.decrease(List)


    def __init__(self, master):
        # Create a container
        self.first=True
        self.master=master
        self.frame = Tkinter.Frame(master)

        self.L1 = Tkinter.Label(self.master, pady=10, text="Input File Name").pack()

        self.filename = Tkinter.StringVar()
        self.E1 = Tkinter.Entry(self.master, textvariable=self.filename).pack()
        global v
        self.L2 = Tkinter.Label(self.master, pady=10, text="Context Switching Time").pack()
        self.t1 = Tkinter.StringVar()
        self.E2 = Tkinter.Entry(self.master, textvariable=self.t1).pack()
        self.L3 = Tkinter.Label(self.master, pady=10, text="Choose Algorithm").pack()
        v=Tkinter.IntVar()
        Tkinter.Radiobutton(self.frame,
                    text="HPF",
                    padx=10,
                    variable=v,
                    value=1).pack(side=Tkinter.LEFT)
        Tkinter.Radiobutton(self.frame,
                    text="FCFS",
                    padx=10,
                    variable=v,
                    value=2).pack(side=Tkinter.LEFT)
        Tkinter.Radiobutton(self.frame,
                    text="RR",
                    padx=10,
                    variable=v,
                    value=3).pack(side=Tkinter.LEFT)
        Tkinter.Radiobutton(self.frame,
                    text="SRTF",
                    padx=10,
                    variable=v,
                    value=4).pack(side=Tkinter.LEFT)

        v.trace('w', check)
        global E4,L4, t2
        self.frame2 = Tkinter.Frame(master)
        self.t2 = Tkinter.StringVar()
        L4 = Tkinter.Label(self.frame2, pady=10, text="Time Quantum")
        E4 = Tkinter.Entry(self.frame2, textvariable=self.t2)
        self.b1 = Tkinter.Button(self.frame2,relief= Tkinter.GROOVE, text="DONE", padx=10, command=self.run).pack(side=Tkinter.BOTTOM)
        self.frame.pack()
        self.frame2.pack()


    def Draw(self,S_T,D_T,I_D):
        window.geometry("800x600")
        fig = Figure(figsize=(5, 4),dpi=100,edgecolor='blue')
        self.subplot1 = fig.add_subplot(111)
        self.subplot1.set_title(" graph")
        self.subplot1.set_xlabel(" Time")
        self.subplot1.set_ylabel(" Process_ID")
        self.subplot1.bar(S_T, I_D,width=D_T, color=('purple'), align="edge")
        self.canvas = FigureCanvasTkAgg(fig,master=self.master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='right', fill='both', expand=1)
        self.first=False

    def decrease(self,process_list):
        S_T = list()
        D_T = list()
        I_D = list()
        for elem in process_list:
            S_T.append(elem.start)
            I_D.append(elem.pid)
            D_T.append((elem.finish - elem.start))
        if self.first:
           self.Draw(S_T,D_T,I_D)
        else:
            self.subplot1.clear()
            self.subplot1.bar(S_T, I_D, width=D_T, color=('blue'), align="edge")
            self.canvas.draw()


window = Tkinter.Tk()
window.title("Os scheduler")
window.geometry("300x300")
app = App(window)
window.mainloop()