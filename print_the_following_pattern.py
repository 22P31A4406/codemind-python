n=int(input())
for i in range(1,n+1):          # --------->>.PATTERNS
    for j in range(1,n-i+2):
        print(j,end='')
    print()