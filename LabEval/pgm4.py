from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("The rank is", rank)

if(rank == 1):
    send_d = "hello"
    desti = 5
    sourced = 5
    data_rec = comm.sendrecv(send_d, dest = desti, source=sourced)
    print("sent: ", send_d)
    print("recv: ", data_rec)

if(rank == 5):
    send_d = "world"
    desti = 1
    sourced = 1; 
    data_rec = comm.sendrecv(send_d, dest = desti, source=sourced)
    print("sent: ", send_d)
    print("recv: ", data_rec)
