name = input("Enter your name: ")

print(f"Greetings {name}!")

start = input("Would you rather play the game or perish? ")

if start == "play":
    print("You're funeral...let us begin!")
    setting = input("Jungle or desert? ")
else:
    print("GAME OVER!")
    quit()

if setting