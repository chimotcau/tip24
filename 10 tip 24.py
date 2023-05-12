f = open('zadanie24_1.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'A' and k%2 == 0) or (f[i] == 'B' and k%2 == 1):
        k += 1
        m = max(m, k)
    elif f[i] == 'A': k = 1
    else: k = 0
print(m)