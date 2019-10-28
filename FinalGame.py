#import
import random
import time
flag = False
import sys

#Defining Introduction for the Game
def Introduction():
    global flag
    x = input('What is your Name? ')
    print ("Welcome!!!...."+ x.title())
    time.sleep(2)
    print ("This Game is all about Survival Techniques")
    time.sleep(2)
    scene = RandomSceneCreation()
    print ("You are trapped in a "+scene[0][1])
    time.sleep(2)
    print ("The distance to nearest civilisation is "+str(scene[0][0])+" km")
    time.sleep(2)
    print ("Your Aim is to help your character to Survive in this Brutal WildLife")
    time.sleep(2)
    print ("Game Begins:---")
    time.sleep(2)
    DisplayInventory(scene[1])
    return scene

#Defining Menu Bar
def Menu(hydration,bodytemp,hour,watersource,timer,distance,hunger):
    if hour > 12:
        hour = hour - 12
        if timer == 0:
            timer = 1
        elif timer == 1:
            timer = 0
    if timer == 1:
        print("There are " + str(12-hour) + "hours of night time left")
    else:
        print ("There are " + str(12-hour) + " hours of day time left")
    print ("1. Walk")
    print ("2. Rest")
    print ("3. Hunt")
    print ("4. Search")
    print ("5. Eat")
    print ("6. Drink Water")
    print ("7. Inventory")
    print ("8. Use Items")
    print ("9. Build Shelter")
    print ("10.Quit game")
    print ("Hydration: "+str(hydration))
    print ("Body Temp: "+str(bodytemp))
    print ("Hunger: "+str(hunger))
    print ("Distance between Civilisation: "+str(distance)+ " km")
    print
    return [input('Action >>> '),hour,timer]

#Defining Random Scene Generation
def RandomSceneCreation():
    scenes = ['RIVERSIDE','MIDDLE OF FOREST']
    water = [True,False]
    startitems = ['full bottle of Water','full bottle of Water','full bottle of Water', 'energy bar','energy bar',
                  'energy bar', 'energy bar', 'walking stick','tea leaves','tea leaves', 'tea leaves']
    randomstart1 = ['warming pack', 'sleeping bag','hygiene kit', 'energy bar', 'torch','tea leaves']
    randomstart2 = ['warming pack', 'full bottle of Water', 'camp set','energy bar', 'tea leaves']
    sceneforplayer = random.choice(scenes)
    if sceneforplayer == 'RIVERSIDE':
        water = True
    else:
        water = random.choice(water)
    startitems.append(random.choice(randomstart1))
    startitems.append(random.choice(randomstart2))
    return [[random.randint(40,60),sceneforplayer,water],startitems]

#Defining useable items with respect to scenes
def CreateRandomSearch(scene):
    itemscanbeobtained = ['tea leaves', 'deer flesh', 'cow flesh', 'bones']
    retlist = []
    if scene == 'RIVERSIDE':
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist
    else:
        itemscanbeobtained.append('Bait')
        itemscanbeobtained.append('Bird Nest')
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist

#Defining Hunting process
def Hunting(location,inventory,water):
    hygiene = SearchItem('hygiene kit', inventory)
    prey = ['bear', 'lion', 'cheetah', 'deer','cow','pig','fox','wolf','rabbit','toad','','','']
    if hygiene != 0:
        for i in range(2):
            prey.append('deer')
            prey.append('cow')
            prey.append('pig')
            prey.append('fox')
            prey.append('wolf')
            prey.append('rabbit')
            prey.append('toad')
    appear = random.choice(prey)
    if appear in ['bear','lion','cheetah']:
        success = random.choice(['True','False','False','False','False','False','False','False','False','False'])
        if success == 'False':
            injury = random.choice(['leg','arm','chest','broken ribs'])
            return [appear, injury]
        else:
            return [appear, success]
    else:
        return [appear, 'True']

#Defining Walk with respective parameters
def Walk(distance,hydration,bodytemp,inventory,timer):
    if 'walking stick' in inventory:
        maxwalking = 8
    else:
        maxwalking = 5
    if timer == 1 and ("torch" not in inventory):
        maxwalking = 2

    walked = random.randint(1,maxwalking)
    distance -= walked
    hydration -= 10
    bodytemp += 10
    return [walked,hydration,bodytemp]

#Definng Items Inventory
def DisplayInventory(inventory):
    amtcount = []
    amtcountunique = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i],1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1]+=1
    print ("You have: ")
    for i in amtcount:
        print (str(i[1])+" x "+str(i[0]))

#Defining Water Drinking
def DrinkWater(inventory):
    amtcount = []
    amtcountunique = []
    water = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] in ["full bottle of Water","full bottle of Water"]:
            water.append(i)
    print ("You have: ")
    if len(water) != 0:
        for i in range(len(water)):
            print (str(i+1)+". " + str(water[i][1])+" x "+str(water[i][0]))
        print ("Would you want to drink? If yes press 1 ")
        waters = input(">>> ")
        if waters == '1':
            if water[0][1] - 1 >= 0:
                inventory.remove('full bottle of Water')
                inventory.append('Empty Bottle')
                return [50, inventory]
        else:
            print ("Invalid Choice, No Such Choice Exists")
    else:
        print ("You have no water supplies")

#Defining Searching of items in Inventory
def SearchItem(item,inventory):
    amtcount = []
    amtcountunique = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] == item:
            amount = i[1]
    try:
        return amount
    except:
        return 0

#Defining Hydration with respect to Body
def CheckValidBody(hydration):
    if hydration > 100:
        hydration = 100
        return hydration
    else:
        return hydration

#Defining Hydration with respect to Hunger
def CheckValidHunger(hydration):
    if hydration < 0:
        hydration = 0
        return hydration
    else:
        return hydration

#Defining Food Search
def SearchFood(inventory):
    food = ['pig flesh', 'rabbit flesh','toad flesh','wolf flesh','fox flesh','bear flesh', 'deer flesh','cow flesh',
            'fish', 'cheetah flesh','lion flesh']
    energy = [50,25,20,60,50,70,50,60,50,70,70]
    ownedfood = []
    for i in inventory:
        if i in food:
            ownedfood.append(i)
    if len(ownedfood) == 0:
        print ("You do not have any food")
    else:
        DisplayInventory(ownedfood)
        print ("What do you want to eat?")
        consume = input(">>> ").lower()
        for i in ownedfood:
            if consume == i:
                owned = True
                print("Hunger Subsides for a while")
            else:
                owned = False
        if not owned:
            print ("You do not have this food")
        else:
            inventory.remove(consume)
            if consume == 'rabbit flesh':
                inventory.append('rabbit skin')
            for i in range(len(food)):
                if food[i] == consume:
                    energy = energy[i]
            return [inventory,energy]

#Defining To Use Items
def UsableItemsOutput(inventory):
    usableitems = ['tea leaves','warming pack','energy bar']
    usableowned = []
    for i in inventory:
        if i in usableitems:
            usableowned.append(i)
    if len(usableowned) != 0:
        print ("You own these usable items:")
        DisplayInventory(usableowned)
        print (">>> Which one do you want to use? <<<")
        use = input("Please type in the full item name >>> ").lower()
        for i in usableowned:
            if use == i.lower():
                inventory.remove(i)
                return [inventory,i]
                break
    else:
        print ("You do not own any usable items")


def UsedItem(hydration,bodytemp,hunger,useitem):
    import time
    usableitems = ['tea leaves', 'warming pack', 'energy bar']
    if useitem not in usableitems:
        print ("Item to use is not in the Usable Items List!")
    else:
        if useitem == usableitems[0]:
            hydration = 100
            print ("Hydration Restored to 100")
        elif useitem == usableitems[1]:
            bodytemp = 100
            print ("bodytemp Restored to 100")
        elif useitem == usableitems[2]:
            hunger -= 30
            print ("Hunger - 30")
        return [hydration,bodytemp,hunger]


#Variables
inform = Introduction()
distance = inform[0][0]
scene = inform[0][1]
watersource = inform[0][2]
startingitems = inform[1]
hour = 0
timer = 0
hydration = 100
bodytemp = 100
hunger = 0
shelter = False
clothing = True

#Game Code
while distance > 0:
    if hydration > 0 and bodytemp > 0 and hunger < 100:
        if not clothing:
            bodytemp -= 5
        else:
            bodytemp += 0
        action = Menu(hydration,bodytemp,hour,watersource,timer,distance,hunger)
        hour = action[1]
        timer = action[2]
        action = action[0]
        if action == '1':
            walked = Walk(distance,hydration,bodytemp,startingitems,timer)
            hour += 4
            distance -= walked[0]
            hydration = walked[1]
            hydration = CheckValidBody(hydration)
            bodytemp = walked[2]
            bodytemp = CheckValidBody(bodytemp)
            watersource = random.choice([True,False])
            print ("You have used 4 hours to walk "+str(walked[0])+" km")
            hunger += 20
        elif action == '2':
            hour += 5
            print ("You have used 5 hours to rest, energy is restored")
            hydration -= 5
            if shelter:
                pass
            else:
                bodytemp -= 15
            if 'sleeping bag' in startingitems:
                bodytemp += 20
            else:
                bodytemp -= 0
            hunger += 15
            bodytemp = CheckValidBody(bodytemp)
            hydration = CheckValidBody(hydration)
        elif action == '3':
            captured = Hunting(scene, startingitems,watersource)
            hour += 1
            if captured[1] == 'True':
                if captured[0]:
                    print ("You saw a "+captured[0]+" and you captured it")
                    startingitems.append((captured[0]+' flesh'))
                    print ('You have used 1 hour to hunt')
                    hydration -= 15
                    hydration = CheckValidBody(hydration)
                    bodytemp += 15
                    bodytemp = CheckValidBody(bodytemp)
                else:
                    print ("You didn't see anything")
            elif captured[1] == 'False':
                print ("You saw a "+captured[0]+" and it escaped... bad luck!")
            else:
                print ("You saw a "+captured[0]+" and it attacked you, causing a "+captured[1]+" injury!")
                if captured[1] in ['broken ribs','lethal','neck']:
                    print ("YOU DIED")
                    print("GAME OVER")
                    flag = True
                    distance = 0
            hunger += 20
        elif action == '4':
            if timer == 0:
                search = CreateRandomSearch(scene)
                search_str = ''
            else:
                search = ["Nothing"]
                search_str = ''
            if search != []:
                for i in search:
                    search_str = search_str + i + ' '
                    startingitems.append(i)
                print (search_str + "is/are obtained")
            else:
                print ("Nothing is found")
            hour += 1
            bodytemp += 10
            bodytemp = CheckValidBody(bodytemp)
            hydration -= 10
            hunger += 10
            hydration = CheckValidBody(hydration)
            print ("You have used 1 hour to explore around you")
        elif action == '5':
            print ("Energy Bars are in Use Items Section. It has an amazing buff!")
            food = SearchFood(startingitems)
            try:
                startingitems = food[0]
                hunger -= food[1]
                CheckValidHunger(hunger)
            except:
                pass
        elif action == '6':
            water = DrinkWater(startingitems)
            try:
                hydration += water[0]
                hydration = CheckValidBody(hydration)
                startingitems = water[1]
            except:
                pass
        elif action == '7':
            DisplayInventory(startingitems)
        elif action == '8':
            check = UsableItemsOutput(startingitems)
            startingitems = check[0]
            used = check[1]
            useitem = UsedItem(hydration,bodytemp,hunger,used)
            hydration = useitem[0]
            bodytemp = useitem[1]
            hunger = CheckValidHunger(useitem[2])
        elif action == '9':
            if 'camp set' in startingitems:
                hour += 1
            else:
                hour += 4
            print ("Shelter Built, Rest would not decrease bodytemp.")
        elif action == '10':
            sys.exit(0)
    else:
        distance = 0
        if hydration <= 0:
            print ("You died of thirst")
            print ("GAME OVER...")
        elif bodytemp <= 0:
            print ("You died of hypothermia")
            print ("GAME OVER...")
        else:
            hunger >= 100
            print ("You have starved to death")
            print ("GAME OVER...")
if distance <= 0 and hydration > 0 and bodytemp > 0 and hunger < 100 and not flag:
        print ("WELL DONE! YOU SURVIVED!!!!!")
else:
    print("TRY AGAIN NEXT TIME")