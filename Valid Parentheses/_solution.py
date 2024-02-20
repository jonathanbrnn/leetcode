inp = "({})"


def findValid(s):
    lst = []
    for char in s:
        lst.append(char)

    s = lst
    n = s

    if len(s) > 2:
        for index, char in enumerate(s):
            print(s)
            if index < len(s) - 1:
                match char:
                    case '(':
                        try:
                            if (s.index(')') - index) > 2 or (index + 1) - s.index(')') == 0:
                                n.remove(')')
                                n.remove('(')
                            else:
                                return False
                        except ValueError:
                            return False
                    case '[':
                        try:
                            if (s.index(']') - index) > 2 or (index + 1) - s.index(']') == 0:
                                n.remove(']')
                                n.remove('[')
                            else:
                                return False
                        except ValueError:
                            return False
                    case '{':
                        try:
                            if (s.index('}') - index) > 2 or (index + 1) - s.index('}') == 0:
                                n.remove('}')
                                n.remove('{')
                            else:
                                return False
                        except ValueError:
                            return False
    end = ''.join(n)
    match end:
        case '()':
            return True
        case '[]':
            return True
        case '{}':
            return True
        case _:
            return False


print(findValid(inp))
