def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        index += 1
    return s[:index]