Bank = {1:["Anjali",5000],2:["Bina",10000],3:["Chetali",15000]}
trans=[]
i=0
j=1
while i in range(j):
    ac = input("\nInput A/C no. :- ")
    ac = int(ac)
    if(ac not in Bank):
        print("Enter Valid Account number!")
        break
    trans.append(ac)
        
    t1 = input("\nEnter type of transection you want to do (D/W) :- ")
    trans.append(t1)
    if(t1 == 'W' or t1 == 'w'):
        amount = int(input("Enter Amount for Withdraw : "))
        temp = Bank[ac][1] - amount
        if(temp < 2000):
            print("Withdraw cannot be done due to insufficiant balance in a/c")
        else:
            Bank[ac][1] = Bank[ac][1] - amount
            print("Updated Amount :- "+str(Bank[ac][1]))
            trans.append(amount)
            print(trans)
    elif(t1 == 'D' or t1 == 'd'):
        amount = int(input("Enter Amount for Depsoit : "))
        dcheck = (Bank[ac][1] * 50) / 100
        if(amount > dcheck):
            print("Depsoit cannot be done due to over deposit balance")
        else:
            Bank[ac][1] = Bank[ac][1] + amount
            print("Updated Amount :- "+str(Bank[ac][1]))
            trans.append(amount)
            print(trans)
    else:
        print("Enter valid input")
        
    print(Bank)
    
    
    n1=int(input("\nEnter a/c no. of account to Report : "))
    if(n1 in Bank):
        print(trans[n1])

    n= input("\nDo you want to terminate process? (Y/N) :- ")
    if(n == 'N' or n == 'n'):
        continue
    if(n == 'Y' or n == 'y'):
        break


