# Intrduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# CODE
def average(array):
    # your code goes here
    s=set(arr)
    avg=sum(s)/len(s)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
