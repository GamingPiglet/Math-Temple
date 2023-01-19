import random, math

from replit import db
from getkey import getkey, keys

run = True # keep game running

vwall = ["c", "v", "v", "v", "v", "v", "v", "c"] # vertical wall

room1 = [vwall, ["h", "s", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([5, 0]): 1}] # sample room, final dict for door storage

map = [["+", "-", " ", "-", " " "-", "+"], ["|", "3", " ", "2", " ", "4", "|"], ["+", "-", "+", " ", "+", "-", "+"], [" ", " ", "|", "1", "|", " ", " "], [" ", " ", "|", "0", "|", " ", " "], [" ", " ", " ", "-", " ", " ", " "]]

floor1 = [room1] # random gen these
floor2 = []
floor3 = [] # was going to make different room types then random gen their labels (1-1, 1-2, 1-3, etc.)
floor4 = []

master = [floor1, floor2, floor3, floor4]

deco = [",", ".", "'", '"', "`"] # decoration list to be picked from

for floor in master: # dw this is O(1)
  for room in floor:
    for column in room:
      for letter in column:
        if letter == "e":
          column[column.index(letter)] = random.choice([random.choice(deco), "e", "e", "e", "e", "e", "e", "e", "e", "e"]) # empty space can be a random decoration (1/10 chance)

playerInv = []

items1 = { # floor 1 items along with their flavour texts
  "bread": "A rather stale loaf of bread. Heals 15 HP.",
  "breadc": 5,
  "breads": "health",
  "chocolate stick": "Not a bar, but a stick of chocolate. Like the ones you break apart into two. Heals 23 HP.",
  "chocolate stickc": 7,
  "chocolate sticks": "health",
  "extra sharp stick": "An extra sharp stick. Nice! Deals 5 more damage on your next attack when used.",
  "extra sharp stickc": 5,
  "extra sharp sticks": "atk",
  "extra sharp stickt": 1,
  "crumb": "A strange looking crumb. You're not sure where this came from. Heals 10 HP.",
  "crumbc": 3,
  "crumbs": "health",
  "dusty textbook": "You aren't sure why, but you feel compelled to read it out loud. Decreases damage by 5 for 3 turns.",
  "dusty textbookc": 6,
  "dusty textbooks": "def",
  "dusty textbookt": 3
}

itemNames1 = ["bread", "chocolate stick", "extra sharp stick", "crumb", "dusty textbook"]

itemNameCaps1 = {
  "bread": "Bread",
  "chocolate stick": "Chocolate Stick",
  "extra sharp stick": "Extra Sharp Stick",
  "crumb": "Crumb",
  "dusty textbook": "Dusty Textbook"
}

enemies = {
  "bogey": {
    "health": 7,
    "atk": 3, # as an actual constant
    "def": 3,
    "crit": 1,
    "miss": 20,
    "xpYield": 5, # as an actual constant
    "moneyYield": 3,
    "initialText": "You are stopped by a brown blob in your tracks. It looks like a chocolate mochi abomination.\n",
    "encounterTexts": ["The blob wobbles aggressively.\n", "The blob hisses.\n", "The blob hops up and down.\n"]
  },
  "rotten apple": {
    "health": 5,
    "atk": 7,
    "def": 2,
    "crit": 1,
    "miss": 20,
    "xpYield": 6,
    "moneyYield": 5,
    "initialText": "As you walk, you find an apple at your feet. It then decided to grow to about your size and start biting you.",
    "encounterTexts": ["The apple rolls around.\n", "The apple rests against a wall.\n", "The apple spits out a little of its insides, and then eats it. \n"]
  },
  "dark cloud": {
    "health": 8,
    "atk": 5,
    "def": 4,
    "crit": 1,
    "miss": 20,
    "xpYield": 4,
    "moneyYield": 4,
    "initialText": "Some math student decided to concentrate all his stress into some black miasma to calm down. Now it's your problem to deal with.",
    "encounterTexts": ["The cloud floats around.\n", "The cloud splits itself, then reforms.\n", "The cloud sits there, menacingly.\n"]
  },
  "addition ninja": {
    "health": 14,
    "atk": 11,
    "def": 3,
    "crit": 2,
    "miss": 10,
    "xpYield": 8,
    "moneyYield": 10,
    "initialText": "This is a math student that watched too much Naruto. Now he's mad and wants to fill you with his plus-shaped shurikens.",
    "encounterTexts": ["The ninja tries to clone himself, then remembers all he can add is cuts to your body.\n", "The ninja does some parkour. You aren't impressed.\n", "The ninja spins his shurikens, then cuts himself.\n"]
  }
}

# when adding bosses, make sure you put the boss name last for easy grabbing
enemyNames1 = ["bogey", "rotten apple", "dark cloud", "addition ninja"] # creativity juice needed

enemyNames2 = []

enemyNames3 = []

enemyNames4 = []

enemyPools = [enemyNames1, enemyNames2, enemyNames3, enemyNames4]

enemyNameCaps1 = {
  "bogey": "Bogey",
  "rotten apple": "Rotten Apple",
  "dark cloud": "Dark Cloud",
  "addition ninja": "Addition Ninja"
}

tileSymbol = {
  "c": "+",
  "v": "|",
  "h": "—",
  "e": " ",
  "p": "@", 
  "d": "*",
  "s": "$"
}

playerStats = { # dict to store player stats
  "currentChar": "@",
  "floor": 0,
  "room": 0,
  "x": 4,
  "y": 6,
  "atk": 0, # unlike enemies, player atk and def are flat damage increases and decreases respectively
  "def": 0,
  "health": 100,
  "money": 0,
  "xp": 1, # as a level
  "xpProg": 0, # out of number determined by xp level
  "crit": 0.05, # chance as a %
  "miss": 0.05, # chance as a %
  "buffs": {
    "atk": {},
    "def": {}
  },
  "mapStates": [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
  ]
}

xpLevelToProg = [
  15
]

floorMath = [
  {
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
    "grade 9 problem": "answer",
  },
  {
    
  },
  {
    
  },
  {
    
  }
]

def printRoom(room):
  for y in range(len(room[0])): # column
    for x in range(len(room) - 1): # row
      tile = room[x][y]
      
      if x == playerStats["x"] and y == playerStats["y"]:
        print(playerStats["currentChar"], end = " ")
      elif tile in {",", ".", "'", '"', "`"}:
        print(tile + " ", end = "")
      else:
        print(tileSymbol[tile] + " ", end = "")
    print() # print \n after each row
  print() # print line break after printing room

printRoom(room1) # starting room print

playerRoom = master[playerStats["floor"]][playerStats["room"]] # indexes player's floor and room and prints it - prob put this somewhere suitable

# was gonna do a dictionary to read direction and output smth hmm oh yea oh true WAIT i ahve a genius idea sorta wait hmm uhh hmm OH oh OH Oh 

dirToCoord = {
  "up": "y",
  "upx": 0,
  "upy": -1,
  "down": "y",
  "downx": 0,
  "downy": 1,
  "left": "x",
  "leftx": -1,
  "lefty": 0,
  "right": "x",
  "rightx": 1,
  "righty": 0,
}

dirToRoom = {
  "up": [5, 6],
  "down": [5, 0],
  "left": [8, 4],
  "right": [8, 0]
}

def move(direction):
  global playerRoom
  posChar = playerRoom[playerStats["x"] + dirToCoord[direction + "x"]][playerStats["y"] + dirToCoord[direction + "y"]] # temp variable for the position of the character
  if posChar in {"v", "h"}: # if its a wall block them
    printRoom(playerRoom)
    print("You can't move to that tile!")
  elif posChar == "s": # if its a shop run shop
    shop1()
  else: # otherwise move them
    playerStats["x"] += dirToCoord[direction + "x"]
    playerStats["y"] += dirToCoord[direction + "y"]
    encounter = random.randint(1, 100)
    if playerRoom[playerStats["x"]][playerStats["y"]] == "d":
      if playerStats["room"] + playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])] == 4:
        print("You feel uneasy, do you want to proceed? (Boss room ahead, press enter to move forward)")
        e = getkey()
        if e == keys.ENTER:
          combat1(boss=True)
          if playerRoom[playerStats["x"]][playerStats["y"]] != "d":
            return
        else:
          print("Going back...")
          playerStats["x"] -= dirToCoord[direction + "x"]
          playerStats["y"] -= dirToCoord[direction + "y"]
          printRoom(playerRoom)
          return
      playerStats["room"] += playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])]
      playerStats["x"] = dirToRoom[direction][0]
      playerStats["y"] = dirToRoom[direction][1]
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      printRoom(playerRoom)
    if 1 <= encounter <= 15:
      playerStats["currentChar"] = "!"
      printRoom(playerRoom)
      combat1()
      playerStats["currentChar"] = "@"
      printRoom(playerRoom)
    else:
      printRoom(playerRoom)

runSuccess = False

def combat1(boss=False):
  global combatPI1
  global enemy1
  global currentEnemyHealth1
  combatPI1 = 0
  if boss:
    enemyName1 = enemyPools[playerStats["floor"]][-1]
  else:
    enemyName1 = random.choice(enemyPools[playerStats["floor"]])
    while enemyName1 == enemyPools[playerStats["floor"]][-1]:
      enemyName1 = random.choice(enemyPools[playerStats["floor"]])
  enemy1 = enemies[enemyName1]
  currentEnemyHealth1 = enemy1["health"]
  print(enemy1["initialText"]) # encounter text
  def combatPointer1Refresh():
    global combatPI1
    print("ATK INV RUN")
    combatPointer1 = [" ", " "]
    combatPointer1.insert(combatPI1, "^")
    print(" " + "   ".join(combatPointer1) + "\n")
  combatPointer1Refresh() # initial menu
  
  def atk1(enemy):
    global currentEnemyHealth1
    a = math.floor(3**(1 + 0.1*playerStats["xp"]))
    b = math.ceil(5**(1 + 0.1*playerStats["xp"]))
    playerAtkInt1 = random.randint(a, b) + playerStats["atk"]
    currentEnemyHealth1 -= playerAtkInt1
    print(f"You dealt {playerAtkInt1} damage to the {enemyNameCaps1[enemyName1]}!\n")

  def enemyAtk1():
    global enemy1
    chance = random.randint(1, 100)
    if chance <= enemy1["miss"]:
      print(f"{enemyNameCaps1[enemyName1]} missed!")
    elif chance >= enemy1["crit"]:
      enemyAtkInt1 = max(math.floor(1.5*random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)) - playerStats["def"], 0)
      playerStats["health"] -= enemyAtkInt1
      print(f"Critical! {enemyNameCaps1[enemyName1]} deals {enemyAtkInt1} damage.")
    else:
      enemyAtkInt1 = random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)
      playerStats["health"] -= enemyAtkInt1
      print(f"{enemyNameCaps1[enemyName1]} deals {enemyAtkInt1} damage.")

  def enemyDeath1():
    print(f"You killed the {enemyName1}.")
    xpGain1 = random.randint(enemy1["xpYield"] - 1, enemy1["xpYield"] + 1)
    moneyGain1 = random.randint(enemy1["moneyYield"] - 1, enemy1["moneyYield"] + 1)
    playerStats["xpProg"] += xpGain1
    playerStats["money"] += moneyGain1
    print(f"You gained {xpGain1} XP and ${moneyGain1}! (Level {playerStats['xp']}; {playerStats['xpProg']}/{xpLevelToProg[playerStats['xp'] - 1]} to next level)\n")
    if playerStats["xpProg"] >= xpLevelToProg[playerStats["xp"] - 1]:
      print("You levelled up!")
      playerStats["xpProg"] %= xpLevelToProg[playerStats["xp"]]
      playerStats["xp"] += 1
      # put stat increasing here
      

  global runSuccess
  while True:
    if currentEnemyHealth1 <= 0:
      enemyDeath1()
      return
    e = getkey()
    if e == keys.LEFT:
      combatPI1 = (combatPI1 - 1) % 3
      combatPointer1Refresh()
    elif e == keys.RIGHT:
      combatPI1 = (combatPI1 + 1) % 3
      combatPointer1Refresh()
    elif e == keys.ENTER:
      for i in playerStats["buffs"].keys():
        for e in playerStats["buffs"][i].keys():
          playerStats["buffs"][i][e]["duration"] -= 1
          if playerStats["buffs"][i][e]["duration"] == 0:
            playerStats[i] -= playerStats["buffs"][i][e]["change"]
            print(f"You lost a buff: -{playerStats['buffs'][i][e]['change']} {i}.")
      if combatPI1 == 0:
        atk1(enemy1)
        enemyAtk1()
        if playerStats["health"] <= 0:
          print("You died! Loading last save...")
          load()
          return
        print(random.choice(enemy1["encounterTexts"]))
        combatPointer1Refresh()# its good now !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      elif combatPI1 == 1:
        inv()
        enemyAtk1()
        combatPointer1Refresh()
      elif combatPI1 == 2:
        run(playerStats["floor"])
        if runSuccess == True:
          print(f"You fled from the {enemyNameCaps1[enemyName1]}.")
          runSuccess = False
          return
        else:
          print("You answered the problem wrong! Try again next turn.")
          enemyAtk1()
          print(random.choice(enemy1["encounterTexts"]))
          combatPointer1Refresh()

def inv():
  if len(playerInv) == 0:
    print("Your inventory is empty!\n")
    return

  invPI = 0
  
  def invRefresh():
    print("Your inventory (esc to exit):")
    invPI = 0
    for i in range(0, len(playerInv)):
      if i == invPI:
        print(f"{i + 1}: {playerInv[i]} <")
      else:
        print(f"{i + 1}: {playerInv[i]}")
  
  invRefresh() # initial inv display
  
  while True:
    e = getkey()
    if e == keys.UP:
      (invPI - 1) % 3
    elif e == keys.DOWN:
      (invPI + 1) % 3
    elif e == keys.ENTER:
      currentItem = playerInv[invPI]
      print()
      print(items1[currentItem] + "\n")
      print("Would you like to use this item? Press enter again to confirm.")
      confirm = getkey()
      if confirm == keys.ENTER:
        if (items1[currentItem + "s"] == "health"):
          playerStats["health"] += items1[currentItem + "c"]
          print(f"{items1[currentItem + 'c']} hp was restored.")
        else:
          playerStats["buffs"][items1[currentItem + "s"]][currentItem] = {"change": items1[currentItem + "c"], "duration": items1[currentItem + "t"]}
          playerStats[items1[currentItem + "s"]] += items1[currentItem + "c"]
          print(f"New buff: +{items1[currentItem + 'c']} {items1[currentItem + 's']} for {items1[currentItem + 't']} turns.\n")
        return
      else:
        invRefresh()
    elif e == keys.ESCAPE:
      return

def run(floor):
  global runSuccess
  mathProblem = random.choice(list(floorMath[floor].keys()))
  mathSolution = floorMath[floor][mathProblem]
  print(f"In order to run you must solve the following problem: {mathProblem}")
  mathSolInput = input("Enter: ")
  if mathSolInput == mathSolution:
    runSuccess = True
    return
  else:
    return
    
# also add healthbar and inv in both this and standard menu when moving around
  
# random gen "seed"
itemList1 = list()
random.shuffle(itemNames1)
for i in range(3): # for floor 1 shop items
  randomItem1 = itemNames1[i]
  itemList1.append(randomItem1)

itemState1 = [0, 0, 0] # so it doesn't get redefined in the shop1() function every time

def shop1():
  print("Welcome to the shop! Use arrow keys and enter to select your items below. Press esc to exit.\n")
  global shopPointerIndex1
  global itemList1
  global itemState1
  shopPointerIndex1 = 0
  itemChar1 = ["# ", "x "]
  def shopPointer1Refresh():
    global shopPointerIndex1
    itemPointer1 = [" ", " "]
    itemPointer1.insert(shopPointerIndex1, "^")
    itemDisplay1 = ""
    for i in range(3):
      itemDisplay1 += itemChar1[itemState1[i]]
    print(itemDisplay1)
    print(" ".join(itemPointer1) + "\n")
  def itemDesc1(itemName):
    print(f"Item: {itemNameCaps1[itemName]}\nDescription: {items1[itemName]}\nCost: {items1[itemName + 'c']}\n\nDo you wish to buy this item? (Press enter again to buy the item. Press esc to go back.)\n")
    while True:
      e = getkey()
      if e == keys.ENTER:
        if items1[itemName + "c"] > playerStats["money"]:
          print("You can't afford that!")
        else:
          playerInv.append(itemName)
          print(f"You have bought the {itemNameCaps1[itemName]}!\n")
          itemState1[shopPointerIndex1] += 1
          playerStats["money"] -= items1[itemName + "c"]
        shopPointer1Refresh()
        return
      elif e == keys.ESCAPE:
        shopPointer1Refresh()
        return
  shopPointer1Refresh()
  while True:
    e = getkey()
    if e == keys.LEFT:
      shopPointerIndex1 = (shopPointerIndex1 - 1) % 3
      shopPointer1Refresh()
    elif e == keys.RIGHT:
      shopPointerIndex1 = (shopPointerIndex1 + 1) % 3
      shopPointer1Refresh()
    elif e == keys.ENTER:
      if itemState1[shopPointerIndex1] == 0:
        itemDesc1(itemList1[shopPointerIndex1])
      else:
        print("You have already bought that item!\n")
        shopPointer1Refresh()
    elif e == keys.ESCAPE:
      print("Come back soon!\n")
      printRoom(playerRoom)
      return
      
      
def save():
  db["save"] = playerStats.copy() # put current player info in db
  db["inv"] = playerInv.copy()

def load():
  global playerStats
  global playerInv
  playerStats = db["save"].copy() # take saved player info from db
  playerInv = db["inv"].copy()

def printMap():
  for x in range(len(map)):
    for y in range(len(map[x])):
      if map[x][y].isnumeric():
        if int(map[x][y]) == playerStats["room"]:
          print("@", end="")
        elif int(map[x][y]) == 4:
          print("B", end="")
        elif playerStats["mapStates"][playerStats["floor"]][int(map[x][y])]:
          print(" ", end="")
        else:
          print("#", end="")
      else:
          print(map[x][y], end="")
    print()

if "save" in db.keys():
  load()

while run: # game loop
  # if player xp is sufficient run levelup
  e = getkey()
  if e == keys.UP:
    move("up")
  elif e == keys.DOWN:
    move("down")
  elif e == keys.LEFT:
    move("left")
  elif e == keys.RIGHT:
    move("right")
  elif e == "m":
    printMap()
  elif e == keys.ESCAPE:
    print("Would you like to quit Math Temple? Press esc again to quit.")
    quitConfirm = getkey()
    if quitConfirm == keys.ESCAPE:
      print("Goodbye!")
      run = False
    else:
      print("Back to Math Temple!")
