from mpi4py import MPI
import random

def compute_partial_sum(numbers):
    """Recursively sums up the numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 16  # Total numbers to sum
numbers = None

if rank == 0:  # Master initializes numbers
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 100))

    print("Master has numbers:", numbers)

# Divide numbers among processes
chunk_size = n // size
local_numbers = comm.scatter([numbers[i * chunk_size:(i + 1) * chunk_size] for i in range(size)], root=0)

# Compute local sum
local_sum = compute_partial_sum(local_numbers)
print(f"Process {rank} computed local sum: {local_sum}")

# Reduce to master
final_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print("Final sum of numbers:", final_sum)