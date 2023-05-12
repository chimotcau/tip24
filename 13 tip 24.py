f = open('zadanie24_2.txt').readline()
k=1
fm=0
for i in range(len(f)-1):
    if f[i]=='D' and f[i+1]=='D':
        k+=1
        fm = max(k,fm)
    else:
        k=1
print(fm)
#answer:11       
