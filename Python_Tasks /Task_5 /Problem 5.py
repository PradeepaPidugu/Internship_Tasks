# String Validators
# https://www.hackerrank.com/challenges/string-validators/copy-from/485397887

# CODE
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s)) 
    print(any(c.isalpha() for c in s)) 
    print(any(c.isdigit() for c in s)) 
    print(any(c.islower() for c in s)) 
    print(any(c.isupper() for c in s))
