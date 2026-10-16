# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# CODE
if __name__ == '__main__':
    n = int(input())
    arr =set(map(int, input().split()))
    res=sorted(arr)
    print(res[-2])
