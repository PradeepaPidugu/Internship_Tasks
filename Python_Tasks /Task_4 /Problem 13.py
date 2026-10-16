# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# CODE
m=int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
res=s1^s2
for i in sorted(res):
    print(i)
