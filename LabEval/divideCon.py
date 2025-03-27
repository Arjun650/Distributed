from mpi4py import MPI
import numpy as np

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Number of elements (must be at least 8 for 8 CPUs)
n = 16  # Example size (can be changed)
if rank == 0:
    numbers = np.arange(1, n + 1)  # Example array [1, 2, ..., n]
else:
    numbers = None

# Scatter data to all processes
local_size = n // size
local_data = np.zeros(local_size, dtype=int)
comm.Scatter(numbers, local_data, root=0)

# Compute local sum
local_sum = np.sum(local_data)

# Binary tree reduction for sum
step = 1
while step < size:
    if rank % (2 * step) == 0:
        if rank + step < size:
            received_sum = comm.recv(source=rank + step)
            local_sum += received_sum
    elif rank % step == 0:
        comm.send(local_sum, dest=rank - step)
        break
    step *= 2

# Master process prints the result
if rank == 0:
    print("Final Sum:", local_sum)
