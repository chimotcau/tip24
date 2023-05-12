s = open('zadanie24_1.txt').readline()
k=1
fmax=0
for i in range(len(s)-1):
    if (s[i]=='B') and(s[i+1]=='B'):
        k+=1
        fmax = max(k,fmax)
    else:
        k=1
print(fmax)
#answer:11            