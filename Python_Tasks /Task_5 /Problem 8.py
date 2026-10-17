# Set.add()
# https://www.hackerrank.com/challenges/py-set-add/copy-from/485395360

# CODE
N=int(input())
res=set()
for i in range(N):
    s=input()
    res.add(s)
print(len(res))
