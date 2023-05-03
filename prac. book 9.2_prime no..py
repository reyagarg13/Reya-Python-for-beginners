
start_val = 1
for n in range(start_val, n+1):
    if(n>1):
        for i in range(2,30):
            if(n%i)==0:
                break
        else:
            print(n)
