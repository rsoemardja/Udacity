while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if response == "waffles":
        print("Waffles it is!")
        break
    elif response == "pancakes":
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")