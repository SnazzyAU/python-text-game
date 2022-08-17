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
armyData = {'armySwordType': 'bronze sword', 'armyArmourType': 'bronze armour', 'totalArmyCount': 0}
armyTroops = {'infantry': 0, 'archer': 0, 'cavalry': 0, 'dragon': 0}
gameInventory = {'improved bronze sword': 1, 'gunpowder': 10, 'morris armour': 1}
settlementInventory = {}
passed = 0
completed = 0
debugSkipTutorial = True

## Maps
def NorthForest():
    gameData['lastLocation'] = 'North Forest'
    pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))

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
                    pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                    Village()
                
                elif mapChoice == "North Forest" or mapChoice == "north forest":
                    print("\033[1;31;1mYou are already in the Northern Forest!\033[0;37;0m")
                
                elif mapChoice == "Harbour" or mapChoice == "harbour":
                    dramaticPrint("You find your south bearing and begin your adventure towards the harbour!\n",0.07)
                    #harbour()
                
                elif mapChoice == "Exodus" or mapChoice == "exodus":
                    print("\033[1;31;1mYou cannot go there without a boat!\033[0;37;0m")
                    
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
                            print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                            time.sleep(3)
                    
                elif mapChoice == "Exit" or mapChoice == "exit":
                    clear()
                    break
                    
                else:
                    print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
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
                    print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")
            
                choice2 = input("\n\n[1] Continue Scavenging\n[2] Stop Scavenging \n\n")

                if choice == '2':
                    break
            
        elif choice == '3':
            Village()
            
        else:
            clear()
            print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")

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
                            print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                            time.sleep(3)
                
                elif mapChoice == "Exodus" or mapChoice == "exodus":
                    print("You cannot go there without a boat! Get to the harbour.")
                    time.sleep(3)
                    
                elif mapChoice == "Exit" or mapChoice == "exit":
                    clear()
                    break
                    
                else:
                    print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                    time.sleep(3)
                
            
        # Villagement Management System
        elif choice == "2":
            clear()
            
            while True:
                print("\n\033[1mYour Village Information\n\033[0m")
                print(settlementData)
                
                choice = input("\n[1] Upgrade Defenses\n[2] Army Management\n[3] Exit \n\n")
                
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
                            neededGold = 500
                            
                            while True:
                                print(f"\n\nYou need: {neededItems} and you need {neededGold} gold.")
                                print(f"Your Inventory: {gameInventory}")
                                
                                action = input("Would you like to proceed with the upgrades? \n\n[1] Yes\n[2] No\n\n")
                                
                                ## Yes
                                if action == "1":
                                    clear()
                                    
                                    if gameData['Gold'] >= neededGold:
                                        
                                        for item in neededItems:
                                            if neededItems.get(item) <= gameInventory.get(item):
                                                global passed
                                                
                                                passed = passed + 1

                                                if len(neededItems) == passed:
                                                    count = 0 
                                                    
                                                    for item in neededItems:
                                                        
                                                        count = count + 1
                                                                                                            
                                                        gameInventory[item] = gameInventory[item] - neededItems.get(item)
                                                            
                                                        if count == len(neededItems):
                                                            print(f"You have successfully upgraded your cannons to level {settlementData['cannonLevel'] + 1}!")
                                                            print(f'Updated Inventory: {gameInventory}')
                                                            print(f"Old Gold Balance: {gameData['Gold']}")
                                                            print(f"New Gold Balance: {gameData['Gold'] - neededGold}")
                                                            
                                                            settlementData['cannonLevel'] = settlementData['cannonLevel'] + 1
                                                            gameData['Gold'] = gameData['Gold'] - neededGold
                                                            
                                                            pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                            break
                                                        
                                            else:
                                                clear()
                                                print("\033[1;31;1mYou do not have the required resources to complete this upgrade!\033[0;37;0m")
                                                
                                                break
                            
                                        
                                    else:
                                        clear()
                                        print("\033[1;31;1mYou do not have enough gold!\033[0;37;0m")
                                                                                
                                ## No
                                elif action == "2":
                                    clear()
                                    break
                                    
                                else:
                                    clear()
                                    print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                                                   
                        ## Wall Upgrade
                        elif choice == 'wall' or choice == 'Wall' or choice == 'walls' or choice == 'Walls':
                            neededItems = {'enchanted wood': 2 * settlementData['wallLevel'], 'gunpowder': 3 * settlementData['wallLevel']}
                            neededGold = 0
                            
                            while True:
                                print(f"\n\nYou need: {neededItems} and you need {neededGold} gold.")
                                print(f"Your Inventory: {gameInventory}")
                                
                                action = input("Would you like to proceed with the upgrades? \n\n[1] Yes\n[2] No\n\n")
                                
                                ## Yes
                                if action == "1":
                                    clear()
                                    
                                    if gameData['Gold'] >= neededGold:
                                        
                                        for item in neededItems:
                                            if neededItems.get(item) <= gameInventory.get(item):
                                                
                                                passed = passed + 1

                                                if len(neededItems) == passed:
                                                    count = 0 
                                                    
                                                    for item in neededItems:
                                                        
                                                        count = count + 1
                                                                                                            
                                                        gameInventory[item] = gameInventory[item] - neededItems.get(item)
                                                            
                                                        if count == len(neededItems):
                                                            print(f"You have successfully upgraded your walls to level {settlementData['wallLevel'] + 1}!")
                                                            print(f'Updated Inventory: {gameInventory}')
                                                            print(f"Old Gold Balance: {gameData['Gold']}")
                                                            print(f"New Gold Balance: {gameData['Gold'] - neededGold}")
                                                            
                                                            settlementData['wallLevel'] = settlementData['wallLevel'] + 1
                                                            gameData['Gold'] = gameData['Gold'] - neededGold
                                                            
                                                            pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                            break
                                                        
                                            else:
                                                clear()
                                                print("\033[1;31;1mYou do not have the required resources to complete this upgrade!\033[0;37;0m")
                                                
                                                break
                            
                                        
                                    else:
                                        clear()
                                        print("\033[1;31;1mYou do not have enough gold!\033[0;37;0m")
                                                                            
                                        
                                ## No
                                elif action == "2":
                                    clear()
                                    break
                            
                        elif choice == 'exit' or choice == 'Exit':
                            clear()
                            break
                            
                        else:
                            clear()
                            print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                
                ## Army Management
                elif choice == "2":
                    clear()
                    
                    while True:
                        
                        print(f"Your Army: {armyTroops}")
                        print(f'Army Sword Type: {armyData["armySwordType"]}')
                        print(f'Army Armour Type: {armyData["armyArmourType"]}')
                        print(f'Total Army Count: {armyData["totalArmyCount"]}')
                        
                        choice = input("\n\n[1] Upgrade Army Equipment\n[2] Recruit Troops\n[3] Exit \n\n")
                        
                        ## Upgrade Army Equipment
                        if choice == "1":
                            clear()
                            
                            while True:
                                print(f"Your Inventory: {gameInventory}")
                                print(f'Army Sword Type: {armyData["armySwordType"]}')
                                print(f'Army Armour Type: {armyData["armyArmourType"]}')
                                
                                choice = input("What would you like to upgrade? (or type 'exit' to exit) ")
                                
                                ## Upgrade Sword
                                if choice == "sword" or choice == "Sword":
                                    clear()
                                    
                                    acceptableSwords = ['bronze sword', 'improved bronze sword', 'gold sword', 'exotic sword', 'morris sword']
                                    swordsHave = []
                                    
                                    for sword in acceptableSwords:
                                        if sword in gameInventory:
                                            swordsHave.append(sword)
                                    
                                    if swordsHave == []:
                                        clear()
                                        
                                        print("\033[1;31;1mYou do not have any available swords to give to your army!\n\n\033[0;37;0m")
                                    
                                    else:
                                        clear()
                                        
                                        while True:
                                            print(f"Available Swords: {swordsHave}")
                                            
                                            choice = input("Which sword would you like your army to use? (or type 'exit' to exit ")
                                            
                                            if choice in swordsHave:
                                                clear()
                                                                  
                                                # Add old sword back to inventory
                                                oldSword = armyData['armySwordType']
                                                gameInventory[oldSword] = 1
                                                
                                                # Remove new sword from inventory
                                                gameInventory.pop(choice)
                                                
                                                # Set new sword to army
                                                armyData['armySwordType'] = choice
                                                
                                                # Save all data
                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                
                                                print(f"You have successfully equipped your army with: {choice}\n\n")
                                                
                                                break
                                                
                                            elif choice == "exit":
                                                clear()
                                                print("\nVery well.")
                                                
                                                break
                                                
                                            else:
                                                print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                                    
                                ## Upgrade Armour
                                elif choice == "armour" or choice == "armor" or choice == "Armour" or choice == "Armor":
                                    clear()
                                    
                                    acceptableArmour = ['bronze armour', 'improved bronze armour', 'gold armour', 'exotic armour', 'morris armour']
                                    armourHave = []
                                    
                                    for armour in acceptableArmour:
                                        if armour in gameInventory:
                                            armourHave.append(armour)
                                    
                                    if armourHave == []:
                                        clear()
                                        print("\033[1;31;1mYou do not have any suitable armour to give to your army!\n\n\033[0;37;0m")
                                    
                                    else:
                                        clear()
                                        
                                        while True:
                                            print(f"Available Armour: {armourHave}")
                                            
                                            choice = input("Which armour would you like your army to use? (or type 'exit' to exit ")
                                            
                                            if choice in armourHave:
                                                clear()
                                                                  
                                                # Add old armour back to inventory
                                                oldArmour = armyData['armyArmourType']
                                                gameInventory[oldArmour] = 1
                                                
                                                # Remove new armour from inventory
                                                gameInventory.pop(choice)
                                                
                                                # Set new armour to army
                                                armyData['armyArmourType'] = choice
                                                
                                                # Save all data
                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                
                                                print(f"You have successfully equipped your army with: {choice} \n\n")
                                                
                                                break
                                                
                                            elif choice == "exit":
                                                clear()
                                                print("\nVery well.")
                                                
                                                break
                                                
                                            else:
                                                print(f'choice: {choice}')
                                                print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                                    
                                elif choice == 'exit' or choice == 'Exit':
                                    clear()
                                    
                                    print("Very well.")
                                    break
                                    
                                else:
                                    clear()
                                    print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                            
                        ## Recruit Troops
                        elif choice == "2":
                            global completed
                            
                            clear()
                            
                            while True:
                                
                                print(f'Your current army: {armyTroops}\n\n')
                                print(f'Your Gold: {gameData["Gold"]}')
                            
                                infantryCost = 0
                                archerCost = 0
                                cavalryCost = 80
                                dragonCost = 100
                                
                                choice = input("What troop would you like to train? (Or type 'exit' to leave)\n\n[1] Infantry\n[2] Archer\n[3] Cavalry\n[4] Dragon \n\n")
                                
                                # Infantry
                                if choice == '1':
                                    clear()
                                    
                                    while True:
                                        amount = int(input(f"How many troops would you like to train? (or type '0' to leave) \n1x Infantry: {infantryCost} gold\n\n"))
                                        
                                        # Check if amount is greater than 0; impossible to train 0 or less troops
                                        if amount > 0:
                                            clear()
                                            
                                            while True:
                                                # Ask for confirmation
                                                confirmation = input(f"Are you sure you want to train, {amount} amount of Infantry units? It will cost you {infantryCost * amount} gold.\n\n[1] Yes\n[2] No \n\n")
                                                
                                                # Yes
                                                if confirmation == '1':
                                                    # Check if player has enough gold for the transaction
                                                    if gameData['Gold'] >= infantryCost * amount:
                                                        gameData['Gold'] = gameData['Gold'] - infantryCost * amount
                                                        
                                                        # Wait 1 second for each troop that is being trained
                                                        for i in range(1,amount+1):
                                                            clear()
                                                            
                                                            # Assign new value
                                                            armyTroops['infantry'] = armyTroops['infantry'] + 1
                                                            
                                                            completed = completed + 1
                                                            
                                                            # Save all data
                                                            if completed == amount:
                                                                armyData["totalArmyCount"] = armyData["totalArmyCount"] + amount
                                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                                
                                                            print(f"{0+i}x Infantry Units Trained")
                                                            
                                                            time.sleep(1)
                                                                                                                
                                                    else:
                                                        clear()                                                        
                                                        print("\033[1;31;1mNot enough gold!\n\033[0;37;0m")
                                                
                                                # No
                                                elif confirmation == '2':
                                                    clear()
                                                    
                                                    break
                                                
                                                else:
                                                    clear()
                                                    
                                                    print("\033[1;31;1mInvalid choice!\n\033[0;37;0m")
                                        
                                        elif amount == 0:
                                            clear()
                                            
                                            break
                                            
                                        else:
                                            clear()
                                            
                                            print("\033[1;31;1mInvalid amount!\n\033[0;37;0m")
                                            
                                # Archer
                                elif choice == '2':
                                    clear()
                                    
                                    while True:
                                        amount = int(input(f"How many troops would you like to train? (or type '0' to leave) \n1x Archer: {archerCost} gold\n\n"))
                                        
                                        # Check if amount is greater than 0; impossible to train 0 or less troops
                                        if amount > 0:
                                            clear()
                                            
                                            while True:
                                                # Ask for confirmation
                                                confirmation = input(f"Are you sure you want to train, {amount} amount of Archer units? It will cost you {archerCost * amount} gold.\n\n[1] Yes\n[2] No \n\n")
                                                
                                                # Yes
                                                if confirmation == '1':
                                                    # Check if player has enough gold for the transaction
                                                    if gameData['Gold'] >= archerCost * amount:
                                                        gameData['Gold'] = gameData['Gold'] - archerCost * amount
                                                        
                                                        # Wait 1 second for each troop that is being trained
                                                        for i in range(1,amount+1):
                                                            clear()
                                                            
                                                            # Assign new value
                                                            armyTroops['archer'] = armyTroops['archer'] + 1
                                                            
                                                            completed = completed + 1
                                                            
                                                            # Save all data
                                                            if completed == amount:
                                                                armyData["totalArmyCount"] = armyData["totalArmyCount"] + amount
                                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                                
                                                            print(f"{0+i}x Archer Units Trained")
                                                            
                                                            time.sleep(1)
                                                                                                                
                                                    else:
                                                        clear()
                                                        print("\033[1;31;1mNot enough gold!\n\033[0;37;0m")
                                                
                                                # No
                                                elif confirmation == '2':
                                                    clear()
                                                    
                                                    break
                                                
                                                else:
                                                    clear()
                                                    
                                                    print("\033[1;31;1mInvalid choice!\n\033[0;37;0m")
                                        
                                        elif amount == 0:
                                            clear()
                                            
                                            break
                                            
                                        else:
                                            clear()
                                            
                                            print("\033[1;31;1mInvalid amount!\n\033[0;37;0m")
                                
                                # Cavalry
                                elif choice == '3':
                                    clear()
                                    
                                    while True:
                                        amount = int(input(f"How many troops would you like to train? (or type '0' to leave) \n1x Cavalry: {cavalryCost} gold\n\n"))
                                        
                                        # Check if amount is greater than 0; impossible to train 0 or less troops
                                        if amount > 0:
                                            clear()
                                            
                                            while True:
                                                # Ask for confirmation
                                                confirmation = input(f"Are you sure you want to train, {amount} amount of Cavalry units? It will cost you {cavalryCost * amount} gold.\n\n[1] Yes\n[2] No \n\n")
                                                
                                                # Yes
                                                if confirmation == '1':
                                                    # Check if player has enough gold for the transaction
                                                    if gameData['Gold'] >= cavalryCost * amount:
                                                        gameData['Gold'] = gameData['Gold'] - cavalryCost * amount
                                                        
                                                        # Wait 1 second for each troop that is being trained
                                                        for i in range(1,amount+1):
                                                            clear()
                                                            
                                                            # Assign new value
                                                            armyTroops['cavalry'] = armyTroops['cavalry'] + 1
                                                            
                                                            completed = completed + 1
                                                            
                                                            # Save all data
                                                            if completed == amount:
                                                                armyData["totalArmyCount"] = armyData["totalArmyCount"] + amount
                                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                                
                                                            print(f"{0+i}x Cavalry Units Trained")
                                                            
                                                            time.sleep(1)
                                                                                                                
                                                    else:
                                                        clear()
                                                        print("\033[1;31;1mNot enough gold!\n\033[0;37;0m")
                                                
                                                # No
                                                elif confirmation == '2':
                                                    clear()
                                                    
                                                    break
                                                
                                                else:
                                                    clear()
                                                    
                                                    print("\033[1;31;1mInvalid choice!\n\033[0;37;0m")
                                        
                                        elif amount == 0:
                                            clear()
                                            
                                            break
                                            
                                        else:
                                            clear()
                                            
                                            print("\033[1;31;1mInvalid amount!\n\033[0;37;0m")
                                
                                # Dragon
                                elif choice == '4':
                                    clear()
                                    
                                    while True:
                                        amount = int(input(f"How many troops would you like to train? (or type '0' to leave) \n1x Dragon: {dragonCost} gold\n\n"))
                                        
                                        # Check if amount is greater than 0; impossible to train 0 or less troops
                                        if amount > 0:
                                            clear()
                                            
                                            while True:
                                                # Ask for confirmation
                                                confirmation = input(f"Are you sure you want to train, {amount} amount of Dragon units? It will cost you {dragonCost * amount} gold.\n\n[1] Yes\n[2] No \n\n")
                                                
                                                # Yes
                                                if confirmation == '1':
                                                    # Check if player has enough gold for the transaction
                                                    if gameData['Gold'] >= dragonCost * amount:
                                                        gameData['Gold'] = gameData['Gold'] - dragonCost * amount
                                                        
                                                        # Wait 1 second for each troop that is being trained
                                                        for i in range(1,amount+1):
                                                            clear()
                                                            
                                                            # Assign new value
                                                            armyTroops['dragon'] = armyTroops['dragon'] + 1
                                                            
                                                            completed = completed + 1
                                                            
                                                            # Save all data
                                                            if completed == amount:
                                                                armyData["totalArmyCount"] = armyData["totalArmyCount"] + amount
                                                                pickle.dump([gameData, gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
                                                                
                                                            print(f"{0+i}x Dragon Units Trained")
                                                            
                                                            time.sleep(1)
                                                                                                                
                                                    else:
                                                        clear()
                                                        print("\033[1;31;1mNot enough gold!\n\033[0;37;0m")
                                                
                                                # No
                                                elif confirmation == '2':
                                                    clear()
                                                    
                                                    break
                                                
                                                else:
                                                    clear()
                                                    
                                                    print("\033[1;31;1mInvalid choice!\n\033[0;37;0m")
                                        
                                        elif amount == 0:
                                            clear()
                                            
                                            break
                                            
                                        else:
                                            clear()
                                            
                                            print("\033[1;31;1mInvalid amount!\n\033[0;37;0m")
                                
                                # Exit
                                elif choice == 'exit' or choice == 'Exit':
                                    clear()
                                    
                                    break
                                
                                else:
                                    print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")
                                                                
                        elif choice == "3":
                            clear()
                            print("Very well.")
                            
                            break
                        
                        else:
                            clear()
                            
                            print("\033[1;31;1mNot a valid option!\n\033[0;37;0m")
                    
                ## Return (Exit)
                elif choice == "3":
                    clear()
                    break
                    
                else:
                    clear()
                    print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
        
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
                                    print("\033[1;31;1mInvalid amount, try again\033[0;37;0m")
                                
                                else:
                                
                                    if gameInventory.get(choice) - amount < 0:
                                        print("\033[1;31;1mYou don't have that much!\033[0;37;0m")
                                    
                                    else:
                                        gameInventory[choice] = gameInventory.get(choice) - amount
                                        settlementInventory[choice] = settlementInventory.get(choice, 0) + amount
                                        
                                        if gameInventory[choice] == 0:
                                            gameInventory.pop(choice)
                                            
                                        pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))

                                        clear()
                                        print(f"Sucessfully deposted x{amount} {choice} into the village's inventory!")
                                        break
                            
                        elif choice == "exit":
                            clear()
                            break
                        
                        else:
                            clear()
                            print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                
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
                                    print("\033[1;31;1mInvalid amount, try again.\033[0;37;0m")
                                
                                else:
                                
                                    if settlementInventory.get(choice) - amount < 0:
                                        print("\033[1;31;1mYou don't have that much in your village's stash!\033[0;37;0m")
                                    
                                    else:
                                        gameInventory[choice] = gameInventory.get(choice, 0) + amount
                                        settlementInventory[choice] = settlementInventory.get(choice) - amount
                                        
                                        if settlementInventory[choice] == 0:
                                            settlementInventory.pop(choice)
                                        
                                        pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))

                                        clear()
                                        print(f"Sucessfully withdrew x{amount} {choice} from the village's inventory!")
                                        break
                                
                        elif choice == "exit":
                            clear()
                            break
                        
                        else:
                            clear()
                            print("\033[1;31;1mInvalid choice, please try again.\n\033[0;37;0m")
                            
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
              
            dramaticPrint(f"Welcome Commander {gameData['playerUsername']} to the library! A place where you can learn all sorts of things.\n", delay)
            dramaticPrint(f"My name is Richard, the local librarian.\n\n",delay)
            
            while True:
                question = input("Choose a topic to learn: \n\n[1] About the game\n[2] Attacking and Defending\n[3] Exploring\n[4] Item Information\n[5] Troop Information \n\nOr type 'exit' to leave.\n\n").lower()
                
                # #About the game
                if question == '1':
                    clear()
                    dramaticPrint("This is a game all about surviving. You are the commander of Azgard, the local village, and it is your job to ensure the safety of all the villagers.\n", delay)
                    dramaticPrint("Every 5 days, your village will be subject to an attack from the barbarians!\n", delay)
                    dramaticPrint("You can check what day is by viewing the village calendar.\n", delay)
                    dramaticPrint("In order to improve your chances of survival, I recommend upgrading your villages defenses in the Village Management System.\n", delay)
                    dramaticPrint("Please be aware, some upgrades require some rare resources, which you can only acquire by exploring outside of the village walls.\n", delay)
                    dramaticPrint("The outside is a dangerous place, so make sure you are ready for a fight!\n", delay)
                    
                    input("\n\nWhen you are done reading, press [ENTER] ")
                    clear()
                    
                ## Attacking and Defending
                elif question == '2':
                    clear()
                    delay = 0.07
                    
                    print("\n\033[1mDefense\033[0m\n")
                    dramaticPrint("Every 10 minutes, a single day passes, and every 5 days, the barbarians attack our village.\n", delay)
                    dramaticPrint("You can check what day it is in the [Calendar].\n", delay)
                    dramaticPrint("Your total defense value is calculated by the amount of troops in your army, and what type they are.\n", delay)
                    dramaticPrint("Your defense structures also play a part in your total defense value. The higher level your canons and walls are, the better.\n", delay)
                    dramaticPrint("You can view the upgrades in the [Village Management] screen.\n\n", delay)

                    time.sleep(6)
                    clear()
                    
                    print("\n\033[1mAttack\033[0m\n")

                    input("\n\nWhen you are done reading, press [ENTER] ")
                    clear()
                    
                ## Exploring
                elif question == '3':
                    clear()
                    
                    dramaticPrint("Resources are scattered all accross the map, some being extremly common, and others being quite rare.\n", delay)
                    dramaticPrint("Certain items can only be found in certain areas. For example, [Enchanted Wood] can only be found in the [Northern Forest].\n", delay)
                    dramaticPrint("You can sell these items to the local tradesmen, [Edgar].", delay)

                    input("\n\nWhen you are done reading, press [ENTER] ")
                    clear()
                    
                ## Item Information
                elif question == '4':
                    clear()                    
                    delay = 0.07
                    
                    dramaticPrint("There are 5 different types of rarities.", delay)
                    dramaticPrint("\n\nBronze,\nImproved Bronze,\nGold,\nExotic and,\nMorris\n\n", delay)
                    dramaticPrint("The better the quality, the better the item is.\n\n", delay)
                    
                    time.sleep(3)
                    clear()
                    
                    print("\n\033[1mWeapons\033[0m\n")
                    dramaticPrint("Bronze Sword: 5 Damage\n", delay)
                    dramaticPrint("Improved Bronze Sword: 8 Damage\n", delay)
                    dramaticPrint("Gold Sword: 12 Damage\n", delay)
                    dramaticPrint("Exotic Sword: 14 Damage\n", delay)
                    dramaticPrint("Morris Sword: 16 Damage\n\n", delay)
                    
                    time.sleep(6)
                    clear()

                    print("\n\033[1mArmour\033[0m\n")
                    dramaticPrint("Bronze Armour: 5 Shield\n", delay)
                    dramaticPrint("Improved Bronze Armour: 25 Shield\n", delay)
                    dramaticPrint("Gold Armour: 50 Shield\n", delay)
                    dramaticPrint("Exotic Armour: 75 Shield\n", delay)
                    dramaticPrint("Morris Armour: 100 Shield\n", delay)
                    
                    input("\n\nWhen you are done reading, press [ENTER] ")
                    clear()
                    
                ## Troop Information
                elif question == '5':
                    
                    input("\n\nWhen you are done reading, press [ENTER] ")
                    clear()                    
                    
                ## Leave
                elif question == 'exit':
                    clear()
                    break
                    
                ## Else
                else:
                    print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")

        
        elif choice == "5":
            clear()
            print(f"\n\nIt is currently day {gameData['Day']}\n\n")
            
        else:
            clear()
            print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")
    
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
    pickle.dump([gameData,gameInventory, settlementData, settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
    
    ## Introduction Text / Skip if debugSkipTutorial Enabled
    clear()
    if not debugSkipTutorial:
        print("\n\nWelcome to VillageLife, good luck!\n\n")
        dramaticPrint(f"Commander {gameData['playerUsername']}, you made it!\n\n",0.07)
        time.sleep(2)
        dramaticPrint("I'm sorry about your fathers death, but now is not the time to grieve!\n\n",0.07)
        time.sleep(2)
        dramaticPrint(f"We need you, {gameData['playerUsername']}, to help make this village thrive! Remember, any good commander needs a little help here and there. Visit the library if you need help.\n\n",0.07)
        time.sleep(2)
        dramaticPrint("It's time, good luck!", 0.07)
        time.sleep(2)
        clear()
    
    else:
        pass
    
    ## First Game Initialization
    setLevel()
    
# Create a new game
def loadGame():
    clear()
        
    global gameData
    global gameInventory
    global settlementData
    global settlementInventory
    global armyData
    global armyTroops
    
    gameData,gameInventory,settlementData,settlementInventory,armyData,armyTroops = pickle.load(open("data/savefile", "rb"))
    
    print(armyData)
        
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
        pickle.dump([gameData,gameInventory,settlementData,settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
        print(f'You collected x1 {item}!')  
    else:
        if len(gameInventory) < 1:
            gameInventory[itemToSpawn] = gameInventory.get(itemToSpawn, 0) + 1
            pickle.dump([gameData,gameInventory,settlementData,settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
            print(f'You collected x1 {item}!')  
        else:
            print("\033[1;31;1mYou can only hold one item without a bag!\033[0;37;0m")
     
def addBag():
    gameData['HasBag'] = True
    pickle.dump([gameData,gameInventory,settlementData,settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))

def dramaticPrint(text,delay):
    for char in text:
        print(char, end = '', flush=True)
        time.sleep(delay)
    
def dayCounter():
    while True:
        time.sleep(600)
        gameData['Day'] = gameData['Day'] + 1
        pickle.dump([gameData,gameInventory,settlementData,settlementInventory, armyData, armyTroops], open('data/savefile', 'wb'))
        
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

def shop():
    clear()
    
    shopItems = {"bag": 40, "gold sword": 20}
    stock = {"bag": 1, "gold sword": 1}
    
    while True:
        choice = input("[1] Buy Items\n[2] Sell Items\n[3] Exit")
        
        ## Buy Items
        if choice == '1':
            clear()
            
            while True:
                choice = input("What would you like to buy? ")
                
                if choice in shopItems:
                    stockAmount = stock.get(choice)
                    
                    if stockAmount == 1:
                        shopItems.pop(choice)
                    else:
                        stock[choice] = stock[choice] - 1
                        
                    print('DEBUG ' + stock)
                    print('DEBUG ' + shopItems)
                    
                else:
                    clear()
                    
                    print("Invalid choice, please only choose the presented options.\n")
        
        ## Sell Items
        elif choice == '2':
            pass
            
        ## Exit
        elif choice == '3':
            break
        
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
                clear()
                
                print("\033[1;31;1mCancelled!\n\033[0;37;0m")
            
        else:
            clear()
            print("\033[1;31;1mInvalid choice, please only choose the presented options.\n\033[0;37;0m")
            
else:
    newGame()

