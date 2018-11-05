import numpy as np
inputfile = raw_input("input file name: ")
outputfile = raw_input("output file name: ")
Context_Switch_Time = int (raw_input("Context Switch Time: "))
with open(inputfile, "r") as input:
    in_arr = input.read().split()

num = int(in_arr[0]) #number of processes
process_queue=np.zeros([num,4],dtype=float)
k=1
for i in range (0,num):
    process_queue[i][0]=int(in_arr[k]) # process id
    process_queue[i][1] = in_arr[k+1]  # process arrival time
    process_queue[i][2] = in_arr[k+2]  #process burst time
    process_queue[i][3] = int(in_arr[k+3]) # process priority
    k+=4

#sort the array of processes according to arrival time
process_queue=np.array(sorted(process_queue, key=lambda x: x[1], reverse=False))
WaitTime=np.zeros(num,dtype=float)
TurnaroundTime=np.zeros(num,dtype=float)
WaitedTurnaroundTime=np.zeros(num,dtype=float)
#calculate Wait time ,turnaround time, weighted turnaround time
for i in range (0,num):
    #for j in range(0, i):
        #WaitTime[i]+= process_queue[j][2] # burst time
    if (not (i == 0)):   # as first process may not came at t=0 but whenever it come it will serve immediately after Context switching time
        WaitTime[i]=WaitTime[i-1]+process_queue[i-1][2]- process_queue[i][1] #waiting time of previous one and burst time of  it - arrival time of me
    WaitTime[i]+=Context_Switch_Time
    TurnaroundTime[i]= WaitTime[i]+process_queue[i][2] # wait time+ burst time
    WaitedTurnaroundTime[i]=TurnaroundTime[i]/process_queue[i][2] #turnaroundtime/burst time
#calculate Average turnaround time of schedule
AverageTurnaroundTime= np.sum(TurnaroundTime)/num
#calculate Average weightturnaround time of schedule
AverageWaitedTurnaroundTime= sum(WaitedTurnaroundTime)/num

with open(outputfile, "w") as output:
    output.write('ProcessID\tWaitingTime\tTurnaroundTime\tWaitedturnaroundTime\n ')
    for i in range (0,num):
        output.write(str(int(process_queue[i][0]))+' '+str(WaitTime[i])+'  '+str(TurnaroundTime[i])+'  '+str(WaitedTurnaroundTime[i])+ '\n ')
    output.write("Average TurnaroundTime of Schedule = "+str(AverageTurnaroundTime)+ '\n ')
    output.write("Average WaitedTurnaroundTime of Schedule = "+str(AverageWaitedTurnaroundTime)+ '\n ')
    output.close()

# in order to draw Graph
# Started time of each one will be arrival + waited 
# Finsished time of each one will be started + brust
#