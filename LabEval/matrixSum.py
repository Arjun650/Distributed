from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Each process computes the sum of one row
if rank < matrix.shape[0]:  # To avoid extra processes running
    local_sum = np.sum(matrix[rank])  # Process rank computes row[rank]
else:
    local_sum = 0

# Master process collects all row sums
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Final Matrix Sum: {total_sum}")
