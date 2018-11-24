import numpy as np

inp_arr = []

inputfile = input()
outputfile = input()

with open(inputfile, "r") as inp:
    inp_arr = inp.read().split()

num = int(inp_arr[0]) #number of processes
mean_arr = float(inp_arr[1])
sigma_arr = float(inp_arr[2])
mean_burst = float(inp_arr[3])
sigma_burst = float(inp_arr[4])
mean_prior = float(inp_arr[5])

with open(outputfile + ".txt", "w") as outp:
    outp.write(str(num))
    outp.write('\n')
    for i in range (0, num):
        outp.write(str(i+1) + ' ' + str(abs(np.random.normal(mean_arr, sigma_arr))) + ' '
                   + str(abs(np.random.normal(mean_burst, sigma_burst))) + ' ' + str(abs(np.random.poisson(mean_prior))) + '\n')