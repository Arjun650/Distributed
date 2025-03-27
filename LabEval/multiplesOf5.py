from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

x = 100

chunk_size = x // size

localdata = np.random.randint(1, 1001, chunk_size)

gatherd = comm.gather(localdata, root = 0)

if rank == 0: 
    multipleOf5 = 0

    for dat in gatherd: 
        for num in dat: 
            if num % 5 == 0: 
                multipleOf5 += 1
    print("multiple: ", multipleOf5)