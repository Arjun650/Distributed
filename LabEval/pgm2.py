from mpi4py import MPI

a = MPI.Wtime()
print("Welcome")
b = MPI.Wtime()

ts = b - a

comm = MPI.COMM_WORLD
x = MPI.Wtime()
rank = comm.Get_rank()

if(rank == 0):
    a = {"a": 3, "b": 3}
    comm.send("Hi", dest = 1, tag = 1)
    comm.send(a, dest =2 )
if(rank == 1):
    recvd = comm.recv(source = 0, tag = 1)
    print(recvd)
if(rank == 2):
    recvd = comm.recv(source = 0)
    print(recvd)

if(rank == 0):
    y = MPI.Wtime()
    tp = y - x
    sp = ts/tp
    eff = (sp / 2) * 100

    print("Speedupp", sp)
    print("Efficieny", eff)