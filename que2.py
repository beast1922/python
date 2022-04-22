list = [1,2,3,4,5,6,7,8,9,10]
ans_even=0
ans_odd=0
i=0
while (i < len(list)):
    if(list[i] % 2==0):
        ans_even = ans_even + 1
        
    else:
        ans_odd = ans_odd + 1
    i = i + 1
        
       
print("count of even number",ans_even)
print("count of odd number",ans_odd)
        
