from process import process

def print_p(pList, avg_tat, avg_wtat, algo):
    #pList.sort(key = lambda x: (x.pid), reverse = False)
    with open("output_" + algo + ".txt", "w") as outp:

        for i in range(len(pList)):
            outp.write("P_id\t" + str(pList[i].pid) + "\tWaiting time\t" + str(pList[i].wait)+ "\tTurnaround time\t" + str(pList[i].tat) + "\tWeighted Turnaround time\t" + str(pList[i].wtat) + '\n')

        outp.write("\nAverage Turnaround time is " + str(avg_tat) + '\n')
        outp.write("Average Weighted turnaround time is " + str(avg_wtat) + '\n')