def too_long(s):
    length = len(s)
    if length > 140:
        return True
    else:
        return False

# another solution
def too_long(s):
    return len(s) > 140

# Apparently you can print emoji's
import unicodedata
unicodedata.lookup("snake")