from collections import Counter
f=open('24.txt').readline()
t=''
for i in range(len(f)-2):
    if f[i]==f[i+1]:
        t+=f[i+2]
#print(t)        
print(Counter(t).most_common())        

