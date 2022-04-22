final = []
first = []
ch="y"
while(ch=="y"):
    n1 = int(input("Enter number of values you want to enter : "))
    if(n1 % 3 == 0):
        for j in range(n1):
            number=int(input("Enter Values :- "))
            first.append(number)
        final.append(first)
        first = []
        
    else:
        print("Enter the value which are multiple of 3 ")
    ch=input("do you want to continue : y/n ")
print(final)

'''for k in len(final):
    for j in k:
        if (final[i][0] + final[i][1] == final[i][3]):
            print("yes")
        else:
            print("no")'''
            
    
        
