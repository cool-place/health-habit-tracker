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

from datetime import datetime, timedelta

def parse_time(time_str: str) -> datetime:
    """
    Accepts:
      - '3 am'
      - '3:00 am'
      - '08:55 am'
    Returns a datetime object (date is arbitrary).
    """
    s = time_str.strip().upper()   # no shift needed
    s = " ".join(s.split())        # squish extra spaces

    for fmt in ("%I:%M %p", "%I %p"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
        
    raise ValueError("Please enter time like '3 am or '3:00 am' or '08:55 am'.")

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
        try:
            bed_time = input("What time did you go to bed last night? (ex: 3 am or 3:00 am): ")
            wake_time = input("What time did you wake up? (ex: 8:55 am): ")

            bed_dt = parse_time(bed_time)
            wake_dt = parse_time(wake_time)
            if wake_dt <= bed_dt:
                wake_dt = wake_dt + timedelta(days=1)

            print(f"You went to bed at {bed_time} and woke up at {wake_time}.")
            sleep_duration = wake_dt - bed_dt
            hours_slept = round(sleep_duration.total_seconds() / 3600, 1)

            print(f"You slept about {hours_slept} hours.")
        
        except ValueError as e:
            print(e)
            continue  # Skip to the next iteration of the loop
    
        sleep_goal = 8.0
        difference = hours_slept - sleep_goal

        print(f"Sleep goal: {sleep_goal} hours")
        print(f"Difference: {round(difference, 1)} hours")
        if hours_slept >= 8:
            print("Marin is energetic! (≧◡≦) ♡")
            mood = "energetic"
            coins_earned = 20
        elif hours_slept >= 6:
            print("Marin is content. (◕‿◕)")
            mood = "content"
            coins_earned = 10
        elif hours_slept >= 4:
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