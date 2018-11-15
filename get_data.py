def get_data(inputfile):
    with open(inputfile, "r") as input:
        in_arr = input.read().split()
    process_list=list()
    k=1
    for i in range (0,len(in_arr)/4):
        # process id     # process arrival time         # process brust time     # process priority
        process_list.append(process(int(in_arr[k]),float(in_arr[k+1]),float(in_arr[k+2]), int(in_arr[k+3])))
        k+=4
    return process_list