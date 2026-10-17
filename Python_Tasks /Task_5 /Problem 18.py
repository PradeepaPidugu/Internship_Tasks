# The Minions Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

# CODE
def minion_game(string):
    # your code goes here
    Stuart=0
    Kevin=0
    n=len(string)
    for i in range(n):
        if string[i] in "AEIOU":
            Kevin+=n-i
        else:
            Stuart+=n-i
    if Stuart>Kevin:
        print("Stuart",Stuart)
    elif Kevin>Stuart:
        print("Kevin",Kevin)
    else:
        print("Draw")
                    
if __name__ == '__main__':
    s = input()
    minion_game(s)
