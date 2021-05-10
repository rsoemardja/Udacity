def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1
    return total

# Here's a call you can test it with. This should print 4:
# print(count_substring('love, love, love, all you need is love', 'love'))

# new version of solution
def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total

print(count_substring('AAAA'))