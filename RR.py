from process import process
from print_p import print_p

def update_readyQ(pList, readyQ, time):
    for i in range(len(pList)):
        if(pList[i].arrival <= time) and (pList[i].arrival != -1):
            pList[i].arrival = -1
            readyQ.append(pList[i])
    return readyQ

def RR(pList, qt, cst):
    
    pList.sort(key=lambda x: x.arrival, reverse=False)
    
    readyQ = list()
    readyQ.append(pList[0])
    time = pList[0].arrival
    pList[0].arrival = -1
    avg_tat = 0.0
    avg_wtat = 0.0
    
    complete = 0
    while complete != len(pList):
        if len(readyQ) == 0:
            time = pList[complete].copy_arrival
            update_readyQ(pList, readyQ, time)
        if readyQ[0].running > qt:
            readyQ[0].running -= qt
            time += qt
            update_readyQ(pList, readyQ, time)
            readyQ.append(readyQ[0])
            del readyQ[0] 
        else:
            time += readyQ[0].running
            readyQ[0].running = 0
            readyQ[0].comp = time
            readyQ[0].tat = readyQ[0].comp - readyQ[0].copy_arrival
            readyQ[0].wait = readyQ[0].tat - readyQ[0].copy_running
            readyQ[0].wtat = readyQ[0].tat / readyQ[0].copy_running
            avg_tat += readyQ[0].tat 
            avg_wtat += readyQ[0].wtat
            del readyQ[0]
            complete += 1
        
    avg_tat /= float(len(pList))
    avg_wtat /= float(len(pList)) 
    
    print_p(pList, avg_tat, avg_wtat, "RR")