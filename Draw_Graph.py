import matplotlib.pyplot as plt
from process import process

def Draw_graph (process_list):
        S_T=list()
        D_T=list()
        I_D=list()
        for elem in process_list:
                S_T.append(elem.start)
                I_D.append(elem.pid)
                D_T.append((elem.finish-elem.start))
        # plotting a bar chart
        plt.bar(S_T, I_D,
                width = D_T, color = ['red', 'blue'], align="edge")

        # naming the x-axis
        plt.xlabel(' Time ')
        # naming the y-axis
        plt.ylabel(' Process Number ')
        # plot title
        plt.title(' Scheduling processes ')

        # function to show the plot
        plt.show()