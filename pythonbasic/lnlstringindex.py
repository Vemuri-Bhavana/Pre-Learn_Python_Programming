s=input()
k=0
if len(s)<=7:
    k=1
for i in range(len(s)):
    if (i+k)%2==0:
        print(s[i])
#assuming string indices starts from 0
