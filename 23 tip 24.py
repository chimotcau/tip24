from collections import Counter
f=open('24.txt').readlines()
k=10*20
t=''
for i in f:
    if i.count('N')<k:
        k=i.count('N')
        t=Counter(i).most_common()[0][0]
print(t)        
