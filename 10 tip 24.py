f = open('zadanie24_1.txt').readline()
k=1
fm=0
for i in range(len(f)-1):
    if (f[i],f[i+1]) in [('A','B')]:
        k+=1
    else:
        fm=max(k,fm)
        k=1
print(fm)            
        
    