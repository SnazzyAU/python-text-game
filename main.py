############################################################################################################
##                                                                                                        ##
##   ███╗   ███╗ █████╗ ██████╗ ███████╗  ██████╗ ██╗   ██╗       ██╗███████╗████████╗ █████╗ ███╗  ██╗   ##
##   ████╗ ████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗ ██╔╝       ██║██╔════╝╚══██╔══╝██╔══██╗████╗ ██║   ##
##   ██╔████╔██║███████║██║  ██║█████╗    ██████╦╝ ╚████╔╝        ██║█████╗     ██║   ██║  ██║██╔██╗██║   ##
##   ██║╚██╔╝██║██╔══██║██║  ██║██╔══╝    ██╔══██╗  ╚██╔╝    ██╗  ██║██╔══╝     ██║   ██║  ██║██║╚████║   ##
##   ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗  ██████╦╝   ██║     ╚█████╔╝███████╗   ██║   ╚█████╔╝██║ ╚███║   ##
##   ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝  ╚═════╝    ╚═╝      ╚════╝ ╚══════╝   ╚═╝    ╚════╝ ╚═╝  ╚══╝   ##
##                                                                                                        ##
##                                                  ########################################################
##   ██╗  ██╗ █████╗  ██████╗ █████╗ ███╗  ██╗██╗   ## 
##   ██║  ██║██╔══██╗██╔════╝██╔══██╗████╗ ██║██║   ##
##   ███████║███████║╚█████╗ ███████║██╔██╗██║██║   ##
##   ██╔══██║██╔══██║ ╚═══██╗██╔══██║██║╚████║██║   ##
##   ██║  ██║██║  ██║██████╔╝██║  ██║██║ ╚███║██║   ##
##   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝   ##
##                                                  ##
######################################################

## Imports
import pickle
import time
import random
import os
from threading import Thread

## Initialized Variables
gameData = {'playerUsername': "", 'health': 100, 'lastLocation': '', 'Gold': 0, 'HasBag': True, 'Day': 0, 'attackCount': 0}
settlementData = {'villageHealth': 100, 'wallLevel': 1, 'cannonLevel': 1}
gameInventory = {'enchanted wood': 4, 'gunpowder': 6}
settlementInventory = {}

## Maps
def NorthForest():
    gameData['lastLocation'] = 'North Forest'
    pickle.dump([gameData,gameInventory, settlementData, settlementInventory], open('data/savefile', 'wb'))

    spawnItems()
    clear()
    while True:
        choice = input("You are in the northern forest. \n\n[1] Begin Travels\n[2] Gather Resources\n[3] Go Back To Village \n\n")
  
        # Explore
        if choice == "1":
            while True:
                print('''
                                    /‾\         /‾‾\     
                                /‾‾‾  | /‾‾‾‾‾‾‾    ‾\  
                                |      ‾             |  
                                |    North           |   
                               /    Forest           |   
                             /‾     (Here)           /   
                            |              ________/‾   
                            |        | Harbour  _/         
                     /‾‾‾‾‾‾‾   _____|_____/‾‾           
                    /          |                         
                    |          |                         
                 /‾‾  Village  |             /‾‾‾‾‾‾\    
                 |             |             |       ‾\  
                 \             |             | Exodus  |  
                  \____       _/             \______  /  
                       \     |                      \/   
                        \____/                           
                                                        
                ''')
                
                mapChoice = input("Where would you like to go? (or 'exit' to cancel) ")
                
                # Village
                if mapChoice == "village" or mapChoice == "Village":
                    dramaticPrint("You grip your sword and prepare for the journey back to the village!\n",0.07)
                    time.sleep(3)
                    gameData['lastLocation'] = 'Village'
                    pickle.dump([gameData,gameInventory, settlementData, settlementInventory], open('data/savefile', 'wb'))
                    Village()
                
                elif mapChoice == "North Forest" or mapChoice == "north forest":
                    print("You are already in the Northern Forest!")
                
                elif mapChoice == "Harbour" or mapChoice == "harbour":
                    dramaticPrint("You find your south bearing and begin your adventure towards the harbour!\n",0.07)
                    #harbour()
                
                elif mapChoice == "Exodus" or mapChoice == "exodus":
                    print("You cannot go there without a boat!")
                    
                    while True:
                        choice = input("Would you like to go to the harbour?\n\n[1] Yes\n[2] No \n\n")

                        if choice == "1":
                            dramaticPrint("You find your south bearing and begin your adventure towards the harbour!\n",0.07)
                            time.sleep(1)
                            #harbour()
                            
                        elif choice == "2":
                            print("Very well.")
                            time.sleep(1)
                            clear()
                            
                            break
                    
                        else:
                            print("Invalid choice, please try again.\n")
                            time.sleep(3)
                    
                elif mapChoice == "Exit" or mapChoice == "exit":
                    clear()
                    break
                    
                else:
                    print("Invalid choice, please try again.\n")
                    time.sleep(3)
        
        # Gather Resources
        elif choice == "2":
            while True:
                print("You begin scavenging for branches...")
                
                time.sleep(3)
                
                choice = input(f"You found: {itemToSpawn} \n\n[1] Collect\n[2] Ignore \n\n")
                
                if choice == '1':
                    addToInventory(itemToSpawn)
                    break
                
                elif choice == '2':
                    break
                
                else:
                    print("Invalid choice, please only choose the presented options.\n")
            
                choice2 = input("\n\n[1] Continue Scavenging\n[2] Stop Scavenging \n\n")

                if choice == '2':
                    break
            
        elif choice == '3':
            Village()
            
        else:
            clear()
            print("Invalid choice, please only choose the presented options.\n")

def Village():
    clear()
    gameData['lastLocation'] = 'Village'
    global gameInventory
    
    while True:
        choice = input("You are in Azgard, the local village. \n\n[1] Begin Travels\n[2] Village Management\n[3] Village Inventory\n[4] Library\n[5] Calendar\n\n")
  
        # Travels
        if choice == "1":
            clear()
            dramaticPrint("You walk to the village's front gate...\n", 0.07)
            
            while True:
                print('''
                                    /‾\         /‾‾\     
                                /‾‾‾  | /‾‾‾‾‾‾‾    ‾\  
                                |      ‾             |  
                                |    North           |   
                               /    Forest           |   
                             /‾                      /   
                            |              ________/‾   
                            |        | Harbour  _/         
                     /‾‾‾‾‾‾‾   _____|_____/‾‾           
                    /          |                         
                    |          |                         
                 /‾‾  Village  |             /‾‾‾‾‾‾\    
                 |    (Here)   |             |       ‾\  
                 \             |             | Exodus  |  
                  \____       _/             \______  /  
                       \     |                      \/   
                        \____/                           
                                                        
                ''')
                
                mapChoice = input("Where would you like to go? (or 'exit' to cancel) ")
                
                # Village
                if mapChoice == "village" or mapChoice == "Village":
                    print("You are already at the village!\n")
                    time.sleep(3)
                
                elif mapChoice == "North Forest" or mapChoice == "north forest":
                    dramaticPrint("You pack your bags and prepare for your trip to the Northern Forest...",0.07)
                    time.sleep(1)
                    NorthForest()
                
                elif mapChoice == "Harbour" or mapChoice == "harbour":
                    print("You can only enter the harbour from the Northern Forest.\n")
                                        
                    while True:
                        choice = input("Would you like to go to the Northern Forest?\n\n[1] Yes\n[2] No \n\n")

                        if choice == "1":
                            dramaticPrint("You pack your bags and prepare for your trip to the Northern Forest...",0.07)
                            time.sleep(1)
                            NorthForest()
                            
                        elif choice == "2":
                            print("Very well.")
                            time.sleep(1)
                            clear()
                            
                            break
                    
                        else:
                            print("Invalid choice, please try again.\n")
                            time.sleep(3)
                
                elif mapChoice == "Exodus" or mapChoice == "exodus":
                    print("You cannot go there without a boat! Get to the harbour.")
                    time.sleep(3)
                    
                elif mapChoice == "Exit" or mapChoice == "exit":
                    clear()
                    break
                    
                else:
                    print("Invalid choice, please try again.\n")
                    time.sleep(3)
                
            
        # Villagement Management System
        elif choice == "2":
            clear()
            
            while True:
                print("Your Village Information")
                print(settlementData)
                
                choice = input("\n[1] Upgrade Defenses\n[2] Repair Defenses\n[3] Exit \n\n")
                
                ## Upgrade Defenses
                if choice == "1":
                    clear()
                    
                    while True:
                        print(f"Cannon Level: {settlementData['cannonLevel']}")
                        print(f"Wall Level: {settlementData['wallLevel']}")
                    
                        choice = input("What would you like to upgrade? (or 'exit' to leave) ")
                        
                        ## Cannon Upgrade
                        if choice == 'cannon' or choice == 'Cannon' or choice == 'cannons' or choice == 'Cannons':
                            neededItems = {'enchanted wood': 2 * settlementData['cannonLevel'], 'gunpowder': 3 * settlementData['cannonLevel']}
                            neededGold = {'gold': 500}
                            
                            while True:
                                print(f"You need: {neededItems} and you need {neededGold} gold.")
                                print(f"Your Inventory: {gameInventory}")
                                
                                action = input("Would you like to proceed with the upgrades? \n\n[1] Yes\n[2] No\n\n")
                                
                                ## Yes
                                if action == "1":
                                    clear()
                                    
                                    # NOT WORK: if gameInventory has neededItems then do
                                    if gameInventory.items() <= neededItems.items():
                                        print("Has Items")
                                        all(map( gameInventory.pop, neededItems))
                                        ## remove neededItems from gameinventory
                                        
                                    else:
                                        clear()
                                        print("You do not have the required resources to complete this upgrade!")
                                        
                                        break
                                        
                                ## No
                                elif action == "2":
                                    clear()
                                    break
                                    
                                else:
                                    clear()
                                    print("Invalid choice, please try again.\n")
                                                   
                        ## Wall Upgrade
                        elif choice == 'wall' or choice == 'Wall' or choice == 'walls' or choice == 'Walls':
                            print("f")
                            break
                            
                        elif choice == 'exit' or choice == 'Exit':
                            clear()
                            break
                            
                        else:
                            clear()
                            print("Invalid choice, please try again.\n")
                
                ## Return (Exit)
                elif choice == "3":
                    clear()
                    break
                    
                else:
                    clear()
                    print("Invalid choice, please try again.\n")
        
        # Village Inventory System
        elif choice == "3":
            clear()
            print("You walk to the villages stash.")
            
            while True:
                choice = input("\n[1] Deposit Items\n[2] Withdraw Items\n[3] Leave \n\n")
                
                ## Deposit
                if choice == "1":
                    while True:
                        print(f"\nYour Inventory: {gameInventory}")
                        print(f"Village Inventory: {settlementInventory}\n")
                        
                        choice = input("Which item would you like to deposit? (type exit to leave) ")
                        
                        if choice in gameInventory:
                            print(f"\nYou chose {choice}, you currently have {gameInventory.get(choice)} of this item.\n")
                            
                            while True:
                                amount = int(input("How many of this item do you want to deposit? "))
                                
                                if amount <= 0:
                                    print("Invalid amount, try again")
                                
                                else:
                                
                                    if gameInventory.get(choice) - amount < 0:
                                        print("You don't have that much!")
                                    
                                    else:
                                        gameInventory[choice] = gameInventory.get(choice) - amount
                                        settlementInventory[choice] = settlementInventory.get(choice, 0) + amount
                                        
                                        pickle.dump([gameData,gameInventory, settlementData, settlementInventory], open('data/savefile', 'wb'))

                                        clear()
                                        print(f"Sucessfully deposted x{amount} {choice} into the village's inventory!")
                                        break
                            
                        elif choice == "exit":
                            clear()
                            break
                        
                        else:
                            clear()
                            print("Invalid choice, please try again.\n")
                
                ## Withdraw
                if choice == "2":
                    while True:
                        print(f"\nYour Inventory: {gameInventory}")
                        print(f"Village Inventory: {settlementInventory}\n")
                        
                        choice = input("Which item would you like to withdraw? (type exit to leave) ").lower()

                        if choice in settlementInventory:
                            clear()
                            print(f"\nYou chose {choice}, you currently have {settlementInventory.get(choice)} of this item in your village's stash.\n")
                            
                            while True:
                                amount = int(input("How many of this item do you want to withdraw? "))
                                
                                if amount <= 0:
                                    print("Invalid amount, try again.")
                                
                                else:
                                
                                    if settlementInventory.get(choice) - amount < 0:
                                        print("You don't have that much in your village's stash!")
                                    
                                    else:
                                        gameInventory[choice] = gameInventory.get(choice, 0) + amount
                                        settlementInventory[choice] = settlementInventory.get(choice) - amount
                                        
                                        pickle.dump([gameData,gameInventory, settlementData, settlementInventory], open('data/savefile', 'wb'))

                                        clear()
                                        print(f"Sucessfully withdrew x{amount} {choice} from the village's inventory!")
                                        break
                                
                        elif choice == "exit":
                            clear()
                            break
                        
                        else:
                            clear()
                            print("Invalid choice, please try again.\n")
                            
                ## Exit
                if choice == "3":
                    clear()
                    break
                
        elif choice == "4":
            time.sleep(1)
            dramaticPrint("\nYou enter the library...", 0.07)
            time.sleep(2)
            clear()
              
            delay = 0.045 
              
            print("-- Tutorial --")
            dramaticPrint(f"Welcome Commander {gameData['playerUsername']} to the library! A place where you can learn all sorts of things.\n", delay)
            dramaticPrint(f"My name is Richard, the local librarian.\n",delay)
            dramaticPrint("This is a game all about surviving. You are the commander of Azgard, the local village, and it is your job to ensure the safety of all the villagers.\n", delay)
            dramaticPrint("Every 5 days, your village will be subject to an attack from the barbarians!\n", delay)
            dramaticPrint("You can check what day is by viewing the village calendar.\n", delay)
            dramaticPrint("In order to improve your chances of survival, I recommend upgrading your villages defenses in the Village Management System.\n", delay)
            dramaticPrint("Please be aware, some upgrades require some rare resources, which you can only acquire by exploring outside of the village walls.\n", delay)
            dramaticPrint("The outside is a dangerous place, so make sure you are ready for a fight!\n", delay)
            dramaticPrint("That's all the help I can give you for now! Good luck on your journey.\n", delay)
            
            input("\n\nWhen you are done reading, press [ENTER] ")
            clear()
        
        elif choice == "5":
            clear()
            print(f"\n\nIt is currently day {gameData['Day']}\n\n")
            
        else:
            clear()
            print("Invalid choice, please only choose the presented options.\n")
    
## Functions
            
# Clear the screen
def clear():
    print('\n' * 100)
    time.sleep(1)

# Display the players last known information
def displayData():
    print("\n")
    print(f"You are currently in: {gameData['lastLocation']}")
    print(f"Your Inventory: {gameInventory}")
    print(f"Your health is currently on: {gameData['health']}")
    print(f"It is currently day {gameData['Day']}.")
    print(f"Gold: {gameData['Gold']}")
    print("\n")
    
def displayVillageData():
    print("\n")
    print("Your walls are currently level: {settlementData['wallLevel']}")
    print("Your cannons are currently level: {settlementData['cannonLevel']}")
    print("\n")
    
# Create a new savefile
def newGame():
    clear()
    
    ## Username Input + Saving of original game data
    playerName = input("What would you like your character to be named: ")
    gameData['playerUsername'] = playerName
    gameData['lastLocation'] = "Village"
    pickle.dump([gameData,gameInventory, settlementData, settlementInventory], open('data/savefile', 'wb'))
    
    ## Introduction Text
    clear()
    print("\n\nWelcome to {}, good luck!\n\n")
    dramaticPrint(f"Commander {gameData['playerUsername']}, you made it!\n\n",0.07)
    time.sleep(2)
    dramaticPrint("I'm sorry about your fathers death, but now is not the time to grieve!\n\n",0.07)
    time.sleep(2)
    dramaticPrint(f"We need you, {gameData['playerUsername']}, to help make this village thrive! Remember, any good commander needs a little help here and there. Visit the library if you need help.\n\n",0.07)
    time.sleep(2)
    dramaticPrint("It's time, good luck!", 0.07)
    time.sleep(2)
    clear()
    
    ## First Game Initialization
    setLevel()
    
# Create a new game
def loadGame():
    clear()
        
    global gameData
    global gameInventory
    global settlementData
    global settlementInventory
    
    gameData,gameInventory,settlementData,settlementInventory = pickle.load(open("data/savefile", "rb"))
        
    print(f'Welcome back, {gameData["playerUsername"]}.')
    
    displayData()
    setLevel()

# Set players level
def setLevel():
    t1 = Thread(target=dayCounter).start()
    
    if gameData['lastLocation'] == 'North Forest':
        NorthForest()
        
    if gameData['lastLocation'] == 'Village':
        Village()
        
def spawnItems():
    commonItems = ['leaf','paper']
    rareItems = ['enchanted wood']
    
    if random.randint(1,100) < 80:
        global itemToSpawn
        itemToSpawn = random.choice(commonItems)
    else:
        itemToSpawn = random.choice(rareItems)
                    
def addToInventory(item):
    clear()
    global gameInventory

    if gameData['HasBag']:
        gameInventory[itemToSpawn] = gameInventory.get(itemToSpawn, 0) + 1
        pickle.dump([gameData,gameInventory,settlementData,settlementInventory], open('data/savefile', 'wb'))
        print(f'You collected x1 {item}!')  
    else:
        if len(gameInventory) < 1:
            gameInventory[itemToSpawn] = gameInventory.get(itemToSpawn, 0) + 1
            pickle.dump([gameData,gameInventory,settlementData,settlementInventory], open('data/savefile', 'wb'))
            print(f'You collected x1 {item}!')  
        else:
            print("You can only hold one item without a bag!")
    

def addBag():
    gameData['HasBag'] = True
    pickle.dump([gameData,gameInventory,settlementData,settlementInventory], open('data/savefile', 'wb'))

def dramaticPrint(text,delay):
    for char in text:
        print(char, end = '', flush=True)
        time.sleep(delay)
    
def dayCounter():
    while True:
        time.sleep(100000)
        gameData['Day'] = gameData['Day'] + 1
        pickle.dump([gameData,gameInventory,settlementData,settlementInventory], open('data/savefile', 'wb'))
        
        # If Day is divisible by 5, war begins
        if gameData['Day'] % 5 == 0:
            attackDay()

def attackDay():
    
    attackCount = gameData['attackCount']
    attackDamage = 10 + attackCount
    
    playerHealth = gameData['health']
    villageHealth = settlementData['villageHealth']
    
    barbarianHealth = random.randint(100,120) + attackCount
    
    gameData['lastLocation'] = 'Village'
    
    clear()
    dramaticPrint(f"Commander {gameData['playerUsername']}, we are being attacked!\n", 0.07)
    dramaticPrint("Prepare the defenses!\n\n", 0.07)
    
    while True:
        print(f"Your Health: {playerHealth}")
        print(f"Village Health: {villageHealth}")
        print("---------------------------------")
        print(f"Barbarian Health: {barbarianHealth}\n\n")
        
        choice4 = input("[1] Attack\n[2] Defend\n\n")
        
        # Attack
        if choice4 == '1':
            
            messages = [
                'You slam your sword onto the never-ending swarm of barbarians!',
                'You throw a huge rock towards the enemy!'
            ]
            
            print(random.choice(messages))
            
            barbarianHealth = random.randint(1,10)
            playerHealth = playerHealth - attackDamage

        elif choice4 == '2':
            print('2')
            
        else:
            print("Invalid choice, please only choose the presented options.\n")

# New/Load Game
if os.path.exists('data/savefile'):
    while True:
        choice1 = input("A savefile has been detected, what would you like to do? \n\n[1] Resume Game\n[2] New Game\n\n")
                
        if choice1 == '1':
             loadGame()
             break
        
        if choice1 == '2':
            choice2 = input("\nAre you sure you want to delete your previous save? \n\n[1] Yes\n[2] No\n\n")
            
            if choice2 == "1":
                newGame()
                break
            
            if choice2 == "2":
                print("Cancelled")
            
        else:
            clear()
            print("Invalid choice, please only choose the presented options.\n")
            
else:
    newGame()
