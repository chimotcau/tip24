f=open('inf_22_10_20_24.txt').readlines()
count=0
for i in range(len(f)):
    if f[i].count('E')>f[i].count('A'):
        count+=1
print(count)        
    
    

