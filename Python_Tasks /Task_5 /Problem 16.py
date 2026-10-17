# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

# CODE
from collections import Counter
N=int(input())
shoe_arr=list(map(int,input().split()))
M=int(input())
shoe_counts=Counter(shoe_arr)
total_earned=0
for i in range(M):
    s,m=map(int,input().split())
    if shoe_counts[s]>0:
        total_earned+=m
        shoe_counts[s]-=1
print(total_earned)
        
