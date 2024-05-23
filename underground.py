"""
This is a simple console game called 'Underground.' 
In it, players can battle enemies that become progressively stronger.
Players can also collect items and use them. The random library is used to determine whether a player encounters enemies and items. 
It is also used to determine whether a player is able to strike enemies, block enemy attacks, or flee from combat.
The game ends when a player's health_stat reaches zero.
"""

import random
import os

# These constants are used to determine the players starting attack_stat and defence_stat
MAX_START_STAT = 10
MIN_START_STAT = 2

def main():
    ### TODO 
    # Implement classes for user -> enemy:user
    # 
    ###
    user_stats = {'attack_stat': 0, 'defence_stat': 0, 'health_stat': 20}
    inventory = []
    items = ['rock', 'first aid kit']
    enemy_stats = {'attack_stat': 1, 'defence_stat': 1, 'health_stat': 5}
    user_win_count = 0
    in_combat = False
    intro(inventory) # Sends you into the game + gives you inventory
    # Gamelogic: Begin game # Game gives you an inventory
    get_stats(user_stats)
    menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)

# This function clears the console when called
def clear_console():
    os.system('clear')

# This function contains the Intro text and takes input from the user
def intro(inventory):
    print('\033[31m' + "This is a simple console game called 'Underground.'\nIn it, players can battle enemies that become progressively stronger after each encounter.\nPlayers can also collect items and use them. The random library is used to determine whether a player encounters enemies and items.\nIt is also used to determine whether a player is able to strike enemies, block enemy attacks, or flee from combat.\nThe game ends when a player's health_stat reaches zero." + '\033[0m')
    user_input = str(input("Press enter to continue. "))
    while user_input == '':
        break
    clear_console()
    print("A hooded figure appears before you.\nAh... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name} , nice to meet you!\nTake this, you'll need it. I have to go now. Good luck to you!\n...\nThe hooded figure melts away into the darkness.\nWhat's this? They dropped a lantern...")
    user_input = str(input("Well, I guess I'm on my own now... \nPress enter to continue."))
    inventory.append('lantern') # Adds new element 'lantern' to the inventory list
    while user_input == '':
        break
    clear_console()
"""
This function uses random.randint to get the user's starting stats.
Starting stats are in the range MIN_START_STAT AND MAX_START_STAT inclusively.
"""
def get_stats(user_stats):
    user_stats['attack_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)
    user_stats['defence_stat'] = random.randint(MIN_START_STAT, MAX_START_STAT)

# This function contains the game menu.
def menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count):
    print("What should I do?")
    print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m') # Red text
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You move forward in the darkness...")
            enemy_encounter_chance = random.random()
            item_chance = random.random()
            enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items, user_win_count)
            find_item(item_chance, inventory, items)
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            check_user_stats(user_stats)
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, items, in_combat, user_win_count)
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '0':
            print(f"You defeated {user_win_count} enemies.")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            quit()
        else:
            print("I don't think I can do that...")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
            
# This function prints user stats.
def check_user_stats(user_stats):
    print(f"Your Stats\nAttack: {user_stats['attack_stat']} | Defence: {user_stats['defence_stat']} | Health: {user_stats['health_stat']}")

# This function prints enemy stats.
def check_enemy_stats(enemy_stats):
    print(f"Enemy Stats\nAttack: {enemy_stats['attack_stat']} | Defence: {enemy_stats['defence_stat']} | Health: {enemy_stats['health_stat']}")

# This function determines if the user encounters an enemy. If yes, the user enters combat.
def enemy_encounter(user_stats, enemy_stats, enemy_encounter_chance, inventory, items, user_win_count):
    if enemy_encounter_chance >= 0.5:
        combat(user_stats, enemy_stats, inventory, items, user_win_count)
        print("An enemy approaches you.")
    else:
        print("...")

# This function determines if the user encounters an item. If yes, it is added to the user's inventory.
def find_item(item_chance, inventory, items):
    item_found = random.choice(items)
    if item_chance >= 0.4:
        print(f"You found a {item_found}!")
        inventory.append(item_found)
    else:
        return

"""
This function determines whether the user is able to flee from combat.
If yes, the user is directed back to the menu. If no, the user remains in combat.
"""
def flee(flee_chance, user_stats, inventory, enemy_stats, items, in_combat):
    if flee_chance >= 0.5:
        print("You were able to flee combat...")
        in_combat = False
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
        menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
    else:
        print("You were not able to flee combat.")
        user_stats['health_stat'] -= 1

"""
This function determines whether the user is able to attack the enemy and how much damage is dealt.
Damage dealt is based off of the user's attack_stat and the enemy's defence_stat.
"""
def attack(attack_chance, user_stats, enemy_stats, check_enemy_stats):
    if attack_chance >= 0.4:
        print("You strike the enemy...")
        if user_stats['attack_stat'] > enemy_stats['defence_stat']:
            enemy_stats['health_stat'] -= (user_stats['attack_stat'] - enemy_stats['defence_stat'])
        elif user_stats['attack_stat'] < enemy_stats['defence_stat']:
            user_stats['health_stat'] -= (enemy_stats['defence_stat'] - user_stats['attack_stat'])
        else:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You missed...")
        user_stats['health_stat'] -= enemy_stats['defence_stat']

"""
This function determines whether the user is able to defend against the enemy and how much damage is dealt.
Damage dealt is based off of the user's defence_stat and the enemy's attack_stat.
"""
def defend(defend_chance, user_stats, enemy_stats, check_enemy_stats):
    if defend_chance >= 0.4:
        print("You block the enemy's blow...")
        if user_stats['defence_stat'] > enemy_stats['attack_stat']:
            enemy_stats['health_stat'] -= (user_stats['defence_stat'] - enemy_stats['attack_stat'])
        elif user_stats['defence_stat'] < enemy_stats['attack_stat']:
            user_stats['health_stat'] -= (enemy_stats['attack_stat'] - user_stats['defence_stat'])
        else:
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You failed to block the enemy's blow...")
        user_stats['health_stat'] -= enemy_stats['attack_stat']

# This function allow the user to use their collected items and removes them from the inventory if used.
def use_item(inventory, user_stats, enemy_stats, items, in_combat, user_win_count):
    user_choice = str(input("Which item will you use? (Or, press enter to exit.) "))
    if user_choice == 'first aid kit' and ('first aid kit' in inventory):
        print("You used the first aid kit...")
        user_stats['health_stat'] += 5
        print("You feel a bit better now!")
        inventory.remove('first aid kit') # Searches inventory list for element and removes it
    elif user_choice == 'rock' and ('rock' in inventory) and in_combat == True:
        print("You throw the rock at the enemy...")
        rock_hit_chance = random.random()
        if rock_hit_chance >= 0.7:
            print("Bull's-eye!")
            enemy_stats['health_stat'] -= 5
            inventory.remove('rock')
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                enemy_stats['health_stat'] = 0
                user_win_count += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                in_combat = False
                menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
        elif rock_hit_chance >= 0.4:
            print("You hit the enemy!")
            enemy_stats['health_stat'] -= 2
            inventory.remove('rock')
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                enemy_stats['health_stat'] = 0
                user_win_count += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                in_combat = False
                menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
        else:
            print("You missed...")
            inventory.remove('rock')
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
    elif user_choice == 'rock' and ('rock' in inventory) and in_combat == False:
        print("Maybe I should save this for a fight...")
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
    elif user_choice == 'lantern':
        print("You hold up the lantern and examine your surroundings...")
        print("What is this place?")
    elif user_choice == '':
        return
    else: 
        print("I don't think I can do that...")
        user_choice = str(input("Which item will you use? "))

"""
This function allows the user to fight enemies.
If the user wins, their stats increase and the next enemy encountered will have increased stats.
If the user loses, the game ends.
"""
def combat(user_stats, enemy_stats, inventory, items, user_win_count):
    user_input = str(input("Press enter to continue. "))
    while user_input == '':
        break
    clear_console()
    in_combat = True
    print("An enemy approaches you.")
    print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
    print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
    user_action = str(input("Choose an action: "))
    while user_action != '':
        if user_action == '1':
            print("You attack the enemy...")
            attack_chance = random.random()
            attack(attack_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                enemy_stats['health_stat'] = 0
                user_win_count += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                user_stats['attack_stat'] += 1
                user_stats['defence_stat'] += 1
                menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
            elif user_stats['health_stat'] <= 0:
                print('\033[31m' + "You have died..." + '\033[0m')
                print(f"You defeated {user_win_count} enemies.")
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                quit()
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            print("You defend yourself...")
            defend_chance = random.random()
            defend(defend_chance, user_stats, enemy_stats, check_enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                print('\033[31m' + "You beat the enemy!" + '\033[0m')
                enemy_stats['health_stat'] = 0
                user_win_count += 1
                in_combat = False
                enemy_stats['attack_stat'] += 1
                enemy_stats['defence_stat'] += 1
                enemy_stats['health_stat'] += 10
                user_stats['attack_stat'] += 1
                user_stats['defence_stat'] += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
            elif user_stats['health_stat'] <= 0:
                print('\033[31m' + "You have died..." + '\033[0m')
                print(f"You defeated {user_win_count} enemies.")
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                quit()
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '3':
            print(f"Inventory: {inventory}")
            use_item(inventory, user_stats, enemy_stats, items, in_combat, user_win_count)
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '4':
            check_user_stats(user_stats)
            check_enemy_stats(enemy_stats)
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: ")) 
        elif user_action == '5':
            print("You attempt to flee...")
            flee_chance = random.random()
            flee(flee_chance, user_stats, inventory, enemy_stats, items, in_combat)
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '0':
            print(f"You defeated {user_win_count} enemies.")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            quit()
        else:
            print("I don't think I can do that...")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print(f"Your Health: {user_stats['health_stat']} | Enemy Health: {enemy_stats['health_stat']}")
            print('\033[31m' + "1. Attack\n2. Defend\n3. Use Item\n4. Check Stats\n5. Flee\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))

if __name__ == "__main__":
    main()