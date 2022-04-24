l=list(map(int,input("Enter Five Numbers: ").split(" ",)))
l=l[:5]
i=0
while i<len(l):
    if l[i]<9:
        l.pop(i)
        i-=1
    i+=1
print(sum(l))
