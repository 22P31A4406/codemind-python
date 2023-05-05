#a,b=list(map(int,input().split()))
#if abs(a-b)==1:
 #   print('Yes')
#elif abs(a-b)==9:
 #   print('Yes')
#else:
 #   print('No')
    
a,b=list(map(int,input().split()))
if a==b-1:
    print('Yes')
elif a+9==b:
    print('Yes')
elif a==b+1:
    print('Yes') 
elif a==b+9:
    print('Yes')
else:
    print('No')