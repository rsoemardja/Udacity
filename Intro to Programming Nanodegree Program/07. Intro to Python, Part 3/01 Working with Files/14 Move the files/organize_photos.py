for filename in originals:
    place = extract_place(filename)
    os.rename(filename, os.path.join(place, filename))