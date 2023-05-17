f=open('24.txt').readline()
f=f.replace('XZZY','!')
curlen =0
maxlen =0
for i in range(len(f)):
    if f[i]=='!':
        maxlen=max(maxlen,curlen+3)
        curlen =3
    else:
        curlen +=1
maxlen=max(maxlen,curlen)    
print(maxlen)            

        
