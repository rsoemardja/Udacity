def word_triangle(word):
    # Add your code here
    length = len(word)
    for n in range(length):
        print(word[:length - n])