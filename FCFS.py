from process import process
from print_p import print_p
from Draw_Graph import Draw_graph
def get_data(inputfile,cst):
    with open(inputfile, "r") as input:
        in_arr = input.read().split()
    process_queue=list()
    k=1
    for i in range (0,len(in_arr)/4):
        # process id     # process arrival time         # process brust time     # process priority
        process_queue.append(process(int(in_arr[k]),float(in_arr[k+1]),float(in_arr[k+2]), int(in_arr[k+3])))
        k+=4
    return (process_queue)

def FCFS(process_queue,cst):
    num= len(process_queue)
    #sort the list of processes according to arrival time
    process_queue.sort(key=lambda x: x.arrival, reverse=False)
    #calculate Wait time ,turnaround time, weighted turnaround time
    avg_tat=0
    avg_wtat=0
    for i in range (0,num):
        if i==0:
            process_queue[i].start = process_queue[i].arrival
        else:
            process_queue[i].start = process_queue[i-1].finish
            if process_queue[i-1].finish < process_queue[i].arrival :
                process_queue[i].start = process_queue[i].arrival
        process_queue[i].start += cst
        process_queue[i].finish=process_queue[i].start+process_queue[i].running
        process_queue[i].wait=process_queue[i].start-process_queue[i].arrival
        process_queue[i].tat = process_queue[i].wait + process_queue[i].running  # wait time+ burst time
        process_queue[i].wtat = process_queue[i].tat / process_queue[i].running  # turnaroundtime/burst time
        avg_tat += process_queue[i].tat
        avg_wtat += process_queue[i].wtat

    print_p(process_queue, avg_tat, avg_wtat, "FCFS")
    return process_queue

p = get_data("3",1)
List = FCFS(p,1)
Draw_graph(List)
