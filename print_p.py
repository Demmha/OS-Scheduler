from process import process

def print_p(pList, avg_tat, avg_wtat, algo):
    with open("output_" + algo + ".txt", "w") as outp:
        outp.write("P_id\tWaiting time\tTurnaround time\tWeighted Turnaround time\n")

        for i in range(len(pList)):
            outp.write(str(pList[i].pid) + '\t' + str(pList[i].wait)+ '\t' + str(pList[i].tat) + '\t' + str(pList[i].wtat) + '\n')

        outp.write("\nAverage Turnaround time is " + str(avg_tat) + '\n')
        outp.write("Average Weighted turnaround time is " + str(avg_wtat) + '\n')