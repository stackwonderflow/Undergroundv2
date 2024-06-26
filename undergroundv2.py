"""
This project was initially made for Code In Place 2022. 
Any new changes to the game will be marked as such by comments and 
new functionality will be summarized either here or in README.
"""

import random
import os

# These constants are used to determine the starting attack_stat and defence_stat for the user
MAX_START_STAT = 10
MIN_START_STAT = 2

def main():
    ### TODO 
    # Implement classes for user -> brawler, rouge, mage
    #   brawler - should be done
    #   rouge - implement combat -- arrows
    #   mage - implement combat -- raw magick
    # Implement different enemy types
    #   Golem - beefy monster with high starting health
    #   Imp - agile monster with lower health
    #   Slime - basic monster
    # Perhaps add art? 
    #   -- ascii art for combat? -- chat can help
    #   -- ascii dark tunnel for outside of combat? -- chat can help
    ###
    user_stats = {'attack_stat': 0, 'defence_stat': 0, 'health_stat': 20, 'class': 'none'}
    inventory = []
    items = ['rock', 'first aid kit']
    enemy_stats = {'attack_stat': 1, 'defence_stat': 1, 'health_stat': 5}
    user_win_count = 0
    in_combat = False
    intro(inventory) # Sends you into the game + gives you inventory
    get_stats(user_stats) # Sends player to class selection
    # Gamelogic: Begin game
    menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)

# This function clears the console when called
def clear_console():
    os.system('clear')

# This function contains the intro text and takes input from the user
def intro(inventory):
    print('\033[31m' + "This is a simple console game called 'Underground.'\nIn it, players can battle enemies that become progressively stronger after each encounter.\nPlayers can also collect items and use them. The random library is used to determine whether a player encounters enemies and items.\nIt is also used to determine whether a player is able to strike enemies, block enemy attacks, or flee from combat.\nThe game ends when a player's health_stat reaches zero." + '\033[0m')
    user_input = str(input("Press enter to continue. "))
    while user_input == '':
        break
    clear_console()
    print("A hooded figure appears before you.\nAh... you look lost. Welcome to the underground.")
    user_name = str(input("What is your name? "))
    print(f"Well, {user_name}, nice to meet you!\nTake this, you'll need it. I have to go now. Good luck to you!\n...\nThe hooded figure melts away into the darkness.\nWhat's this? They dropped a lantern...")
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

# New function for class selection -- need to finish implementation / test
def get_class(user_stats, inventory):
    print("Choose Your Class: Mage, Rouge, Brawler")
    user_input = str(input("Enter your selection to learn more. "))
    if user_input == 'Mage':
        print("Mages can inflict damage from a distance using a substance called 'Raw Magick.' Their natural affinity for magick allows them to draw on the enegry of their surroundings. Mages tend to have lower health and higher defence.")
        user_input = str(input("Would you like to be a Mage? (Y/N) "))
        if user_input == 'Y':
            user_stats['health_stat'] -= 10
            user_stats['defence_stat'] += 5
            user_stats['class'] = 'Mage'
            inventory.append('raw magick')
            inventory.append('raw magick')
        if user_input == 'N':
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)
        else:
            print("Please choose a valid selection.")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)
    if user_input == 'Rouge':
        print("Rouges prefer to avoid direct combat and weild bows. They can more easily flee from combat due to their preference for stealth.")
        user_input = str(input("Would you like to be a Rouge? (Y/N) "))
        if user_input == 'Y':
            user_stats['class'] = 'Rouge'
            inventory.append('arrow')
            inventory.append('arrow')
        if user_input == 'N':
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)
        else:
            print("Please choose a valid selection.")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)   
    if user_input == 'Brawler':
        print("Brawlers enjoy close quarters combat and fight with their bare hands. They tend to have higher health and attack.")
        user_input = str(input("Would you like to be a Brawler? (Y/N) "))
        if user_input == 'Y':
            user_stats['health'] += 10
            user_stats['attack'] += 5
            user_stats['class'] = 'Brawler'
        if user_input == 'N':
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)
        else:
            print("Please choose a valid selection.")
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            get_class(user_stats)   
    else:
        print("Please choose a valid class.")
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
        get_class(user_stats)


# New function to reduce redundancies in code
def defeat_enemy(enemy_stats, user_stats):
    print('\033[31m' + "You beat the enemy!" + '\033[0m')
    enemy_stats['health_stat'] = 0
    enemy_stats['attack_stat'] += 1
    enemy_stats['defence_stat'] += 1
    enemy_stats['health_stat'] += 10
    user_stats['attack_stat'] += 1
    user_stats['defence_stat'] += 1

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
            find_item(item_chance, inventory, items, user_stats)
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            print('\033[31m' + "1. Move\n2. Check Stats\n3. Check Inventory\n0. Quit" + '\033[0m')
            user_action = str(input("Choose an action: "))
        elif user_action == '2':
            check_user_stats(user_stats)
            print(f"Enemies Defeated: {user_win_count}")
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
def find_item(item_chance, inventory, items, user_stats):
    item_found = random.choice(items)
    if item_chance >= 0.6:
        print(f"You found a {item_found}!")
        inventory.append(item_found)
    elif item_chance >= 0.5 and user_stats['class'] == 'Rouge':
        print("You found an arrow!")
        inventory.append('arrow')
    elif item_chance >= 0.5 and user_stats['class'] == 'Mage':
        print("You found some raw magick")
        inventory.append('raw magick')
    else:
        return

"""
This function determines whether the user is able to flee from combat.
If yes, the user is directed back to the menu. If no, the user remains in combat.
"""
def flee(flee_chance, user_stats, inventory, enemy_stats, items, in_combat, user_win_count):
    if flee_chance >= 0.6:
        print("You were able to flee combat...")
        in_combat = False
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
        menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
    elif flee_chance >= 0.3 and user_stats['class'] == 'Rouge':
        print("You were able to flee combat...")
        in_combat = False
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
        menu(user_stats, inventory, enemy_stats, items, in_combat, user_win_count)
    else:
        print("You were not able to flee combat.")
        if flee_chance <= 0.2:
            print("You trip while trying to flee, minorly injuring yourself.")
            user_stats['health_stat'] -= 1

"""
This function determines whether the user is able to attack the enemy and how much damage is dealt.
Damage dealt is based off of the user's attack_stat and the enemy's defence_stat.
"""
def attack(attack_chance, user_stats, enemy_stats):
    if attack_chance >= 0.4:
        print("You strike the enemy...")
        if user_stats['attack_stat'] > enemy_stats['defence_stat']:
            print("You overcome the enemy's defence, inflicting damage.") # New description
            enemy_stats['health_stat'] -= (user_stats['attack_stat'] - enemy_stats['defence_stat'])
        elif user_stats['attack_stat'] < enemy_stats['defence_stat']:
            print("The enemy has the upper hand, you take damage.") # New description
            user_stats['health_stat'] -= (enemy_stats['defence_stat'] - user_stats['attack_stat'])
        else:
            print("You clash with the enemy and both take damage.") # New description
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You missed...")
        print("The enemy stikes you, inflicting damage.") # New description
        user_stats['health_stat'] -= enemy_stats['defence_stat']

"""
This function determines whether the user is able to defend against the enemy and how much damage is dealt.
Damage dealt is based off of the user's defence_stat and the enemy's attack_stat.
"""
def defend(defend_chance, user_stats, enemy_stats):
    if defend_chance >= 0.4:
        print("You block the enemy's blow...")
        if user_stats['defence_stat'] > enemy_stats['attack_stat']:
            print("You succesfully block and inflict damage on the enemy.") # New description
            enemy_stats['health_stat'] -= (user_stats['defence_stat'] - enemy_stats['attack_stat'])
        elif user_stats['defence_stat'] < enemy_stats['attack_stat']:
            print("The enemy has the upper hand, you take damage.") # New description
            user_stats['health_stat'] -= (enemy_stats['attack_stat'] - user_stats['defence_stat'])
        else:
            print("You clash with the enemy and both take damage.") # New description
            enemy_stats['health_stat'] -= 1
            user_stats['health_stat'] -= 1
    else:
        print("You failed to block the enemy's blow...")
        print("You take damage.")
        user_stats['health_stat'] -= enemy_stats['attack_stat']

# This function allow the user to use their collected items and removes them from the inventory if used.
def use_item(inventory, user_stats, enemy_stats, items, in_combat, user_win_count):
    user_choice = str(input("Which item will you use? (Or, press enter to exit.) "))
    if user_choice == 'first aid kit' and ('first aid kit' in inventory):
        print("You used the first aid kit...")
        user_stats['health_stat'] += 5
        print("You feel a bit better now!")
        inventory.remove('first aid kit') # Searches inventory list for element and removes it
        clear_console()
    elif user_choice == 'rock' and ('rock' in inventory) and in_combat == True:
        print("You throw the rock at the enemy...")
        rock_hit_chance = random.random()
        if rock_hit_chance >= 0.6:
            print("Bull's-eye!")
            enemy_stats['health_stat'] -= 5
            inventory.remove('rock')
            user_input = str(input("Press enter to continue. "))
            while user_input == '':
                break
            clear_console()
            if enemy_stats['health_stat'] <= 0:
                defeat_enemy(enemy_stats, user_stats)
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
                defeat_enemy(enemy_stats, user_stats)
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
        user_input = str(input("Press enter to continue. "))
        while user_input == '':
            break
        clear_console()
        use_item(inventory, user_stats, enemy_stats, items, in_combat, user_win_count)

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
            attack(attack_chance, user_stats, enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                defeat_enemy(enemy_stats, user_stats)
                user_win_count += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                in_combat = False
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
        elif user_action == '1' and user_stats['class'] == 'Rouge': # Needs to be finished
            break
        elif user_action == '1' and user_stats['class'] == 'Mage': # Needs to be finished
            break
        elif user_action == '2':
            print("You defend yourself...")
            defend_chance = random.random()
            defend(defend_chance, user_stats, enemy_stats)
            if enemy_stats['health_stat'] <= 0:
                defeat_enemy(enemy_stats, user_stats)
                user_win_count += 1
                user_input = str(input("Press enter to continue. "))
                while user_input == '':
                    break
                clear_console()
                in_combat = False
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