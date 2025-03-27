from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0: 
    senddata1 = 'Hello'
    senddata2 = 'How are you?'
    comm.send(senddata1, dest = 1, tag = 11)
    comm.send(senddata2, dest= 2, tag = 12)

    recievedata1 = comm.recv(source = 1)
    recievedata2 = comm.recv(source = 2)
    print(recievedata1 + " " + recievedata2)
elif rank == 1: 
    recievedata1 = comm.recv(source = 0, tag = 11)
    print(recievedata1)
    comm.send('Thank ', dest = 0)
elif rank == 2: 
    recievedata2 = comm.recv(source = 0, tag = 12)
    print(recievedata2)
    comm.send('You!', dest = 0)


