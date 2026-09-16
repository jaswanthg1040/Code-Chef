# cook your dish here
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if (2*n) >= k and k >= 0 :
        print((k // 2)* 2 )
    else:
        print(k)
