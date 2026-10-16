# Set.add()
# https://www.hackerrank.com/challenges/py-set-add/problem

# CODE
N=int(input())
res=set()
for i in range(N):
    s=input()
    res.add(s)
print(len(res))
