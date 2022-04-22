t = (10, 11, 12, 13, 14, 15)
print("Original tuple : ",t)


new_tup = ()
for k in reversed(t):
    new_tup = new_tup + (k,)
print("Reversed tuple : ")
print(new_tup)

