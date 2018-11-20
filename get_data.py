from process import process


def get_data(inputfile):

    process_list = list()
    # read input file
    with open(inputfile, "r") as inp:
        # get number of processes
        np = int(inp.readline())

        for i in range(np):
            parameters = [float(x) for x in inp.readline().split()]
            pid = int(parameters[0])
            arrival_time = parameters[1]
            burst_time = parameters[2]
            priority = int(parameters[3])
            process_list.append(process(pid, arrival_time, burst_time, priority))

    return process_list
