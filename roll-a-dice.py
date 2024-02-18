import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        dice1, dice2 = roll_dice()
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")

if __name__ == "__main__":
    main()