import time

t = time.time()

x = [y**5 for y in range(1,151)]
x1 = set(x)

for a in range(0,150):
    for b in range(a,150):
        for c in range(b,150):
            for d in range(c,150):
                e = x[a] + x[b] + x[c] + x[d] 
                if e in x1:
                    print(a + 1, b + 1, c + 1, d + 1, x.index(e) + 1)
                    print(a + b + c + d + x.index(e) + 5)
                        
print(time.time() - t)