from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

if size < 3:
    if rank == 0:
        print("Run with minimum 3 processes")
    exit()


elif rank == 0:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total_sum = sum(numbers)
    print("The total sum is", total_sum)
    comm.send(numbers, dest = 1, tag = 10)
    comm.send(numbers, dest = 2, tag = 12)

elif rank == 1: 
    numbers = comm.recv(source=0, tag = 10)
    evenSum = 0
    for num in numbers: 
        if(num % 2 == 0):
            evenSum += num
    
    print("Even sum: ", evenSum)
elif rank == 2: 
    numbers = comm.recv(source = 0, tag  =12)
    oddSum = 0
    for num in numbers: 
        if num % 2 != 0:
            oddSum += num
    print("Odd Sum: ", oddSum)            