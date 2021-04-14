check = int (input("Enter the number of Fibonacci Numbers to be printed : "))
i = 0
j = 1
k = 1
c = 2
print (i,"\b,",j,end=" \b")
while(c < check):
    k = i + j
    print(",",k,end=" \b")
    i = j
    j = k
    c = c + 1