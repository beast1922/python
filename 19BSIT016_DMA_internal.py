
list=[]
n=int(input("Enter how many numbers you want to enter : "))    
if(n % 2 == 0):
    for i in range(n):
        n1=int(input("Enter number :"))
        list.append(n1)

    print(list)
    ans=[]
    for i in range(0,len(list),2):
        temp = [list[i],list[i+1]]
        temp1=[list[i] + list[i+1]]
        ans.append(temp)
        ans.append(temp1)
        temp = []
    print(ans)
else:
    print("Enter Even Number!!")

