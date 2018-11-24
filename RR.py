from process import process
from print_p import print_p

class pRR:
    def __init__(self, pid, ST, FT):
        self.pid = pid
        self.start = ST
        self.finish = FT


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
    prev = readyQ[0]

    avg_tat = 0.0
    avg_wtat = 0.0

    chart = []
    first = 0
    complete = 0
    while complete != len(pList):
        if first == 0:
            time += cst
            first = 1

        if len(readyQ) == 0:
            if time < pList[complete].copy_arrival:
                time = pList[complete].copy_arrival
            update_readyQ(pList, readyQ, time)
            time += cst

        if readyQ[0].running > qt:
            readyQ[0].running -= qt

            chart.append(pRR(readyQ[0].pid, time, time + qt))

            time += qt
            update_readyQ(pList, readyQ, time)
            readyQ.append(readyQ[0])
            prev = readyQ[0]
            del readyQ[0]
        else:
            chart.append(pRR(readyQ[0].pid, time, time + readyQ[0].running))

            time += readyQ[0].running
            readyQ[0].running = 0
            readyQ[0].finish = time
            readyQ[0].tat = readyQ[0].finish - readyQ[0].copy_arrival
            readyQ[0].wait = readyQ[0].tat - readyQ[0].copy_running
            readyQ[0].wtat = readyQ[0].tat / readyQ[0].copy_running
            avg_tat += readyQ[0].tat
            avg_wtat += readyQ[0].wtat
            prev = readyQ[0]
            del readyQ[0]
            complete += 1

        if len(readyQ) != 0:
            if prev != readyQ[0]:
                time += cst

    avg_tat /= float(len(pList))
    avg_wtat /= float(len(pList))

    print_p(pList, avg_tat, avg_wtat, "RR")
    return chart
