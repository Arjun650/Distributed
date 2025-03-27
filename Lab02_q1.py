from mpi4py import MPI

comm = MPI.COMM_WORLD  
rank = comm.Get_rank()
size = comm.Get_size()

if size < 3:
    if rank == 0:
        print("Please run the program with at least 3 processes.")
    exit()

if rank == 0:
    numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
    total_sum = sum(numbers)
    print(f"Process {rank}: Total sum of list = {total_sum}")

    comm.send(numbers, dest=1, tag=11)
    comm.send(numbers, dest=2, tag=12)

elif rank == 1: 
    numbers = comm.recv(source=0, tag=11)
    even_sum = sum(num for num in numbers if num % 2 == 0)
    print(f"Process {rank}: Sum of even numbers = {even_sum}")

elif rank == 2:
    numbers = comm.recv(source=0, tag=12)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print(f"Process {rank}: Sum of odd numbers = {odd_sum}")
