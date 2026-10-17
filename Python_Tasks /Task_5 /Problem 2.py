# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/copy-from/485399549

# CODE
def split_and_join(line):
    # write your code here
    s1=line.split()
    res="-".join(s1)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
