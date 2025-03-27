from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

array_size = 3

recvData = np.zeros(array_size, dtype=int)
sendData = (rank + 1) * np.arange(array_size, dtype=int)

print("Process: ", rank, " Sending: ", sendData)

comm.Reduce(sendData, recvData, root=0, op=MPI.SUM)

print("On task: ", rank, " After reduce: ", recvData)