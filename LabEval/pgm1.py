from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Inside parent process")
else:
    print("Inside process", rank)

name = MPI.Get_processor_name()
print("Hello i am rank %d of %d with name %s" %(rank, size, name))