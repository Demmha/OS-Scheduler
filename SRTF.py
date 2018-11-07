import numpy as np
from collections import deque
from copy import deepcopy
from process import process


def update_queue(process_list,process_queue,t): # list hya aslya w ally hy7t feha hya process_queue
    for i in range (0,len(process_list)):
        if (((process_list[i].arrival)<=t) and (not(process_list[i].arrival)==-1)):
            process_queue.insert(len(process_queue),deepcopy(process_list[i]))
            process_list[i].arrival =-1 # flag to indicate that this process is already executed or listed
    process_queue.sort(key=lambda x: (x.remaining), reverse=False)
    return(process_queue)

inputfile = raw_input("input file name: ")
outputfile = raw_input("output file name: ")
Context_Switch_Time = int(raw_input("Context Switch Time: "))
with open(inputfile, "r") as input:
    in_arr = input.read().split()

num = int(in_arr[0]) #number of processes
process_list=list() # process list
k=1
R_T= np.zeros(num+1)  # Remaining brust time of each process
F_T= np.zeros(num+1)  # finished time
for i in range (0,num):
    # process id     # process arrival time         # process brust time     # process priority
    process_list.append(process(int(in_arr[k]),float(in_arr[k+1]),float(in_arr[k+2]), int(in_arr[k+3])))
    k+=4


#sort the array of processes according to arrival time and priority
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
# assume in this algorithm check every 1 min
while complete != num :
    print("at time = "+str(Current_Time))
    process_queue = update_queue(process_list,process_queue,Current_Time)
    print("p"+str (process_queue[0].pid))

    if len(process_queue)>0 :
        if process_queue[0].pid != l_id : # check if process changed or not
            if s_t[process_queue[0].pid]==-1: # check if this process start before or not
                s_t[process_queue[0].pid]=Current_Time
            Current_Process.insert(i, deepcopy(process_queue[0]))
            l_id = process_queue[0].pid
            i+=1
        process_queue[0].remaining-=1
        if (process_queue[0].remaining ==0):
            f_t[process_queue[0].pid] = Current_Time+1
            complete+=1
            process_queue.remove(process_queue[0])
    Current_Time+=1

AverageTurnaroundTime=0
AverageWaitedTurnaroundTime=0
for i in range (0,len(process_list)) :
    process_list[i].wait = f_t[process_list[i].pid] - s_t[process_list[i].pid] + Context_Switch_Time  # start - finish + context switching
    process_list[i].tat= process_list[i].wait+ process_list[i].running # wait time+ burst time
    process_list[i].wtat= process_list[i].tat/ process_list[i].running #turnaroundtime/burst time
    AverageTurnaroundTime+=process_list[i].tat
    AverageWaitedTurnaroundTime+=process_list[i].wtat

#calculate Average turnaround time of schedule
AverageTurnaroundTime= AverageTurnaroundTime/num
#calculate Average weightturnaround time of schedule
AverageWaitedTurnaroundTime= AverageWaitedTurnaroundTime/num


with open(outputfile, "w") as output:
    output.write('ProcessID\tWaitingTime\tTurnaroundTime\tWaitedturnaroundTime\n ')
    for i in range (0,num):
        output.write(str(int(process_list[i].pid))+' '+str(process_list[i].wait)+'  '+str(process_list[i].tat)+'  '+str(process_list[i].wtat)+ '\n ')
    output.write("Average TurnaroundTime of Schedule = "+str(AverageTurnaroundTime)+ '\n ')
    output.write("Average WaitedTurnaroundTime of Schedule = "+str(AverageWaitedTurnaroundTime)+ '\n ')
    output.close()


