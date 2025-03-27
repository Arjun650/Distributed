from mpi4py import MPI 

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
print("My rank is", rank)

if(rank == 0):
    data = 10000
    dest_p = 4
    comm.send(data, dest=dest_p)
    print("Sending data %s"%data)

if(rank == 1):
    data = 'dkfj'
    dest_p = 8
    comm.send(data, dest = dest_p)
    print("Sending data %s"%data)

if(rank == 4):
    data = comm.recv(source=0)
    print("data recieved",  data)

if(rank == 8):
    data = comm.recv(source = 1)
    print("data recieved", data)