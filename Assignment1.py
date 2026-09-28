#PRINTING PRIME WITHIN A LIMIT
limit=int(input("Enter the limit:"))
for num in range(2,limit+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)



