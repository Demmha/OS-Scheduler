import numpy as np
from copy import deepcopy
from process import process
from print_p import print_p

def update_queue(process_list,process_queue,t): # list hya aslya w ally hy7t feha hya process_queue
    for i in range (0,len(process_list)):
        if (((process_list[i].arrival)<=t) and (not(process_list[i].arrival)==-1)):
            process_queue.insert(len(process_queue),deepcopy(process_list[i]))
            process_list[i].arrival =-1 # flag to indicate that this process is already executed or listed
    process_queue.sort(key=lambda x: (x.remaining), reverse=False)
    return(process_queue)


def SRTF(process_list,cst):
    num=len(process_list)
    #sort the array of processes according to arrival time and running time
    process_list.sort(key=lambda x: (x.arrival,x.running), reverse=False)

    # the program always start at arrival time of 1st process
    Current_Time = process_list[0].arrival
    Current_Process=list()
    process_queue=list() # process sequence of execution

    complete=0
    i=0
    l_id=0
    s_t = np.array([-1 for i in range (0,num+1)])
    f_t = np.array([0 for i in range (0,num+1)])
    step=0.0001
    #assume in this algorithm check every 1 min
    while complete != num :
        process_queue = update_queue(process_list,process_queue,Current_Time)
        if len(process_queue)>0 :
            if process_queue[0].pid != l_id : # check if process changed or not
                Current_Time+= cst
                if s_t[process_queue[0].pid]==-1: # check if this process start before or not
                    s_t[process_queue[0].pid]=Current_Time
                process_queue[0].start = Current_Time
                Current_Process.insert(i, deepcopy(process_queue[0]))
                l_id = process_queue[0].pid
                i+=1

            process_queue[0].remaining-=step
            if (process_queue[0].remaining <=0):
                f_t[process_queue[0].pid] = Current_Time+step
                complete+=1
                process_queue.remove(process_queue[0])

            Current_Process[len(Current_Process)-1].finish = Current_Time+step
        Current_Time+=step

    avg_tat=0
    avg_wtat=0
    for i in range (0,len(process_list)) :
        process_list[i].tat = f_t[process_list[i].pid] - process_list[i].arrival  # wait time = start time - arrival
        process_list[i].wait = process_list[i].tat - process_list[i].running  # tat = wait time + brust
        process_list[i].wtat= process_list[i].tat/ process_list[i].running #turnaroundtime/burst time
        avg_tat+=process_list[i].tat
        avg_wtat+=process_list[i].wtat

    #calculate Average turnaround time of schedule
    avg_tat/= num
    #calculate Average weightturnaround time of schedule
    avg_wtat/=num

    print_p(process_list, avg_tat, avg_wtat, "SRTF")
    return(Current_Process)


