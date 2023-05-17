f=open('24.txt').readline()
k=1
lm=0
for i in range(len(f)-1):
    if f[i]=='P' and f[i+1]=='P':
        lm=max(lm,k)
        k=1
    else:
        k+=1
lm=max(lm,k)
print(lm)            
