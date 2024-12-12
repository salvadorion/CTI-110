# Leila Furman
# 11/21/2024
# P5HW
# Create a text-based game using functions

import random
import sys
import time


# setup

def create_character():
    # this is for the character's apprentice name 
    name = input("Enter your character's prefix!: ").strip().capitalize()
    suffix = "paw"
    charname = name + suffix

    # this is for the character's age, which should be between 12 and 18 moons (months)
    while True:
        try:
            age = int(input("Enter the character's age in moons (6-18): "))
            if 6 <= age <= 18:
                break  # exit the loop because the age is correct
            else:
                print("Age must be between 6 and 18. Please try again.")
        except ValueError:
            print("Please enter a number between 6 and 18.")

    # this one's so the program uses the right pronouns when its talking about the player's character
    while True:
        gender = input("Enter the character's gender (m for male, f for female, n for neutral): ").lower().strip()
        if gender in ['m', 'f', 'n']:
            break
        else:
            print("Invalid input. Please enter 'm', 'f', or 'n'.")
            
    # HIS PRONOUNS ARE SHE/THEY !!!!!
    pronouns = {
        "m": {"subject": "he", "object": "him", "possessive": "his"},
        "f": {"subject": "she", "object": "her", "possessive": "her"},
        "n": {"subject": "they", "object": "them", "possessive": "their"},
    }
    character_pronouns = pronouns[gender]
    # uses the random library to choose starting stats, which are all low at the start of the game obviously
    # additionally hardcodes "maximums" for all stats that cannot be exceeded
    initial_hp = random.randint(15, 30) # rolls for health stat
    character = {
        "name": charname,
        "age": age,
        "prns": character_pronouns,
        "HP": initial_hp, # health stat
        "MAX_HP": initial_hp,  # max health stat
        "ATK": random.randint(1, 5), # attack stat
        "MAX_ATK": 20, # max attack stat
        "DEF": random.randint(1, 5), # defense stat
        "MAX_DEF": 20, # max defense stat
        "AGI": random.randint(1, 5), # agility stat
        "MAX_AGI": 20, # max agility stat
        "SPD": random.randint(1, 5), # speed stat
        "MAX_SPD": 20, # max speed stat
        "STL": random.randint(1, 10), # stealth stat
        "MAX_STL": 40, # max stealth stat
    }
    return character

def display_character(character):
    print(f"Name: {character['name']}")
    print(f"Age: {character['age']}")
    print(f"Pronouns: {character['prns']['subject']} / {character['prns']['object']} / {character['prns']['possessive']}")
    print(f"HP: {character['HP']}/{character['MAX_HP']}")
    print(f"STL: {character['STL']}")

# increases hp without exceeding max hp; healing
def increase_hp(character, amount):
    character['HP'] = min(character['HP'] + amount, character['MAX_HP'])
    print(f"{character['name']} regained {amount} HP. Current HP: {character['HP']} / {character['MAX_HP']}")

# decreases hp without going beyond 0; taking damage
def decrease_hp(character, amount):
    character['HP'] = max(character['HP'] - amount, 0)
    print(f"{character['name']} lost {amount} HP. Current HP: {character['HP']} / {character['MAX_HP']}")

# increases maximum hp, capped at 100 hp
def increase_max_hp(character, amount):
    if character['MAX_HP'] < 100:
        old_max = character['MAX_HP']
        character['MAX_HP'] = min(character['MAX_HP'] + amount, 100)
        print(f"{character['name']}'s MAX_HP increased from {old_max} to {character['MAX_HP']}.")
    else:
        print(f"{character['name']} already has the maximum HP of 100!")

def increase_stat(character, stat, amount):
    # determine the corresponding max stat key
    max_stat_key = f"MAX_{stat}"
    
    # make sure its an actual stat and also compare it to the max of that stat
    if stat in character and max_stat_key in character:
        if character[stat] < character[max_stat_key]:
            # add to the stat without going over the limit
            character[stat] = min(character[stat] + amount, character[max_stat_key])
            print(f"{stat} increased by {amount}! Current {stat}: {character[stat]}")
        else:
            print(f"{stat} is already at its maximum value ({character[max_stat_key]}). No stat increase; great work!")
    else:
        print(f"Error: Stat '{stat}' or its max value is not defined for the character.")

# this function contains most of the gameplay 
def main_menu(character):
    print(f"{character['name']} is in camp.")
    print(f"Here are the things {character['prns']['subject']} can do:")
    print("1. Hunt")
    print("2. Explore")
    print("3. Train")
    print("4. Patrol")
    print("Type 'leave' or 'exit' to return to this menu.")
    print()

    while True:
        choice = input(f"What would you like {character['name']} to do? ").lower().strip()

        if choice in ['1', 'hunt']:
            hunting(character)
        elif choice in ['2', 'explore']:
            exploring(character)
        elif choice in ['3', 'train']:
            start_training(character)
        elif choice in ['4', 'patrol']:
            global enemy_encounter
            enemy_encounter = patrolling(character)
            if enemy_encounter == 3:
                break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# this function is for the hunting mechanic
def hunting(character):
    print(f"{character['name']} ventures out to hunt.")
    while True:
        # show only the character's hp and max hp
        print(f"\n{character['name']}'s current health:")
        print(f"HP: {character['HP']} / {character['MAX_HP']}")
        
        # hunting options + splash text to suggest stat boosts
        print(f"\nWhat would you like {character['name']} to hunt?")
        print("1. Mice (Always a good start for beginners!)")
        print(f"2. Squirrels (Catching one might make {character['name']} quicker!)")
        print(f"3. Birds (Perhaps this could improve {character['name']}'s reflexes?)")
        print(f"4. Snakes (Taking one down could sharpen {character['name']}'s strength!)")
        print("Type 'leave' or 'exit' to return to camp.")
        
        choice = input(f"Choose {character['name']}'s prey: ").lower().strip()
        
        if choice in ['leave', 'exit']:
            print("\nHeading back to camp...")
            break
        elif choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1, 2, 3, 4, or 'leave'.")
            continue

        prey = {
            '1': {"name": "Mice", "required_stealth": 1, "success_threshold": 7, "hp_gain": 1, "stat_gain": None},
            '2': {"name": "Squirrels", "required_stealth": 10, "success_threshold": 15, "hp_gain": 2, "stat_gain": "SPD"},
            '3': {"name": "Birds", "required_stealth": 20, "success_threshold": 25, "hp_gain": 5, "stat_gain": "AGI"},
            '4': {"name": "Snakes", "required_stealth": 30, "success_threshold": 38, "hp_gain": 10, "stat_gain": "ATK"},
        }
        target = prey[choice]

        # Check stealth recommendation
        if character['STL'] < target["required_stealth"]:
            print(f"\n{character['name']}'s stealth ({character['STL']}) is below the recommended {target['required_stealth']} for hunting {target['name']}.")
            print(f"{character['name']} can still try, but {character['prns']['possessive']} chances are lower.")

        # Hunting logic
        hunt_roll = random.randint(1, 10) + character['STL']
        print(f"\nHunting {target['name']}... (Roll + Stealth: {hunt_roll})")
        
        if hunt_roll >= target["success_threshold"]:
            print(f"Success! {character['name']} successfully hunted {target['name']}!")
            increase_hp(character, target["hp_gain"])  # heal hp (unless already maxed)
            if target["stat_gain"]:
                increase_stat(character, target["stat_gain"], 1)  # increases stats for different prey
            increase_stat(character, "STL", 1)  # increase stealth (unless already capped)
        else:
            print(f"Failed to hunt {target['name']}. Better luck next time!")
        
        again = input(f"\nWould you like {character['name']} to hunt again? (yes/no): ").lower().strip()
        if again not in ['yes', 'y']:
            print("\nHeading back to camp...")
            break

    # after hunting, return to the main menu
    main_menu(character)

def start_training(character):
    """Initiates a training session where the player selects a stat to train or activates debug mode."""
    print("Choose a stat to train: ")
    print("1. HP (Health Points)")
    print("2. ATK (Attack)")
    print("3. DEF (Defense)")
    print("4. AGI (Agility)")
    print("5. SPD (Speed)")
    
    # Placeholder for start training dialogue
    print(f"{character['name']} heads to the training hollow in order to sharpen {character['prns']['possessive']} skills!")
    
    choice = input("Enter the number of the stat to train: ").strip().lower()
    
    if choice == 'hid':
        print("The answer's 2, slayboss. Debug that thing")
        if training_action(equation_override=("1+1", 2)):  # Debug mode uses a fixed equation
            print("All stats maxed out!")
            for stat in ['ATK', 'DEF', 'AGI', 'SPD']:
                max_stat_key = f"MAX_{stat}"
                character[stat] = character[max_stat_key]
            character['MAX_HP'] = 100
            character['HP'] = 100
            return
    else:
        stat_map = {
            "1": "HP",
            "2": "ATK",
            "3": "DEF",
            "4": "AGI",
            "5": "SPD"
        }
        if choice in stat_map:
            stat_to_train = stat_map[choice]
            success = training_action()
            end_training(character, stat_to_train, success)
        else:
            print("Invalid choice. Please try again.")

    main_menu(character)

def training_action(equation_override=None):
    """Simulates the training action by presenting a math problem."""
    if equation_override:
        equation, solution = equation_override
    else:
        # Generate a random addition or subtraction problem
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-"])
        equation = f"{num1} {operation} {num2}"
        solution = eval(equation)  # Calculate the correct answer
    
    print(f"Solve this equation: {equation}")
    start_time = time.time()
    try:
        player_answer = int(input("Your answer: "))
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            print("Time's up!")
            return False
        if player_answer == solution:
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def end_training(character, stat_to_train, success):
    """Ends the training session and awards stats based on success."""
    if success:
        stat_increase = random.randint(1, 3)
        # Placeholder for successful training dialogue
        print(f"Congratulations! {character['name']} has learned a little bit more about what it means to be a warrior.")
        if stat_to_train == "HP":
            # Increase current HP but cap it at MAX_HP
            character["HP"] = min(character["HP"] + stat_increase, character["MAX_HP"])
            print(f"HP increased by {stat_increase}! Current HP: {character['HP']}/{character['MAX_HP']}")
        else:
            # Increase other stats normally
            increase_stat(character, stat_to_train, stat_increase)
    else:
        # Placeholder for failed training dialogue
        print(f"{character['name']} isn't quite sure {character['prns']['subject']} understood the training session this time...")
        print("No stat increase this time. Keep trying!")

# dictionaries for exploring encounters

landscape_features = {
    "trees": ["fallen log", "stump", "oak tree", "pine tree", "willow tree", "maple tree", "birch tree", "elm tree", "cedar tree", "chestnut tree"],
    "rocks": ["pebbles", "boulder", "outcropping", "cave"],
    "water": ["stream", "pond", "lake", "puddle"],
}

scavenged_items = {
    "herbs": [
        {"name": "catmint", "stat_boost": {"HP": 10}},
        {"name": "goldenrod", "stat_boost": {"AGI": 5}},
    ],
    "prey": [
        {"name": "fresh prey", "stat_boost": {"ATK": 5}},
    ],
    "moss": [
        {"name": "moss", "stat_boost": {"DEF": 3}},
    ],
}

friendly_encounters = {
    "cat_1": {
        "name": "Swiftstrike",
        "sentence": "Swiftstrike greets {character['name']} with a quick nod, offering advice on hunting.",
        "stat_boost": {"SPD": 2},
    },
    "cat_2": {
        "name": "Rosepetal",
        "sentence": "Rosepetal looks up and smiles, sharing some freshly caught prey.",
        "stat_boost": {"HP": 5},
    },
    "cat_3": {
        "name": "Lightningstar",
        "sentence": "Lightningstar rambles for a bit, and then offers {character['name']} a strange but well-meaning life lesson on seizing opportunities.",
        "stat_boost": {"ATK": 10},
    },
}


def get_article(word):
    """Return 'a' or 'an' based on whether the word starts with a vowel sound."""
    vowels = "AEIOUaeiou"
    if word[0] in vowels:
        return "an"
    else:
        return "a"



# this function is for the exploring mechanic
def exploring(character):
    while True:
        event_type = random.choice(["territory", "item", "cat"])

        if event_type == "territory":
            feature_type = random.choice(list(landscape_features.keys()))
            feature = random.choice(landscape_features[feature_type])
            article = get_article(feature)  # Get the article ('a' or 'an')
            print(f"\n{character['name']} has encountered {article} {feature} while wandering.")

        elif event_type == "item":
            item_type = random.choice(list(scavenged_items.keys()))
            item = random.choice(scavenged_items[item_type])  # Select a random item from the list
            print(f"\n{character['name']} found {item['name']}! {item['stat_boost']}")
            
        elif event_type == "cat":
            cat_key = random.choice(list(friendly_encounters.keys()))
            cat = friendly_encounters[cat_key]
            print(f"\n{cat['sentence']} You gained {cat['stat_boost']}.")

        # Prompt the player to explore again or return to camp
        choice = input(f"\nWould you like {character['name']} to explore again? (yes/no): ").lower().strip()
        if choice not in ['yes', 'y']:
            print("\nHeading back to camp...")
            break
        
    # after hunting, return to the main menu
    main_menu(character)


def generate_enemy(enemy_num):
    """Generates an enemy with stats based on the enemy number."""
    enemy_names = {
        1: ["Bluefoot", "Lizardtail", "Ratwhisker", "Rainclaw", "Owlpaw"],  # List of names for Enemy 1
        2: ["Weaselnose", "Badgerstrike", "Yellowfang", "Redtalon", "Hawkclaw"],  # Names for Enemy 2
        3: ["Ravenstar", "Darkstalker", "Brokenstar"]  # Names for Enemy 3
    }
    
    # Stat ranges for enemies
    enemy_stats = [
        {"HP": (20, 30), "ATK": (5, 7), "DEF": (5, 7), "AGI": (5, 7), "SPD": (5, 7)},
        {"HP": (40, 60), "ATK": (10, 12), "DEF": (10, 12), "AGI": (10, 12), "SPD": (10, 12)},
        {"HP": (70, 90), "ATK": (15, 18), "DEF": (12, 15), "AGI": (15, 18), "SPD": (15, 18)},
    ]
    
    if 1 <= enemy_num <= 3:
        stats = enemy_stats[enemy_num - 1]
        name = random.choice(enemy_names[enemy_num])  # Randomly select a name from the list
        return {
            "name": name,
            "HP": random.randint(*stats["HP"]),
            "MAX_HP": stats["HP"][1],
            "ATK": random.randint(*stats["ATK"]),
            "DEF": random.randint(*stats["DEF"]),
            "AGI": random.randint(*stats["AGI"]),
            "SPD": random.randint(*stats["SPD"]),
        }
    else:
        return None

enemy_encounter = 0

def patrolling(character):
    """Handles the patrolling logic."""
    global enemy_encounter
    print(f"{character['name']} goes out on patrol...")
    if random.choice([True, False]):  # 50% chance of encountering an enemy
        print(f"{character['name']} encountered an enemy!")
        if enemy_encounter < 3:  # Ensure enemies are fought in order
            enemy = generate_enemy(enemy_encounter + 1)
            print(f"Prepare to battle {enemy['name']}!")
            result = combat(character, enemy)
            if result == "win":
                print(f"{character['name']} defeated {enemy['name']} and returns to camp victorious!")
                enemy_encounter += 1
                if enemy_encounter == 3:  # Check for final boss defeat
                    print(f"\n>>> {character['name']} has defeated the final boss! <<<")
                    # Final Stats and Epilogue
                    print(f"Name: {character['name']}")
                    print(f"Age: {character['age']}")
                    print(f"Pronouns: {character['prns']['subject']} / {character['prns']['object']} / {character['prns']['possessive']}")
                    print(f"HP: {character['HP']}/{character['MAX_HP']}")
                    print(f"STL: {character['STL']}")
                    print(f"ATK: {character['ATK']}")
                    print(f"DEF: {character['DEF']}")
                    print(f"AGI: {character['AGI']}")
                    print(f"SPD: {character['SPD']}")
                    print(f"\n>>> {character['name']} is well on the path to becoming a warrior thanks to your help, and is certain {character['prns']['subject']} will get {character['prns']['possessive']} warrior name soon! <<<")
                    sys.exit()
            elif result == "lose":
                print(f"{character['name']} was defeated by {enemy['name']} and returned to camp injured, with 1 HP left.. Hunt to help regain {character['prns']['possessive']} health, and consider training up a bit!")
                character["HP"] = 1  # Reset player's HP after losing
            else:  # Flee scenario
                print(f"{character['name']} fled and returned to camp safely.")
        else:
            print(f"{character['name']} encountered no further enemies. {character['prns']['possessive']} patrol ends uneventfully.")
    else:
        print(f"{character['name']}'s patrol ends uneventfully.")
    return enemy_encounter

    main_menu(character)


def combat(character, enemy):
    """Handles turn-based combat between the player and an enemy."""
    print(f"--- Combat Start: {character['name']} vs {enemy['name']} ---")
    print(f"{enemy['name']} appears! HP: {enemy['HP']}/{enemy['MAX_HP']}")
    
    # Determine turn order
    player_turn = character["SPD"] >= enemy["SPD"]
    
    while character["HP"] > 0 and enemy["HP"] > 0:
        print(f"\n{character['name']} HP: {character['HP']} / {character['MAX_HP']}")
        print(f"{enemy['name']} HP: {enemy['HP']} / {enemy['MAX_HP']}")
        
        if player_turn:
            # Player's turn
            action = input("Choose an action: (A)ttack, (F)lee: ").strip().lower()
            if action == "a":
                damage = max(1, character["ATK"] - enemy["DEF"])  # Minimum 1 damage
                enemy["HP"] -= damage
                print(f"{character['name']} attacks {enemy['name']} for {damage} damage!")
            elif action == "f":
                print(f"{character['name']} flees the battle!")
                decrease_hp(character, 5)  # Optional fleeing penalty
                return "flee"
            else:
                print(f"Invalid action. {character['name']} hesitates!")
        else:
            # Enemy's turn
            damage = max(1, enemy["ATK"] - character["DEF"])  # Minimum 1 damage
            character["HP"] -= damage
            print(f"{enemy['name']} attacks {character['name']} for {damage} damage!")

        # Check for end of combat
        if enemy["HP"] <= 0:
            print(f"{character['name']} defeated {enemy['name']}!")
            return "win"
        elif character["HP"] <= 0:
            print(f"{character['name']} was defeated by {enemy['name']}...")
            return "lose"

        # Switch turns
        player_turn = not player_turn
    
def main():
    mc = create_character()
    print()
    display_character(mc)
    print()
    # splash text so the player has some context, although it relies on their knowledge of warrior cats
    print(f"{mc['name']} is an apprentice of ThunderClan who has recently turned {mc['age']} moons old. \
{mc['prns']['subject'].capitalize()} may not be very experienced yet, but that's where you come in! \
Get {mc['name']} ready to become a warrior by hunting, training, exploring the territory, or going on \
patrol. Keep an eye on {mc['prns']['possessive']} stats while you help {mc['prns']['object']} become \
the best ThunderClan warrior.")
    print()
    main_menu(mc)

if __name__ == "__main__":
    main()
    
