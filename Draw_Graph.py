from process import process
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def Draw_graph (process_list,root):
        S_T=list()
        D_T=list()
        I_D=list()
        for elem in process_list:
                S_T.append(elem.start)
                I_D.append(elem.pid)
                D_T.append((elem.finish-elem.start))
        # plotting a bar chart
        figure1 = Figure(figsize=(5, 4),dpi=100)
        subplot1 = figure1.add_subplot(111)
        subplot1.set_title(" graph")
        subplot1.set_xlabel(" Time")
        subplot1.set_ylabel(" Process_ID")
        subplot1.bar(S_T, I_D,width=D_T ,color='g', align="edge")
        bar1 = FigureCanvasTkAgg(figure1, root)

        return (bar1)



