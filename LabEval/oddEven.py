from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

totalSize = 1000

if rank == 0:  # Master process
    data = np.random.randint(1, 51, totalSize)

    if size > 1:  # Ensure there's at least one worker
        chunkSize = totalSize // (size - 1)
        chunks = np.array_split(data, size - 1)

        for i in range(1, size):
            comm.send(chunks[i - 1], dest=i, tag=11)

        evenSum = 0
        oddSum = 0

        for i in range(1, size):  # Receiving from all worker processes
            parSum = comm.recv(source=i, tag=22)

            if i % 2 == 0:
                evenSum += parSum
            else:
                oddSum += parSum

        totalSum = evenSum + oddSum  # Fix: Compute total sum here
        print("Even Sum:", evenSum, "Odd Sum:", oddSum, "Total Sum:", totalSum)

else:  # Worker processes
    dataChunk = comm.recv(source=0, tag=11)

    result = 0 
    if rank % 2 == 0:
        for num in dataChunk: 
            if num % 2 == 0: 
                result += num
    else:
        for num in dataChunk: 
            if num % 2 != 0: 
                result += num

    comm.send(result, dest=0, tag=22)  # Correctly sending the result
