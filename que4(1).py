k = [1,2,3,4,5,6]
print("Whole List:- ",k)
temp = []
ans = []
for i in range(0,len(k),2):
    #temp.append(k[i])
    #temp.append(k[i+1])
    temp = (k[i],k[i+1])
   

    #if(k[i] > k[i+1]):
     #   temp = (k[i],k[i+1],k[i])
    #else:
     #   temp = (k[i],k[i+1],k[i])
        
    ans.append(temp)
    temp = []
print(ans)
