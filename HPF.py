import numpy as np
from collections import deque
from copy import deepcopy

def update_queue(process_list,process_queue,t): # list hya aslya w ally hy7t feha hya process_queue

    for i in range (0,len(process_list)):
        if (((process_list[i][1])<=t) and (not(process_list[i][1])==-1)):
            process_queue.insert(len(process_queue),deepcopy(process_list[i]))
            process_list[i][1]=-1 # flag to indicate that this process is already executed or listed
    process_queue = list((sorted(process_queue, key=lambda x: (x[3]), reverse=True)))
    return(process_queue)

inputfile = raw_input("input file name: ")
outputfile = raw_input("output file name: ")
Context_Switch_Time = int(raw_input("Context Switch Time: "))
with open(inputfile, "r") as input:
    in_arr = input.read().split()

num = int(in_arr[0]) #number of processes
process_list=list() # process list
k=1
for i in range (0,num):
    # process id     # process arrival time         # process brust time     # process priority
    process_list.insert(i,[int(in_arr[k]),float(in_arr[k+1]),float(in_arr[k+2]), int(in_arr[k+3])])
    k+=4
#sort the array of processes according to arrival time and priority
process_list=(sorted(process_list, key=lambda x: (-x[1],x[3]), reverse=True))
# the program always start at arrival time of 1st process
Current_Time = process_list[0][1]
Current_Process=np.zeros([num,4],dtype=float) # process sequence of execution
process_queue=list()
complete=0
while(not(complete==num)):
    process_queue = update_queue(process_list, process_queue, Current_Time)
    if (not(len(process_queue)==0)):
        Current_Process[complete]= deepcopy(process_queue[0])
        print(Current_Process[complete])
        process_queue.remove(process_queue[0])
        Current_Time += Current_Process[complete][2]
        complete+=1
    else:
        Current_Time+=1
 # waiting time of each process
WaitTime=np.zeros(num,dtype=float)
# Turnaround time of each process
TurnaroundTime=np.zeros(num,dtype=float)
# Waitedturnaround time of each process
WaitedTurnaroundTime=np.zeros(num,dtype=float)
#calculate Wait time ,turnaround time, weighted turnaround time
for i in range (0,len(Current_Process)):
    if (not (i == 0)):  # as first process may not came at t=0 but whenever it come it will serve immediately
        WaitTime[i] = WaitTime[i-1] + Current_Process[i - 1][2]- Current_Process[i][1]  # waiting time of previous one and burst time of it
    if (WaitTime[i] < 0):  # as if a process came and processor was free so it will start immediatly after Context Switching time
        WaitTime[i] = 0
    WaitTime[i] += Context_Switch_Time
    TurnaroundTime[i]= WaitTime[i]+ Current_Process[i][2] # wait time+ burst time
    WaitedTurnaroundTime[i]=TurnaroundTime[i]/Current_Process[i][2] #turnaroundtime/burst time
#calculate Average turnaround time of schedule
AverageTurnaroundTime= np.sum(TurnaroundTime)/num
#calculate Average weightturnaround time of schedule
AverageWaitedTurnaroundTime= sum(WaitedTurnaroundTime)/num


with open(outputfile, "w") as output:
    output.write('ProcessID\tWaitingTime\tTurnaroundTime\tWaitedturnaroundTime\n ')
    for i in range (0,num):
        output.write(str(int(Current_Process[i][0]))+' '+str(WaitTime[i])+'  '+str(TurnaroundTime[i])+'  '+str(WaitedTurnaroundTime[i])+ '\n ')
    output.write("Average TurnaroundTime of Schedule = "+str(AverageTurnaroundTime)+ '\n ')
    output.write("Average WaitedTurnaroundTime of Schedule = "+str(AverageWaitedTurnaroundTime)+ '\n ')
    output.close()

