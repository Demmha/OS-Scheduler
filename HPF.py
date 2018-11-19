import numpy as np
from copy import deepcopy
from process import process
from print_p import print_p

def update_queue(process_list,process_queue,t): # list hya aslya w ally hy7t feha hya process_queue

    for i in range (0,len(process_list)):
        if (((process_list[i].arrival)<=t) and (not(process_list[i].arrival)==-1)):
            process_queue.insert(len(process_queue),deepcopy(process_list[i]))
            process_list[i].arrival=-1 # flag to indicate that this process is already executed or listed
    process_queue.sort( key=lambda x: (x.priority,-x.pid), reverse=True)
    return(process_queue)

def HPF (process_list,cst):
    num=len(process_list)
    #sort the array of processes according to arrival time and priority
    process_list.sort(key=lambda x: (-x.arrival,x.priority), reverse=True)
    # the program always start at arrival time of 1st process
    Current_Time = process_list[0].arrival

    Current_Process=list() # process sequence of execution
    process_queue=list()
    avg_tat = 0
    avg_wtat = 0
    complete = 0
    while complete != num:
        process_queue= update_queue(process_list, process_queue, Current_Time)
        if(len(process_queue)==0):
            Current_Time =  process_list[complete].arrival
        else:
            Current_Process.insert(complete, deepcopy(process_queue[0]))
            Current_Process[complete].start=Current_Time+cst
            process_queue.remove(process_queue[0])
            Current_Time += Current_Process[complete].running+cst
            Current_Process[complete].finish = Current_Time

            # calculate Wait time ,turnaround time, weighted turnaround time
            Current_Process[complete].wait = Current_Process[complete].start - Current_Process[complete].arrival  # wait time = start time - arrival time
            Current_Process[complete].tat = Current_Process[complete].wait + Current_Process[complete].running  # wait time+ burst time
            Current_Process[complete].wtat = Current_Process[complete].tat / Current_Process[complete].running  # turnaroundtime/burst time
            avg_tat += Current_Process[complete].tat
            avg_wtat += Current_Process[complete].wtat
            complete += 1
    #calculate Average turnaround time of schedule
    avg_tat/= num
    #calculate Average weightturnaround time of schedule
    avg_wtat/=num
    print_p(Current_Process, avg_tat, avg_wtat, "HPF")
    return (Current_Process)