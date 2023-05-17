f=open('24.txt').readline()
lenmax=0
curlen=0
for i in range(len(f)-1):
    if (f[i]=='K' and f[i+1]=='L') or (f[i]=='L' and f[i+1]=='K'):
        lenmax = max(lenmax,curlen)
        curlen=1
    else:
        curlen+=1
lenmax=max(lenmax,curlen) 
print(lenmax)           
