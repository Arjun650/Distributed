from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0: 
    senddata = {'a': 7, 'b': 3.14}
    comm.send(senddata, dest = 1)
elif rank == 1:
    recievedata = 'none'
    print('Before receiving, the data in p1 : ', recievedata)
    recievedata = comm.recv(source=0)
    comm.send(recievedata , dest=3)
    print('After recieving, the data in p1 : ', recievedata)
elif rank == 3: 
    recievedata = "didn't recieve data"
    print('Before recieving data in p3', recievedata)
    recievedata = comm.recv(source=1)
    print('After recieving data in p3:', recievedata)