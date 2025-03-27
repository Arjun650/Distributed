from mpi4py import MPI 
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10

if rank == 1: 
    for i in range(1, n + 1): 
        comm.send(i, dest=0, tag = 11)
    comm.send(-1, dest=0, tag=11)
elif rank == 0: 
    fact_res = 1
    while True: 
        num = comm.recv(source=1, tag=11)
        if num == -1: 
            break;  
        fact_res *= num
    print(fact_res)