def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return f(n-1)*n-2*f(n-2)
print(f(6))  
#answer:44              