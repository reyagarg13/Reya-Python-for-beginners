def Diff(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1

num = [10,23,14,54,32]
for CNT in range (4,0,-1):
    A = num[CNT]
    B = num[CNT-1]
    print(Diff(A,B),'#',end='')
