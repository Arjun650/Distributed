from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2
data = comm.gather(data, root = 0)

if rank == 0:
    print("Rank is: ", rank , " Recieving data")
    
    for i in range(0, size):
        # data[i] = (i + 1) ** 2
        value = data[i]
        print("Process: ", rank, " Data: ", value, " From: ", i)