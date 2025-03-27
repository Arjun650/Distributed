from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

if(size < 4):
    print("Execute with minimum 4 process")
    exit()

if(rank == 0):
    text = "Hello World"
    print("Text: ", text)

    comm.send(text, dest = 1, tag = 12)
    comm.send(text, dest = 2, tag = 13)

if(rank == 1):
    text = comm.recv(source = 0, tag = 12 )
    vow =""
    for char in text: 
        if char in "aeiou":
            vow = vow + char + " "
    print("Vowels: ", vow)

if(rank == 2):
    text = comm.recv(source = 0, tag = 13)
    con = ""

    for char in text: 
        if char.isalpha() and char not in "aeiou":
            con = con + char + " "

    print("Consonants: ", con)