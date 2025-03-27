from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Ensure there are exactly 10 processors (P0 to P9)
if size != 10:
    if rank == 0:
        print("Error: This program requires exactly 10 processors.")
    MPI.Finalize()
    exit()

# Maximum number of digits in input (assumption: 3-digit numbers)
MAX_DIGITS = 3

# Function to get the most significant digit (MSD)
def get_msd(number):
    return int(str(number)[0])  # Get the first digit of the number

# Master process (P0)
if rank == 0:
    # Generate random 3-digit numbers (example: n=20)
    n = 20
    numbers = np.random.randint(100, 999, n)  # Generate 20 random 3-digit numbers
    print("Unsorted numbers:", numbers)

    # Distribute numbers into buckets based on the MSD
    buckets = {i: [] for i in range(10)}
    for num in numbers:
        msd = get_msd(num)
        buckets[msd].append(num)

    # Send each bucket to the corresponding process
    for i in range(1, 10):  # P1 to P9
        comm.send(buckets[i], dest=i, tag=11 + i)

    # Receive sorted numbers from workers
    sorted_numbers = []
    for i in range(1, 10):
        sorted_bucket = comm.recv(source=i, tag=22 + i)
        sorted_numbers.extend(sorted_bucket)

    # Print final sorted array
    print("Sorted numbers:", sorted_numbers)

# Worker processes (P1 to P9)
else:
    # Receive numbers for this bucket
    bucket = comm.recv(source=0, tag=11 + rank)

    # Sort bucket
    bucket.sort()

    # Send sorted bucket back to master
    comm.send(bucket, dest=0, tag=22 + rank)

    # Print bucket processing details
    print(f"Process {rank} sorted bucket: {bucket}")
