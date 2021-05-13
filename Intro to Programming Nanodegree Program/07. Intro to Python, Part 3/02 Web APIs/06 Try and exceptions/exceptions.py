def takeoff():
    print(TAKEOFF)

try:
    print("3, 2, 1, ...")
    takeoff()
except NameError:
    print("Failed to launch")