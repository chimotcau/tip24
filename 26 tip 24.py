f=open('inf_26_04_21_24.txt').readlines()
dist=0
for i in range(len(f)):
    if f[i].count('G')<25:
        for k in range(len(f[i])):
            for j in range(len(f[i])-1,k,-1):
                if f[i][k]==f[i][j]:
                    dist = max(dist,j-k)
print(dist)                    