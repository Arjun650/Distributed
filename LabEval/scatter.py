from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0:
    arr_to_share = "dklfj asdkfj asdklf jaklj "
else:
    arr_to_share = None

recvbuf = comm.scatter(arr_to_share, root = 0)
print("Process: ", rank , "Data: ", recvbuf)