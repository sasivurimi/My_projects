'''a=0
b=1
i=0
print(a,b)
while i<8:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1'''

x=int(input("enter a number"))
if x==0 or x==1:
    print("it is in fib series")
a=0
b=1
c=a+b
flag=0
while c <= x:
    if c==x:
        flag=1
        print('it is in fib series')
    a=b
    b=c
    c=a+b
if flag==0:
    print('it is not in fib series')

    
