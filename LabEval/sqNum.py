from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size % 2 != 0: 
    print("Enter even process")
    exit()

pair = size - rank - 1

if rank % 2 != 0: 
    rand_num = np.random.randint(1, 101)
    comm.send(rand_num, dest=pair, tag = 11)
    squaredNum = comm.recv(source=pair, tag = 22)

    print("Process: ", rank, " To: ", pair, " Sq Value: ", squaredNum)

else: 
    recivedNum = comm.recv(source=pair, tag = 11)
    squaredNum = recivedNum ** 2
    comm.send(squaredNum, dest=pair, tag=22)
