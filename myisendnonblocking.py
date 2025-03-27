from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0: 
    senddata = {'a': 7, 'b': 3.14}
    req = comm.isend(senddata, dest = 1, tag = 11)
    req.wait()
elif rank == 1: 
    receiveddata = 'none'
    print('Before receiving, the data is: ', receiveddata)
    receiveddata = comm.irecv(source=0, tag = 11)
    print('After receiing, the data is: ', receiveddata)
    reply = re