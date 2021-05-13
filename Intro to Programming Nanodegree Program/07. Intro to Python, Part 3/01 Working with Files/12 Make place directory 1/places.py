import os

def extract_place(filename):
    return filename.split('_')[1]

os.chdir("Photos")
originals = os.listdir()
places = []
# Add the loop here!
for filename in originals:
    place = extract_place(filename)
    places.append(place)
# When you're done, this line should print a list of place names:
print(places)