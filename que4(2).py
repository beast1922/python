k = [1,2,3,4,5,6]
print("Whole List:- ",k)
temp = []
ans = []
for i in range(0,len(k),2):
    temp = (k[i],k[i+1],k[i] + k[i+1])
    ans.append(temp)
    temp = []
print(ans)
