from mpi4py import MPI

comm = MPI.COMM_WORLD  
rank = comm.Get_rank()  
size = comm.Get_size()  

if size < 4:
    if rank == 0:
        print("Please run the program with at least 4 processes.")
    exit()

if rank == 0:
    text = "Hello World"
    print(f"Process {rank}: Sending string '{text}' to processes 2 and 3.")

    comm.send(text, dest=2, tag=11)

    comm.send(text, dest=3, tag=12)

elif rank == 2:
    text = comm.recv(source=0, tag=11)
    vowels = [ch for ch in text if ch.lower() in "aeiou"]
    print(f"Process {rank}: Vowels in the string: {''.join(vowels)}")

elif rank == 3:
    text = comm.recv(source=0, tag=12)
    consonants = [ch for ch in text if ch.isalpha() and ch.lower() not in "aeiou"]
    print(f"Process {rank}: Consonants in the string: {''.join(consonants)}")
