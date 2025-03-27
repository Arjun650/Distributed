from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0: 
    senddata = {'a': 7, 'b': 3.14}
    comm.send(senddata, dest=1, tag = 11)
    comm.send('testdata', dest=1, tag = 10)
elif rank == 1: 
    recievedata = 'none'
    print('Before receiving, the data is: ', recievedata)
    recievedata = comm.recv(source=0,tag=11)
    print('After receiving, the data is: ', recievedata)
