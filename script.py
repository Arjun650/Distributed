from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("Inside Parent Process")
else:
    print("Inside Process ", rank)
