from mpi4py import MPI
import numpy as np
import time
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N, M = 500, 500  # Image dimensions
theta = math.radians(30)  # Rotation angle

def transform_pixel(x, y):
    """Translate (10,10) and rotate by 30 degrees"""
    x_new = x * math.cos(theta) - y * math.sin(theta) + 10
    y_new = x * math.sin(theta) + y * math.cos(theta) + 10
    return int(x_new), int(y_new)

if rank == 0:
    # Create a dummy image (NxM matrix with pixel values)
    image = np.random.randint(0, 256, (N, M))

    # Distribute rows equally to all processes
    row_chunks = np.array_split(image, size-1, axis=0)

    start_time = time.time()

    for i in range(1, size):
        comm.send(row_chunks[i-1], dest=i, tag=11)

    # Collect transformed rows
    new_image = np.zeros_like(image)

    for i in range(1, size):
        transformed_rows = comm.recv(source=i, tag=22)
        start_row = (i-1) * (N // (size-1))
        new_image[start_row:start_row + transformed_rows.shape[0], :] = transformed_rows

    end_time = time.time()
    
    # Compute speedup & efficiency
    T_serial = N * M  # Approximate sequential time units
    T_parallel = (end_time - start_time) * 1e6  # Convert to microseconds
    speedup = T_serial / T_parallel
    efficiency = (speedup / size) * 100

    print(f"Speedup Factor: {speedup:.2f}")
    print(f"Efficiency: {efficiency:.2f}%")

else:
    # Receive rows assigned to this process
    sub_image = comm.recv(source=0, tag=11)
    
    new_sub_image = np.zeros_like(sub_image)

    for i in range(sub_image.shape[0]):
        for j in range(sub_image.shape[1]):
            x_new, y_new = transform_pixel(i, j)
            if 0 <= x_new < N and 0 <= y_new < M:
                new_sub_image[i, j] = sub_image[i, j]  # Map transformed pixels
    
    # Send transformed data back
    comm.send(new_sub_image, dest=0, tag=22)
