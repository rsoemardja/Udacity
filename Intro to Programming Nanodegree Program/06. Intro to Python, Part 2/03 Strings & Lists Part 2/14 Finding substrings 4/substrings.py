def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total

# Here are a couple function calls to test with.

# This one should return 1
# print(locate_first('cookbook', 'ook'))

# This one should return -1
# print(locate_first('all your bass are belong to us', 'base'))
-1