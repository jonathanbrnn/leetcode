testlist = [""]
lowercase = 'abcdefghijklmnopqrstuvwxyz'


def commonPrefixes(strs):
    prefix = ""
    if strs[0] != "":
        if 1 <= len(strs) <= 200:
            for index, char in enumerate(strs[0]):
                if all(char == word[index] for word in strs):
                    print(f"The current char is: {char}")
                    prefix += char
                else:
                    return prefix
        else:
            return prefix
    else:
        return prefix


print(commonPrefixes(testlist))
