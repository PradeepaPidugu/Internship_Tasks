# Piling  Up! 
# https://www.hackerrank.com/challenges/piling-up/problem

# CODE
for _ in range(int(input())):
    n=int(input())
    cubes=list(map(int,input().split()))
    
    left=0
    right=n-1
    last=float("inf")
    
    while left<=right:
        if cubes[left]>=cubes[right]:
            current=cubes[left]
            left+=1
        else:
            current=cubes[right]
            right-=1
        if current>last:
            print("No")
            break
            
        last=current
    else:
        print("Yes")
