class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram



    def toprint(self):
        print('Config:',self.cpu,self.ram)

    
   

    def isram(self):
        if self.ram>4:
            print("Your cpu was maufactured after 2007")
        else:
            print("Your Cpu was manufactured before 2007")


n=int(input("No of Entries: "))
list=[]
for i in range(n):
    cpu=str(input("Enter Cpu:"))
    ram=int(input("Enter Ram: "))
    a=computer(cpu,ram)
    a.toprint()
    a.isram()
    list.append(cpu)
    list.append(ram)
    print(list)
