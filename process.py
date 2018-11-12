class process:
    def __init__(self, pid, AT, BT, PR):
        self.pid = pid
        self.arrival = AT
        self.running = BT
        self.priority = PR
		self.copy_running = BT
        self.copy_arrival = AT
        self.remaining = BT # in order to use it in RR and SRTF
        self.start=0.0 #to keep track of start time of each process
        self.finish=0.0 #to keep track of finish time of each process
        self.tat = 0.0 #turnaround time
        self.wtat = 0.0 #weighted turnaround time
        self.wait = 0.0   #wait time
