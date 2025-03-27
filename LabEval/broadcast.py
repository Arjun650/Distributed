from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    varToShar = p1
else:
    varToShar = None
    print("Process ", rank, " Before receiving ", varToShar)

varToShar = comm.bcast(varToShar, root = 0)
print("Process ", rank, " data: ", varToShar)