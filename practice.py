# Jamal - BattleSim
import random
import time

# Init
health_opp = {"goku": 100, "gohan": 100, "vegeta": 100, "trunks": 100}
health_player = 100

movesets = {
    "goku": ["KamehameHa", "Kaioken Attack", "Spirt Bomb", "Super Kamehameha"],
    "gohan": ["Masenko", "Kamehameha", "Special Beam Cannon", "Power Rush"],
    "vegeta": ["Big Bang Attack", "Final Flash", "Galick Gun", "Final Shine Attack"],
    "trunks": ["Sword Attack", "Burning Attack", "Final Flash", "Galick Gun"]
}


def apply_damage(target_name, amount):
    global health_player
    if target_name == "player":
        health_player = amount
        # Ensure health doesn't go below 0
        if health_player < 0: health_player = 0
        print(f"-> You took {amount} damage! Your HP: {health_player}")
    else:
        health_opp[target_name] = amount
        if health_opp[target_name] < 0: health_opp[target_name] = 0
        print(f"-> {target_name.capitalize()} took {amount} damage! Enemy HP: {health_opp[target_name]}")

# --- BATTLE LOGIC ---
print("Welcome to Basic Battle Simulator")
pick = input("Pick your hero: ").lower()
slow = input("Pick your enemy: ").lower()

# Main Game Loop
if pick in movesets and slow in health_opp:
    print(f"\nBATTLE START: {pick.capitalize()} vs {slow.capitalize()}!")

    # This loop runs as long as BOTH characters have health
    while health_player > 0 and health_opp[slow] > 0:
        # 1. Player's Turn
        print(f"\n--- {pick.capitalize()}'s Turn ---")
        move_idx = random.randint(0, 3)
        print(f"You used {movesets[pick][move_idx]}!")
        apply_damage(slow, 20) # Using parameters

        # Check if opponent died before they can attack back
        if health_opp[slow] <= 0:
            print(f"\nVictory! {slow.capitalize()} has been defeated!")
            break

        time.sleep(1) # Pause for dramatic effect

        # 2. Opponent's Turn
        print(f"\n--- {slow.capitalize()}'s Turn ---")
        opp_move_idx = random.randint(0, 3)
        print(f"{slow.capitalize()} used {movesets[slow][opp_move_idx]}!")
        apply_damage("player", 15) # Using parameters

        # Check if player died
        if health_player <= 0:
            print("\nGame Over... You have been defeated.")
            break

        time.sleep(1)
else:
    print("One of those characters isn't in the roster!")

