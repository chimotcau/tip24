f = open('zadanie24_2.txt').readline()
k=1
fm=1
for i in range(len(f)-1):
    if f[i]=='R' and f[i+1]=='R':
        k+=1
        fm = max(k,fm)
    else:
        k=1
print(fm)
#answer:1       
