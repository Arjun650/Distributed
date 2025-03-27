from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank + 1)**2
print("rank = %s" %rank + "my data is: ")
print(data)

data = comm.gather(data, root=0)