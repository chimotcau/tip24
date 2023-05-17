from collections import Counter
f=open('24.txt').readline()
t=''
for i in range(len(f)-1):
    if f[i]=='E':
        t+=f[i+1]
print(Counter(t).most_common()[0][0])        