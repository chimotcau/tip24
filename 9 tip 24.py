s = open('zadanie24_1.txt').readline()
k=1
fmax=1
for i in range(len(s)-1):
    if (s[i]=='C') and(s[i+1]=='C'):
        k+=1
        fmax = max(k,fmax)
    else:
        k=1
print(fmax)
#answer:1            