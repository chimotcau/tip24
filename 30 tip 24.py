f=open('24.txt').readline()
count_old=count=0
k=0
for i in range(len(f)):
    if f[i]=='A':
        k=max(k,count+count_old+1)
        count_old=count
        count=0
    else:
        count+=1 
k=max(k,count+count_old+1) 
print(k)       
