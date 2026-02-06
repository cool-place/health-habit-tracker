# (note: all # comments are for explanation purely for learning purposes)
import json # Importing the json module to handle JSON file operations
try:
    with open("save.json", "r") as file:   # "r" means read mode, with means auto-closes the file when done
        data = json.load(file)             # json.load reads JSON data from a file and converts it to a Python dictionary
        total_coins = data.get("total_coins", 0)  # .get() retrieves the value for "total_coins", defaulting to 0 if not found
        mood = data.get("mood", "content")  # .get() retrieves the value for "mood", defaulting to "content" if not found
except (FileNotFoundError, json.JSONDecodeError): # If the file doesn't exist or is empty/corrupted
    total_coins = 0
    mood = "content"

print("Hello! This is your chibi Marin. (◕‿◕✿)")
print("Her status depends on how well you sleep!")

running = True

while running:
    print("\nWhat would you like to do?")
    print("1. Log sleep hours.")
    print("2. View status and total coins.")
    print("3. Exit.")

    choice = input("Enter the number of your choice: "
                   ).strip()  # .strip() removes any extra whitespace/newline characters
    if choice == "1":
        sleep_hours = float(input("\nPlease log how many hours you slept last night (numbers only): "))

        if sleep_hours >= 8:
            print("Marin is energetic! (≧◡≦) ♡")
            mood = "energetic"
            coins_earned = 20
        elif sleep_hours >= 6:
            print("Marin is content. (◕‿◕)")
            mood = "content"
            coins_earned = 10
        elif sleep_hours >= 4:
            print("Marin is a bit tired. (－‸ლ)")
            mood = "tired"
            coins_earned = 5
        else:
            print("Marin is very sleepy! (×_×;)")
            mood = "sleepy"
            coins_earned = 0

        total_coins += coins_earned # Update total coins

        print("\n--- Daily Summary ---")               # \n creates a new line
        print(f"Mood: {mood}")                         # f-string lets us embed variables
        print(f"Coins earned today: {coins_earned}")
        print(f"Total coins: {total_coins}")

        with open("save.json", "w") as file:
            json.dump({"total_coins": total_coins, "mood": mood}, file)  # Save progress after logging sleep

    elif choice == "2":
        print(f"\nStatus is {mood}. Total coins: {total_coins}")
    elif choice == "3":
        print("Goodbye! See you next time. (＾▽＾)")
        running = False
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")