from collections import Counter
f=open('24.txt').readline()
t=''
for i in range (len(f)-2):
    if f[i]==f[i+2] :
        t+=f[i+1]
print(Counter(t).most_common()[0][0])        
