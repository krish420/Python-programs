
count=0
cnt=0

class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram



    def toprint(self):
        print('Config:',self.cpu,self.ram)

    
   

    def isram(self):
        global count
        global cnt
        if self.ram>4:
            print("Your cpu was maufactured after 2007")
            count=count+1
        else:
            print("Your Cpu was manufactured before 2007")
            cnt=cnt+1



n=int(input("No of Entries: "))

dlist={}
d={}

for i in range(1,n+1):
    cpu=str(input("Enter Cpu: "))
    ram=int(input("Enter Ram: "))
    a=computer(cpu,ram)
    a.toprint()
    a.isram()
    dlist={cpu : ram}
    d[i]=dlist
    print(d)
       

print("\[Serial no:,Cpu,Ram]")
print('\n',d)
print("\nThe Cpus manufactured after 2007:",count)
print("The Cpus manufactured before 2007:",cnt)



