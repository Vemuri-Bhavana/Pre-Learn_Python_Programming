l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
l3=[]
for i in range(len(l1)):
    if i%2==0:
        l3.append(l1[i])
for i in range(len(l2)):
    if i%2!=0:
        l3.append(l2[i])
print(l3)
