# cook your dish here
a,b = map(int,input().split())
if (a+b) % 2 == 0:
    print((a+b)// 2 - b)
else:
    print(-1)