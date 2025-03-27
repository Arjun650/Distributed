from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None
    print("Process", rank, "before receiving has variable_to_share =", variable_to_share)
variable_to_share = comm.bcast(variable_to_share, root=0)
print("Process", rank, "after receiving has variable_to_share =", variable_to_share)