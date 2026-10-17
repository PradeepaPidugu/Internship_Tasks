# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

# CODE
import textwrap
def merge_the_tools(string, k):
    s=textwrap.fill(string,k)
    for sub in s.split("\n"):
        result=""
        for ch in sub:
            if ch not in result:
                result+=ch
        print(result)    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
