print("Hello World!")

# just writing something
while True:
    answer = input("Choose your Class: Melee Ranged Magic\n")
    if answer.lower() not in ("melee", "ranged", "magic"):
        print("Input not understood.\n")
    else:
        print(f"You selected {answer}!")
        break
    





