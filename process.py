class process:
    def __init__(self, pid, AT, BT, PR):
        self.pid = pid
        self.arrival = AT
        self.running = BT
        self.priority = PR
        self.comp = 0   #completion time
        self.wait = 0   #wait time