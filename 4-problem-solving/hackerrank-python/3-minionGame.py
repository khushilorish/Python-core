def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    v =0
    c=0
    n = len(string)
    for i in range(n):
        if string[i] in vowel:
            v += n-i
        else:
            c += n-i
    if((v) > (c)):
        print("Kevin",v)
    elif ((v) < (c)):
        print("Stuart",c)
    else:
        print("Draw")

print("Enter string: ")
s = input()
minion_game(s)