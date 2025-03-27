from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank == 1:
    arr_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
    arr_to_share = None
recvbuf = comm.scatter(arr_to_share, root=1)
print("Process", rank, "received", recvbuf)