from process import process
from print_p import print_p

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
