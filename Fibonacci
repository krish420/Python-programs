def fibo(n):
    fno = 0
    sno = 1
    list = [0,1]
    for i in range(n-1): # we have already included two elements in list hence list runs 2 less than n,i.e, but in here since upper limit is not counted thus to run the list two times less than n we use (n-2)
        res = fno+sno
        fno = sno
        sno = res
        #print(res)
        list.append(res)
    print(*list,sep=",") #prints upto 10th element
    print(list[10]) #prints 10 th element
fibo(10)
