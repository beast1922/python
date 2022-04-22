list2 = [1,2,3,4,5,6,7,8,9,10]
ans_even=0
ans_odd=0
i=0
for i in range(len(list2)):
    if(list2[i] % 2 ==0):
        ans_even= ans_even + list2[i]
        i = i + 1
    else:
        ans_odd= ans_odd + list2[i]
        i = i+ 1 
    
    
print("Sum of even number",ans_even)
print("Sum of odd number",ans_odd)
        
        
