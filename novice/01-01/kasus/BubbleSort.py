def bs(list):
    iterasi = 0
    for j in range (len(list)-1):
        for i in range(len(list)-1-j):
            if list [i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        iterasi+=1
        print(iterasi,list)

list= [9,17,2,42,1,3,4,67]
print('Data yang akan di sort :',list)
print('Bubble Sort :')
bs(list)
