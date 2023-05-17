f=open('24.txt').readline()
lm=0
k=0
for i in range(len(f)-1):
    if (f[i]=='a' and f[i+1]=='d') or (f[i]=='d' and f[i+1]=='a'):
        lm=max(lm,k)
        k=1
    else:
        k+=1
lm=max(lm,k)
print(lm)            