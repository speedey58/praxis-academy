def ss(list):
    iterasi = 0
    for i in range(len(list)-1):
        minimal = i
        for j in range(i+1,len(list)):
            if list[j]<list[minimal]:
                minimal=j
        iterasi += 1
        list[minimal],list[i]=list[i], list[minimal]
        print(iterasi,list)
list=[98,6,33,44,57,29,86,77]
print('data yang akan di sort :', list)
print('Selection Sort :')
ss(list)