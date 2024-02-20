s = 'Hello World      '

def lengthOfLastWord(input):
    l = len(input.split()[-1])
    print(l)

lengthOfLastWord(s)