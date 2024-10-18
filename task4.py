n = [1,1,9,1,9,1,9]

nmax = [0]

for i in range(0,len(n)):
    if n[i] > n[nmax[0]]:
        nmax = []
        nmax.append(i)
    elif n[i] == n[nmax[0]]:
        nmax.append(i)

print(nmax)
out = n.copy()
for i in range(0,len(nmax)):
    s = 0
    for j in range(0,nmax[i]):
        s += float(n[j])
    out[nmax[i]] = s

print(out)
