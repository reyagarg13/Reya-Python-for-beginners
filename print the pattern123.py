"""
WAP to print the following pattern:
1
1 2
1 2 3
"""
depth = 4
for number in range(1, depth):
    for i in range(1, number + 1):
        print(i, end=' ')
    print("")
