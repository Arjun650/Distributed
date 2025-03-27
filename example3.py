from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("my rank is: ", rank)

if rank == 0: 
    data = 10000000
    destination_process = 4
    comm.send(data, dest = destination_process)
    print("Sending data %s" %data + "to process %d" %destination_process)

if rank == 1:
    destination_process=8
    data="hello"
    comm.send(data, data=)