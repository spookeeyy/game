from random import randint

# variables
hearts = 10
coins = 0
win_amount = 150

inventory = []
# Item IDs:
# Sword
# Mushroom
# Golden Apple

left = False

# statistics variables
dangers_encountered = 0

items_picked_up = 0
items_ignored = 0
items_used = 0

swords_found = 0
swords_used = 0
swords_broken = 0

edible_mushrooms_eaten = 0
edible_mushrooms_sold = 0
poisonous_mushrooms_eaten = 0
poisonous_mushrooms_sold = 0

golden_apples_found = 0
golden_apples_eaten = 0

# functions
def pick(item, text=None):
    # pick up items
    global items_picked_up
    global items_ignored
    
    if text != None: # if text variable is not specified do not print it
        print(text, "Do you want to:")
    
    else: # if it is then print it
        print("Do you want to:")
    
    print("1) Pick " + item + " up and store it in the inventory")
    print("2) Ignore it")
    options_text = "(1, 2)"
    
    if item == "Mushroom" or item == "Golden Apple": # if the item is a consumable, add a third option
        if item == "Mushroom":
            print("3) Eat or Sell the Mushroom")
        else:
            print("3) Eat the " + item)
        
        options_text = "(1, 2, 3)"
    
    print("What do you want to do?")
    
    while True: # keep repeating until a correct choice has been chosen
        choice = input(options_text + " > ")
        
        if choice.isnumeric(): # if the string is a number
            choice = int(choice) # turn string into number
            
            if choice == 1:
                inventory.append(item)
                print("+ " + item)
                items_picked_up += 1
                break
            
            elif choice == 2:
                print("You chose to leave the " + item + " as it is.")
                items_ignored += 1
                break
            
            elif choice == 3 and (item == "Mushroom" or item == "Golden Apple"): # if choice is 3 and the item is a consumable
                inventory.append(item)
                print("+ " + item)
                
                if item == "Mushroom":
                    use_mushroom()
                
                elif item == "Golden Apple":
                    use_golden_apple()
                
                break
        
        print("Invalid choice, please select between " + options_text + ".") # if the loop doesn't break, inform the user a wrong choice was given

def use(item, text=None):
    # use an item and remove it from the inventory 
    global items_used
    
    if text != None: # if text is specified, print it
        print(text)
    
    inventory.remove(item)
    print("- " + item)
    items_used += 1

def use_sword():
    # use a sword with a 1/6 chance of breaking
    global items_used
    global swords_used
    global swords_broken
    swords_used += 1
    
    if randint(1, 6) == 1:
        use("Sword", "Your sword broke!")
        swords_broken += 1
    
    else:
        items_used += 1

def use_mushroom():
    # eat or sell a mushroom
    global coins
    global hearts
    global edible_mushrooms_eaten
    global poisonous_mushrooms_eaten
    global edible_mushrooms_sold
    global poisonous_mushrooms_sold
    
    print("Do you want to:")
    print("1) Eat the mushroom")
    print("2) Sell it")
    poisonous = (randint(1, 3) == 1) # if random number is 1, True otherwise False
    
    while True: # keep repeating until a correct choice has been chosen
        choice = input("(1, 2) > ")
        
        if choice.isnumeric(): # if the string is a number
            choice = int(choice) # turn string into number
            
            if choice == 1:
                if poisonous:
                    print("You chose to eat a mushroom, but it turned out to be poisonous. You lost 1 heart.")
                    hearts -= 1
                    poisonous_mushrooms_eaten += 1
                
                else:
                    hearts_gained = randint(2, 6)
                    print("You ate the mushroom and gained " + str(hearts_gained) + " hearts.")
                    hearts += hearts_gained
                    edible_mushrooms_eaten += 1
                
                break
            
            elif choice == 2:
                if poisonous:
                    print("The mushroom seems to be poisonous. It's worthless. You sold it for a mere 0 coins.")
                    poisonous_mushrooms_sold += 1
                
                else:
                    if randint(1, 5) < 5:
                        coins_gained = randint(1, 3)
                        print("The mushroom is edible and was sold for " + str(coins_gained) + " coins.")
                        coins += coins_gained
                    
                    else:
                        coins_gained = randint(5, 20)
                        print("JACKPOT! You found a rare mushroom which was sold for " + str(coins_gained) + " coins!")
                        coins += coins_gained
                    
                    edible_mushrooms_sold += 1
                
                break
        
        print("Invalid choice, please select between (1, 2).") # if the loop doesn't break, inform the user a wrong choice was given
    
    use("Mushroom")

def use_golden_apple(dangerous=False):
    # eat a golden apple
    global hearts
    global golden_apples_eaten
    
    hearts_gained = randint(3, 12)
    if not dangerous:
        print("You ate the golden apple and gained " + str(hearts_gained) + " hearts.")
    else:
        print("You ate the golden apple and gained " + str(hearts_gained) + " hearts and are free from the danger.")
    
    hearts += hearts_gained
    golden_apples_eaten += 1
    use("Golden Apple")

def options(other_option="Keep exploring the forest.", other_option_chosen="You decided to keep exploring.", fight_bear=False, fight_wolves=False, dangerous=False):
    # display options for specific events
    global left
    global coins
    global hearts
    
    options_ = []
    print()
    print("Do you want to:")
    
    if fight_bear and "Sword" in inventory:
        print(str(len(options_) + 1) + ") Use Sword against bear")
        options_.append("sword on bear")
    
    if fight_wolves and "Sword" in inventory:
        print(str(len(options_) + 1) + ") Use Sword against the wolves")
        options_.append("sword on wolves")
    
    if fight_bear:
        print(str(len(options_) + 1) + ") Go see what the bear wants")
        options_.append("see bear")
    
    if fight_wolves:
        print(str(len(options_) + 1) + ") Go see what the wolves want")
        options_.append("see wolves")
    
    if "Mushroom" in inventory:
        print(str(len(options_) + 1) + ") Consume or Sell Mushroom (" + str(inventory.count("Mushroom")) + ")")
        options_.append("mushroom")
    
    if "Golden Apple" in inventory:
        print(str(len(options_) + 1) + ") Consume Golden Apple (" + str(inventory.count("Golden Apple")) + ")")
        options_.append("golden apple")
    
    if not (fight_bear or fight_wolves):
        print(str(len(options_) + 1) + ") " + other_option)
        options_.append("other")
    
    if len(options_) == 1:
        options_text = "(1)"
    elif len(options_) == 2:
        options_text = "(1, 2)"
    elif len(options_) == 3:
        options_text = "(1, 2, 3)"
    elif len(options_) == 4:
        options_text = "(1, 2, 3, 4)"
    
    while True: # keep repeating until a correct choice has been chosen
        choice = input(options_text + " > ")
        print()
        
        if choice == "leave":
            # leave the forest
            left = True
            return
        
        elif choice == "inventory":
            # show inventory
            show_inventory()
            return
        
        elif choice.isnumeric() and int(choice) > 0 and int(choice) <= len(options_): # if choice string is a number and choice number is > 0 and choice number is less than or equal to number of all available options
            choice = options_[int(choice) - 1] # choose the option and set it as choice variable
            
            if choice == "sword on bear":
                if not dangerous:
                    print("The poor bear just wanted a hug... It got scared and ran away after seeing your sword.")
                    
                    coin_drop = randint(1, 3)
                    if coin_drop > 1:
                        coins_dropped = randint(1, 15)
                        print("Looks like the bear had a few coins that got left behind while running away. You gained " + str(coins_dropped) + " coins.")
                        coins += coins_dropped
                
                else:
                    print("The bear dodged your attack and dealt 5 hearts of damage.")
                    hearts -= 5
                
                use_sword()
                return False # inform main code to break the loop
            
            elif choice == "sword on wolves":
                wolves_action = randint(1, 2)
                
                if not dangerous and wolves_action == 1:
                    print("The wolves just wanted to say hi, they ran away after seeing your sword.")
                
                elif not dangerous and wolves_action == 2:
                    print("You slay your sword at the wolves, they seem to fear your sword.")
                
                else:
                    print("The wolves dodge your attack and launch at you.")
                    print("You got bit by the wolves and lost 4 hearts.")
                    hearts -= 4
                
                use_sword()
                return False # inform main code to break the loop
            
            elif choice == "see bear" or choice == "see wolves":
                return True # inform main code to break the loop and go see that animal
            
            elif choice == "mushroom":
                use_mushroom()
            
            elif choice == "golden apple" and (fight_bear or fight_wolves):
                use_golden_apple(dangerous=dangerous)
                
                if not dangerous:
                    if fight_bear:
                        coins_gained = randint(1, 15)
                        print("Aww! The bear just wants a hug! It gave you " + str(coins_gained) + " coins as a thank you gift.")
                        coins += coins_gained
                    
                    elif fight_wolves:
                        coins_gained = randint(1, 20)
                        print("The wolves are so cute! They just wanted some company.")
                        print("Oh look they even got some coins to share! You got " + str(coins_gained) + " coins from the wolves.")
                        coins += coins_gained
                
                return False # inform main code to break the loop
            
            elif choice == "golden apple":
                use_golden_apple()
            
            elif choice == "other":
                print(other_option_chosen)
                return True # inform main code to break the loop
            
            break
            
        else:
            print("Invalid choice, please select between " + options_text + ".") # inform the user the choice given was not valid

def show_stats(show_coins=True):
    # show health and coins
    
    if hearts > 0:
        print("â¤ï¸" * hearts)
    print("â¤ï¸ Hearts: " + str(hearts))
    
    if show_coins:
        print("ðŸ’° Coins: " + str(coins))

def show_inventory():
    # show inventory and coins
    
    text = ""
    
    if "Sword" in inventory:
        text += "ðŸ—¡ï¸ Sword x" + str(inventory.count("Sword")) + "\n"
    
    if "Mushroom" in inventory:
        text += "ðŸ„ Mushroom x" + str(inventory.count("Mushroom")) + "\n"
    
    if "Golden Apple" in inventory:
        text += "ðŸ Golden Apple x" + str(inventory.count("Golden Apple")) + "\n"
    
    if text == "":
        text = "Inventory is empty.\n"
    
    print(text, end="")
    print("ðŸ’° Coins: " + str(coins))

def advance():
    # advance into story more
    input("> Press enter to advance into the story... ")

# start
print("Forest Adventures. - a story game by spooky")

name = input("Enter your name: ").strip() # get name and strip it
if name == "": # if name was not given, default to FireInTheHole
    name = "FireInTheHole"

# main storyline
print()
print("There was a man named " + name + """ who was just exploring around his town, and he stumbled upon a forest. Maybe he's paranoid of this place? He decided to go and explore the forest.

Upon entering the forest, he found a poisonous mushroom. He didn't know that it was poisonous, but hunger got the best of him, so he decided to eat it. (He lost 1 heart)

He kept on walking, randomly damaging himself. Then he found a bear who he didn't know if it was friendly or not.

He kept on exploring the forest, but he heard branches crack behind him. He decided to check his left and right, and his shoulder one more time. He thought, "Maybe I'm a schizophrenic; I be fearing for my heart." After checking, there was no one. Maybe he really is a schizophrenic. Then he decided to check one last time, and there was an angry bear behind him, which damaged him. (He lost 1 heart)

After that, he keeps on walking. (What did you expect, bruh?) He keeps randomly damaging himself. (Which took 2 of his hearts)""")
print()
print("You are the man in the story. Your goal is to find a way out of the forest.")
print("Type 'leave' to leave the forest and to quit the game.")
print("Type 'inventory' to see the inventory.")
print()

# Lore starts
print("You walked into the forest.")

# starter item
pick("Sword", "You found another traveller's sword.")
swords_found += 1

while hearts > 0 and coins < win_amount and not left: # if hearts are > 0 or coins are less than the win amount of user has not left the game, keep looping
    print()
    show_stats() # show health and coins
    
    while True:
        explore = options() # prompt options
        
        if left: # if user has left the forest
            break
        
        if explore: # if user wants to explore the forest
            break
    
    if left: # if they left, make sure to turn any negatives back to 0
        if coins < 0:
            coins = 0
        
        if hearts < 0:
            hearts = 0
        
        break
    
    if randint(1, 15) == 1: # bear encounter
        print()
        print("You encountered a bear.")
        dangers_encountered += 1
        dangerous = (randint(1, 5) < 3)
        
        while True:
            go_see = options(fight_bear=True, dangerous=dangerous) # prompt options
            
            if left: # if user has left the forest
                break
            
            if go_see: # if user wants to go see the bear
                break
            
            if go_see == False: # if user has used their sword or consumed golden apple
                break
        
        if left: # if they left, make sure to turn any negatives back to 0
            if coins < 0:
                coins = 0
            
            if hearts < 0:
                hearts = 0
            
            break
        
        if go_see: # if user wants to see the bear
            if not dangerous: # if the bear is not dangerous
                coins_gained = randint(1, 15)
                print("Aww! The bear just wants a hug! It gave you " + str(coins_gained) + " coins as a thank you gift.")
                coins += coins_gained
            
            else: # if the bear is dangerous
                print("The bear is angry and dealt 5 hearts of damage.")
                hearts -= 5
            
        if hearts < 0: # if hearts are in negative, fix it back to 0
            hearts = 0
        
        continue # skip everything and go do another loop of conditions of while loop meet
    
    if randint(1, 15) == 1: # wolf encounter
        print()
        print("You encountered some wolves.")
        dangers_encountered += 1
        dangerous = (randint(1, 3) < 3)
        
        while True:
            go_see = options(fight_wolves=True, dangerous=dangerous) # prompt options
            
            if left: # if user has left the forest
                break
            
            if go_see: # if user wants to go see the wolves
                break
            
            if go_see == False: # if user has used their sword or consumed golden apple
                break
        
        if left: # if they left, make sure to turn any negatives back to 0
            if coins < 0:
                coins = 0
            
            if hearts < 0:
                hearts = 0
            
            break
        
        if go_see: # if user wants to see the wolves
            if not dangerous: # if the wolves are not dangerous
                coins_gained = randint(1, 20)
                print("The wolves are so cute! They just wanted some company.")
                print(" Oh look they even got some coins to share! You got " + str(coins_gained) + " coins from the wolves.")
                coins += coins_gained
            
            else: # if the wolves are dangerous
                print("The wolves are angry and launch at you.")
                print("You got bit and lost 4 hearts.")
                hearts -= 4
            
        if hearts < 0: # if hearts are in negative, fix it back to 0
            hearts = 0
        
        continue
    
    if randint(1, 10) == 1: # treasure chest
        print()
        coins_gained = randint(5, 25)
        print("OMG! You found a treasure chest, and found " + str(coins_gained) + " coins there.")
        coins += coins_gained
        advance()
    
    if randint(1, 14) == 1: # monkey approach
        print()
        print("A monkey just approached you!")
        coins_stolen = randint(2, randint(25, 35))
        print("It stole " + str(coins_stolen) + " coins from your coin bag!")
        coins -= coins_stolen
        
        if coins < 0:
            coins = 0
        
        advance()
    
    event = randint(1, 5) # event
    
    if event == 1: # prick event
        print()
        print("You stepped on a prick! You lost 1 heart.")
        hearts -= 1
        advance()
    
    if event == 2: # mushroom event
        print()
        print("You found a Mushroom!")
        pick("Mushroom")
        advance()
    
    if event == 3: # coin event
        print()
        print("You found a coin on the ground.")
        coins += 1
        advance()
    
    if event == 4: # trip event
        print()
        print("Ow! You tripped and hurt yourself. You lost 1 heart.")
        hearts -= 1
        advance()
    
    if event == 5: # coins event
        print()
        coins_gained = randint(2, 8)
        print("You found " + str(coins_gained) + " coins on the ground.")
        coins += coins_gained
        advance()
    
    if randint(1, 15) == 1: # finding a sword
        print()
        print("You found a Sword on the ground!")
        swords_found += 1
        pick("Sword")
        advance()
    
    if randint(1, 16) == 1: # finding a golden apple
        print()
        print("You found a Golden Apple!")
        golden_apples_found += 1
        pick("Golden Apple")
        advance()
    
    # fixing negatives to 0
    if coins < 0:
        coins = 0
    
    if hearts < 0:
        hearts = 0
    
    # now loop again

# out of loop
print()

if coins >= win_amount: # if coins are greater or equal to the win amount
    # win
    print("You collected " + str(coins) + """ and found your way out of the forest, luckily surviving.
You won, GG bro""")
    
elif left: # if user left the forest
    # surrender
    print("You left the forest, escaping all dangers.")

else: # if they died
    # lose
    print("""You died.
Your body was later found by a passerby in the forest,