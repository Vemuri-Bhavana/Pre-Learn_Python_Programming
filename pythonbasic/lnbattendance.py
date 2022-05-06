e=int(input())
w=int(input())
data=list(input().split(" "))
for i in range(w):
    if data[i].count('P')==e:
        print(i+1,end=" ")
