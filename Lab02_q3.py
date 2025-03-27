from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD  
rank = comm.Get_rank()  
size = comm.Get_size() 

n = 10 

if size < 2:
    if rank == 0:
        print("Please run the program with at least 2 processes.")
    exit()

if rank == 0:
    numbers = np.random.randint(0, 101, size=n)
    print(f"Process {rank}: Generated array: {numbers}")

    comm.send(numbers, dest=1, tag=11)

    count_less_than_50 = np.sum(numbers < 50)
    print(f"Process {rank}: Count of numbers less than 50 = {count_less_than_50}")

    total_sum = comm.recv(source=1, tag=12)
    print(f"Process {rank}: Sum of all numbers = {total_sum}")

elif rank == 1:
    numbers = comm.recv(source=0, tag=11)

    total_sum = np.sum(numbers)

    comm.send(total_sum, dest=0, tag=12)
