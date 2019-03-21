def shengcheng():
    h=[1]
    while True:
        yield h
        h=[1] + [h[i]+h[i+1] for i in range(len(h)-1) ] + [1]
n=0
for t in shengcheng():
    print(t)
    n=n+1
    if n==10 :
        break

s=[1] + [2] +[3]
print (s[2])






