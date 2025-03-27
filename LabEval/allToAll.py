from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 1

senddata = (rank + 1) * np.arange(size, dtype = int)
recvdata = np.empty(size * a_size , dtype=int)

comm.Alltoall(senddata, recvdata)

print("Process: ", rank, " Sending ", senddata, " Recieving: ", recvdata)
