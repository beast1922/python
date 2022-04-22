k = []
ans = []

n = int(input("Enter how many numbers you want:- "))

if (n % 2 == 0):
    for i in range(n):
        n1 = int(input("Enter number:- "))
        k.append(n1)
    print(k)

    for i in range(0,len(k),2):
        temp = [k[i],k[i+1]]
        temp1 = [k[i] + k[i+1]]
        ans.append(temp)
        ans.append(temp1)
    temp = []
    print(ans)
    
else:
    print("Enter even number")
    
