from copy import deepcopy
from process import process
from print_p import print_p
def update_queue(process_list,process_queue,t): # list hya aslya w ally hy7t feha hya process_queue

    for i in range (0,len(process_list)):
        if (((process_list[i].arrival)<=t) and (not(process_list[i].arrival)==-1)):
            process_queue.insert(len(process_queue),deepcopy(process_list[i]))
            process_list[i].arrival=-1 # flag to indicate that this process is already executed or listed
    process_queue.sort( key=lambda x: (x.arrival), reverse=False)
    return(process_queue)

def FCFS(process_list,cst):
    num= len(process_list)
    # the program always start at arrival time of 1st process
    Current_Time = min(process_list, key=lambda x: x.arrival).arrival

    #calculate Wait time ,turnaround time, weighted turnaround time
    avg_tat=0
    avg_wtat=0
    process_queue = list()
    step=0.0001
    i=0
    lst_id =-1
    while i < num:
        process_queue = update_queue(process_list, process_queue, Current_Time)
        if (lst_id == process_queue[-1].pid):
            Current_Time += step
        else:
            process_queue[i].start = Current_Time
            if process_queue[i-1].finish < process_queue[i].arrival :
                process_queue[i].start = process_queue[i].arrival
            process_queue[i].start += cst
            process_queue[i].finish=process_queue[i].start+process_queue[i].running
            process_queue[i].wait=process_queue[i].start - process_queue[i].arrival
            process_queue[i].tat = process_queue[i].wait + process_queue[i].running  # wait time+ burst time
            process_queue[i].wtat = process_queue[i].tat / process_queue[i].running  # turnaroundtime/burst time
            avg_tat += process_queue[i].tat
            avg_wtat += process_queue[i].wtat
            Current_Time = process_queue[i].finish
            lst_id = process_queue[i].pid
            i+=1
    avg_tat /=num
    avg_wtat /= num
    print_p(process_queue, avg_tat, avg_wtat, "FCFS")
    return process_queue

