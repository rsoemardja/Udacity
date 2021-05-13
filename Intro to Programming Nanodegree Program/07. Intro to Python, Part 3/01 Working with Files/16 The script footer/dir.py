import os

def extract_place(filename):
    return filename.split('_')[1]

# Add the make_place_directories function here!
def make_place_directories(places):
    for place in places:
        os.mkdir(place)

os.chdir("Photos")
originals = os.listdir()
places = []
for filename in originals:
    place = extract_place(filename)
    places.append(place)

# Call the function here!
make_place_directories(places)
# Let's use os.listdir to check that all the directories are there:
print(os.listdir())