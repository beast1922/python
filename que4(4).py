k = [1,2,3,4,5,6]
print("Whole List:- ",k)
temp = []
ans = []

temp1 = []
ans1 = []
for i in range(len(k)):
    if(k[i] % 2 == 0):
        temp =  k[i]
        ans.append(temp)
    else:
        temp1 = (k[i])
        ans1.append(temp1)
        
    i = i + 1     
    
print(ans)
print(ans1)

