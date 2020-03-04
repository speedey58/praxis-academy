def insertion(list):
    for j in range(len(list)-1,-1,-1):
        value = list[j]
        hole = j
        while hole < (len(list)-1) and list[hole+1]>list[hole]:
            list[hole] = list[hole+1]
            hole = hole+1
            list[hole] = value
        print(list)
list = [84,77,92,1,4,99,37,15]
print("Data yang akan di sort", list)
print("Insertion Sort :")

insertion(list)