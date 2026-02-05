# (note: all # comments are for explanation purely for learning purposes)
import json # Importing the json module to handle JSON file operations
try:
    with open("save.json", "r") as file:   # "r" means read mode, with means auto-closes the file when done
        data = json.load(file)             # json.load reads JSON data from a file and converts it to a Python dictionary
        total_coins = data["total_coins"]  # ["total_coins"] accesses the value associated with the key "total_coins"
except (FileNotFoundError, json.JSONDecodeError): # If the file doesn't exist or is empty/corrupted
    total_coins = 0

print("Hello! This is your chibi Marin. (◕‿◕✿)")
print("Her status depends on how well you sleep!")

sleep_hours = float(input("\nPlease log how many hours you slept last night (numbers only): "))

if sleep_hours >= 8:
    print("Marin is energetic! (≧◡≦) ♡")
    mood = "energetic"
    coins_earned = 20
elif 6 <= sleep_hours < 8:
    print("Marin is content. (◕‿◕)")
    mood = "content"
    coins_earned = 10
elif 4 <= sleep_hours < 6:
    print("Marin is a bit tired. (－‸ლ)")
    mood = "tired"
    coins_earned = 5
else:
    print("Marin is very sleepy! (×_×;)")
    mood = "sleepy"
    coins_earned = 0

total_coins += coins_earned

print("\n--- Daily Summary ---")               # \n creates a new line
print(f"Mood: {mood}")                         # f-string lets us embed variables
print(f"Coins earned today: {coins_earned}")
print(f"Total coins: {total_coins}")

with open("save.json", "w") as file:   # "w" means create or overwrite the file
    json.dump({"total_coins": total_coins}, file)  # json.dump writes a Python dictionary to a file in JSON format