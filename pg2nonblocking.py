from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    senddata1 = 'Hello'
    senddata2 = 'How are you?'

    req1 = comm.isend(senddata1, dest=1, tag=11)
    req2 = comm.isend(senddata2, dest=2, tag=12)

    req_recv1 = comm.irecv(source=1)
    req_recv2 = comm.irecv(source=2)

    req1.wait()
    req2.wait()

    recievedata1 = req_recv1.wait()
    recievedata2 = req_recv2.wait()

    print(recievedata1 + " " + recievedata2)

elif rank == 1:
    req_recv1 = comm.irecv(source=0, tag=11)
    recievedata1 = req_recv1.wait()
    print(recievedata1)

    req_send = comm.isend('Thank ', dest=0)
    req_send.wait()  

elif rank == 2:
    req_recv2 = comm.irecv(source=0, tag=12)
    recievedata2 = req_recv2.wait()
    print(recievedata2)

    req_send = comm.isend('You!', dest=0)
    req_send.wait()
