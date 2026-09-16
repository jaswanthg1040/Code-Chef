# cook your dish here
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if (2*n) > k:
        print(max(0,(k-(n//2))))
    else:
        print(k)