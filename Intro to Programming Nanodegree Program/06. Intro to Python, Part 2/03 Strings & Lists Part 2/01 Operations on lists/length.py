# Add your code here.

# Should return 6:
# print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
# print(total_length([]))

# Should return 8:
# total_length(['balloons'])

# Should return 0 (it has four empty strings):
# >>> total_length(["", '', "", ''])

def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total