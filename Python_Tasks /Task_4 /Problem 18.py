# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

# CODE
if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        s=input().split()
        if s[0]=="insert":
            lst.insert(int(s[1]),int(s[2]))
        elif s[0]=="append":
            lst.append(int(s[1]))
        elif s[0]=="print":
            print(lst)
        elif s[0]=="remove":
            lst.remove(int(s[1]))
        elif s[0]=="sort":
            lst.sort()
        elif s[0]=="pop":
            lst.pop()
        elif s[0]=="reverse":
            lst.reverse()
            
            
