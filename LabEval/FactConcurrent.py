from mpi4py import MPI
import numpy as np

def factorial(start, end):
    res = 1
    for i in range(start, end + 1): 
        res *= i

    return res

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 5
half = n // 2

if rank == 1: 
    part1 = factorial(1, half)
    comm.send(part1, dest= 0, tag = 11)
elif rank == 2: 
    part2 = factorial(half + 1, n)
    comm.send(part2, dest=0, tag=22)
elif rank == 0: 
    part1 = comm.recv(source=1, tag = 11)
    part2 = comm.recv(source=2, tag=22)

    result = part1 * part2 

    print("result: ", result)