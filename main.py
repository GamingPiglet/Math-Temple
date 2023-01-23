import random, math, copy # import some builtin modules for operations

from replit import db # import replit module so we can use db for saving
from getkey import getkey, keys # import getkey package so we can use keypresses, keys is for handling keys like enter or tab

run = True # keep game running 

vwall = ["c", "v", "v", "v", "v", "v", "v", "c"] # vertical wall

# lists for storing room layouts. the final dictionary at the end with tuples as keys store door information
room10 = [vwall, ["h", "s", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([5, 0]): 1}]

room11 = [vwall, ["h", "e", "h", "e", "e", "e", "e", "h"], ["d", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "d"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], vwall, {tuple([5, 7]): -1, tuple([2, 0]): 1}]

room12 = [["c", "v", "v", "d", "v", "v", "v", "c"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "d"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["c", "v", "d", "v", "v", "v", "v", "c"], {tuple([2, 7]): -1, tuple([0, 3]): 1, tuple([9, 2]): 2}]

room13 = [vwall, ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "e", "e", "h"], ["h", "h", "e", "h", "v", "v", "e", "h"], ["h", "i", "e", "e", "h", "e", "e", "h"], ["h", "v", "v", "v", "h", "e", "v", "h"], ["h", "e", "e", "e", "h", "e", "e", "h"], ["h", "e", "v", "v", "v", "v", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "d", "v", "v", "v", "c"], {tuple([9, 3]): -1}]

room14 = [["c", "v", "d", "v", "v", "v", "v", "c"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "U", "v", "v", "v", "c"], {tuple([0, 2]): -2}]

room20 = [["e", "e", "e", "e", "e", "e", "e", "e"], vwall, ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "s", "h", "e", "v", "e", "h"], ["h", "e", "v", "h", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "h", "v", "v", "e", "e", "h"], ["d", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["c", "v", "v", "D", "v", "v", "v", "c"], {tuple([7, 0]): 1}]

room21 = [vwall, ["h", "e", "e", "e", "e", "v", "v", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "v", "h", "e", "e", "e", "h"], ["d", "e", "h", "v", "e", "e", "h", "h"], ["h", "e", "e", "e", "e", "e", "h", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "h", "v", "e", "e", "d"], ["h", "e", "e", "v", "h", "e", "e", "h"], vwall, {tuple([7, 7]): -1, tuple([3, 0]): 1, tuple([4, 0]): 1, tuple([6, 0]): 1}]

room22 = [["c", "v", "v", "v", "v", "v", "d", "c"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "v", "v", "v", "v", "v", "h"], ["h", "e", "e", "h", "e", "e", "e", "d"], ["h", "v", "e", "h", "e", "e", "e", "d"], ["h", "e", "e", "e", "e", "h", "v", "v"], ["h", "e", "e", "e", "e", "h", "e", "d"], ["h", "e", "v", "v", "e", "h", "v", "v"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "v", "v", "d", "v", "c"], {tuple([3, 7]): -1, tuple([4, 7]): -1, tuple([6, 7]): -1, tuple([0, 6]): 1, tuple([9, 5]): 2}]

room23 = [["c", "v", "v", "v", "v", "v", "v", "v", "c"], ["h", "e", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "h", "v", "v", "v", "h", "e", "h"], ["h", "e", "h", "e", "e", "e", "h", "e", "h"], ["h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "e", "h", "i", "h", "e", "h", "e", "h"], ["h", "e", "h", "v", "e", "e", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "e", "h"], ["c", "v", "v", "v", "v", "v", "d", "v", "c"], {tuple([9, 6]): -1}]

room24 = [["c", "v", "v", "v", "v", "d", "v", "c"], ["U", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "v", "v", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], vwall, {tuple([0, 5]): -2}]

room30 = [["v", "v", "v", "v", "v", "v", "v", "c"], ["D", "e", "e", "e", "e", "e", "e", "h"], ["v", "v", "v", "v", "v", "v", "e", "h"], ["d", "e", "e", "e", "h", "e", "e", "h"], ["v", "v", "h", "e", "h", "e", "e", "h"], ["d", "e", "h", "e", "h", "e", "e", "h"], ["v", "e", "h", "e", "h", "e", "e", "h"], ["d", "e", "h", "e", "h", "e", "v", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([1, 0]): 1, tuple([3, 0]): 1, tuple([5, 0]): 1, tuple([7, 0]): 1}]

room31 = [["v", "v", "v", "v", "v", "v", "v", "c"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["v", "v", "v", "v", "v", "h", "e", "h"], ["d", "e", "e", "e", "e", "h", "e", "d"], ["v", "e", "v", "v", "e", "h", "v", "v"], ["d", "e", "e", "e", "e", "e", "e", "d"], ["v", "v", "v", "v", "v", "v", "v", "v"], ["h", "h", "e", "e", "e", "e", "e", "d"], ["h", "h", "e", "e", "h", "e", "e", "h"], ["c", "v", "v", "d", "v", "d", "v", "c"], {tuple([3, 7]): -1, tuple([5, 7]): -1, tuple([7, 7]): -1, tuple([1, 0]): 1, tuple([3, 0]): 1, tuple([5, 0]): 1, tuple([9, 3]): 4, tuple([9, 5]): 4}]

room32 = [["c", "v", "v", "v", "d", "v", "v", "v"], ["h", "e", "e", "e", "e", "h", "e", "d"], ["h", "v", "e", "h", "e", "h", "v", "v"], ["h", "e", "e", "h", "e", "e", "e", "d"], ["h", "e", "v", "v", "v", "h", "e", "v"], ["h", "e", "e", "e", "e", "h", "e", "d"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["h", "e", "v", "v", "v", "v", "v", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "v", "v", "d", "v", "c"], {tuple([0, 4]): 1, tuple([1, 7]): -1, tuple([3, 7]): -1, tuple([5, 7]): -1, tuple([9, 5]): 2}]

room33 = [["c", "v", "v", "v", "v", "v", "c"], ["h", "h", "e", "h", "e", "h", "h"], ["h", "e", "s", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "h"], ["h", "e", "e", "e", "e", "e", "h"], ["h", "h", "e", "h", "e", "h", "h"], ["h", "e", "h", "e", "e", "e", "h"], ["h", "h", "e", "h", "e", "h", "h"], ["h", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "v", "d", "v", "c"], {tuple([9, 4]): -1}]

room34 = [["c", "v", "v", "v", "v", "d", "v", "c"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "U", "v", "e", "v", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([0, 5]): -2}]

room35 = [["c", "v", "v", "d", "v", "d", "v", "c"], ["h", "e", "e", "e", "h", "e", "e", "h"], ["h", "e", "v", "v", "v", "v", "e", "h"], ["h", "e", "h", "h", "h", "h", "e", "h"], ["h", "e", "h", "h", "h", "h", "e", "h"], ["h", "e", "h", "h", "h", "h", "e", "h"], ["h", "e", "h", "h", "h", "h", "e", "h"], ["h", "e", "v", "v", "v", "v", "e", "h"], ["h", "e", "e", "i", "e", "e", "e", "h"], vwall, {tuple([0, 3]): -4, tuple([0, 5]): -4}]

room40 = [vwall, ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "v", "v", "e", "v", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "v", "e", "v", "v", "h", "e", "d"], ["h", "e", "e", "e", "e", "h", "v", "h"], ["h", "v", "v", "h", "e", "e", "e", "h"], ["h", "e", "D", "h", "v", "v", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([4, 7]): 1}]

room41 = [["c", "v", "d", "v", "d", "v", "d", "v", "d", "v", "d", "c"], ["h", "v", "e", "v", "e", "e", "e", "v", "i", "v", "e", "h"], ["h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h", "h"], ["h", "e", "e", "v", "e", "e", "e", "e", "e", "v", "e", "h"], ["d", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h", "h"], ["h", "e", "e", "e", "e", "v", "e", "e", "e", "e", "e", "d"], ["h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h", "h"], ["h", "v", "e", "e", "e", "e", "e", "e", "e", "e", "e", "d"], ["h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h", "h"], ["c", "v", "v", "v", "v", "v", "v", "v", "v", "v", "v", "c"], {tuple([4, 0]): -1, tuple([0, 2]): 4, tuple([0, 4]): 4, tuple([0, 6]): 4, tuple([0, 8]): 4, tuple([0, 10]): 4, tuple([5, 11]): 1, tuple([7, 11]): 1}]

room42 = [["c", "v", "v", "v", "v", "v", "v", "v", "v", "c"], ["h", "e", "e", "e", "e", "e", "e", "e", "e", "d"], ["h", "e", "e", "h", "e", "e", "e", "h", "e", "d"], ["h", "e", "h", "h", "h", "e", "h", "h", "h", "d"], ["h", "e", "e", "h", "e", "e", "e", "h", "e", "d"], ["d", "e", "e", "e", "e", "e", "e", "e", "e", "d"], ["v", "v", "v", "v", "v", "v", "h", "e", "e", "d"], ["d", "e", "h", "e", "e", "e", "h", "v", "v", "h"], ["h", "e", "e", "e", "h", "e", "e", "e", "h", "h"], ["c", "v", "v", "v", "v", "v", "v", "d", "v", "c"], {tuple([5, 0]): -1, tuple([7, 0]): -1, tuple([1, 9]): 2, tuple([2, 9]): 2, tuple([3, 9]): 2, tuple([4, 9]): 2, tuple([5, 9]): 2, tuple([6, 9]): 2, tuple([9, 7]): 1}]

room43 = [["c", "v", "v", "v", "v", "v", "v", "d", "v", "c"], ["h", "s", "h", "e", "e", "e", "h", "e", "e", "h"], ["h", "e", "h", "e", "h", "e", "h", "h", "e", "h"], ["h", "e", "e", "e", "h", "e", "e", "e", "e", "h"], ["c", "v", "v", "v", "v", "v", "v", "v", "v", "c"], {tuple([0, 7]): -1}]

room44 = [["v", "v", "v", "v", "v", "v", "v", "c"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([1, 0]): -2, tuple([2, 0]): -2, tuple([3, 0]): -2, tuple([4, 0]): -2, tuple([5, 0]): -2, tuple([6, 0]): -2}]

room45 = [["c", "v", "v", "v", "v", "v", "v", "v", "v", "v", "v", "c"], ["h", "h", "e", "e", "e", "e", "e", "e", "e", "e", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "h", "e", "h", "e", "h", "e", "h"], ["h", "h", "d", "h", "d", "h", "d", "h", "d", "h", "d", "h"], {tuple([11, 2]): -4, tuple([11, 4]): -4, tuple([11, 6]): -4, tuple([11, 8]): -4, tuple([11, 10]): -4}]

# putting the rooms into lists for indexing
floor1 = [room10, room11, room12, room13, room14]
floor2 = [room20, room21, room22, room23, room24]
floor3 = [room30, room31, room32, room33, room34, room35]
floor4 = [room40, room41, room42, room43, room44, room45]

# stores the entire temple in one list
master = [floor1, floor2, floor3, floor4]

# map layouts for each floor. the number corresponds to a room and is used to index a value later on to see if that room has been visited before
map1 = [["+", "-", " ", "-", " " "-", "+"], ["|", "3", " ", "2", " ", "4", "|"], ["+", "-", "+", " ", "+", "-", "+"], [" ", " ", "|", "1", "|", " ", " "], [" ", " ", "|", "0", "|", " ", " "], [" ", " ", " ", "-", " ", " ", " "]]

map2 = [["+", "-", " ", "-", " ", "-", "+"], ["|", "3", " ", "2", " ", "4", "|"], ["+", "-", "+", " ", "+", "-", "+"], [" ", " ", "|", "1", " ", "5", "|"], [" ", " ", "|", "0", "+", "-"], [" ", " ", " ", "-"]]

map3 = [[" ", " ", "+", "-", "+"], ["+","-","+", "0", "|"], ["|", "5", " ", "1", "+", "-", "+"], ["+", "-", "+", "2", " ", "3", "|"], [" ", " ", "|", "4", "+", "-", "+"], [" ", " ", " ", "-"]]

# stores the layouts in 1 convenient list for indexing later
maps = [map1, map1, map2, map3]

deco = [",", ".", "'", '"', "`"] # decoration list to be picked from

for floor in master: # randomizes decoration throughout each room
  for room in floor:
    for column in room:
      for letter in column:
        if letter == "e":
          column[column.index(letter)] = random.choice([random.choice(deco), "e", "e", "e", "e", "e", "e", "e", "e", "e"]) # empty space can be a random decoration (1/10 chance)

playerStats = { # dict to store player stats
  "currentChar": "@", # player char changes to ! once combat begins, so we store the player's current character so we can just index a value once we have to print the player
  "floor": 0, # player position values, x and y are based on 0, 0 in the room being the top left corner
  "room": 0, # stores which room player is in
  "x": 4,
  "y": 6,
  "atk": 0, # unlike enemies, player atk and def are flat damage increases and decreases respectively
  "def": 0,
  "health": 100, # self-explanatory
  "money": 0,
  "xp": 0, # as a level
  "xpProg": 0, # out of number determined by xp level
  "crit": 15, # chance as a %
  "miss": 10, # chance as a %
  "buffs": { # stores player buffs by item used. the item names are mapped to dictionaries that store its duration and how much they change the stat so we can simply decrement the duration and subtract the other value from the current value of the stat
    "atk": {},
    "def": {}
  },
  "mapStates": [ # stores which rooms the player has visited on the floor. the first room of any floor will always be visited, so it's true by default
    [True, False, False, False, False],
    [True, False, False, False, False],
    [True, False, False, False, False, False],
    [True, False, False, False, False, False]
  ]
}

playerRoom = master[playerStats["floor"]][playerStats["room"]] # index player room from the master list, stores entire temple

playerInv = [] # list that stores the items the player bought

items = { # dictionary of items that shops sell. keys that are just item names are the description, item names + c is cost, item name + s is the stat they change, item name + t is the duration they last if aren't heals, and item name + b is how much they change the stat. if an item has stat unusable, they're a boss drop and merely print the statement under item name + c once used
  "bread": "A rather stale loaf of bread. Heals 15 HP.",
  "breadc": 4,
  "breads": "health",
  "breadb": 15,
  "chocolate stick": "Not a bar, but a stick of chocolate. Like the ones you break apart into two. Heals 23 HP.",
  "chocolate stickc": 7,
  "chocolate sticks": "health",
  "chocolate stickb": 23,
  "extra sharp stick": "An extra sharp stick. Nice! Deals 3 more damage on your next attack when used.",
  "extra sharp stickc": 5,
  "extra sharp sticks": "atk",
  "extra sharp stickt": 1,
  "extra sharp stickb": 3,
  "crumb": "A strange looking crumb. You're not sure where this came from. Heals 10 HP.",
  "crumbc": 3,
  "crumbs": "health",
  "crumbb": 10,
  "dusty textbook": "You aren't sure why, but you feel compelled to read it out loud. Decreases damage by 4 for 3 attacks.",
  "dusty textbookc": 6,
  "dusty textbooks": "def",
  "dusty textbookt": 3,
  "dusty textbookb": 4,
  "golden three": "The Golden Three! Increases your attack by a whopping 33 for 3 turns through the power of sheer confidence.", # floor 1 special item
  "golden threec": (4, 1),
  "golden threes": "atk",
  "golden threet": 3,
  "golden threeb": 33,
  "study note 1": "Dropped by the addition ninja. Seems to be grade 9 material.",
  "study note 1c": "In any linear equation in y-intercept form y = mx + b, m gives the slope of the line and b gives the y-intercept. The slope affects how steep the line appears and the y-intercept not only is equal to y in the point (0, y) but also represents how high or low the line is (its vertical shift). Parallel lines have the same slope m and perpendicular lines have slopes that are negative reciprocals of each other (e.g. a perpendicular line to y = 2x + 3 would be y = -x/2).",
  "study note 1s": "unusable",
  "apple core": "A rotten apple core. Smells rancid. Decreases damage by 6 for 1 turn.",
  "apple corec": 7,
  "apple cores": "def",
  "apple coret": 1,
  "apple coreb": 6,
  "empty crate": "The apples all around this floor have to be carried somehow. Deals 6 more damage for 4 attacks.",
  "empty cratec": 11,
  "empty crates": "atk",
  "empty cratet": 4,
  "empty crateb": 6,
  "instant boba": "Bubble tea made from powder packets and milk. Not as good as the real thing, but gets the job done. Heals 17 HP.",
  "instant bobac": 9,
  "instant bobas": "health",
  "instant bobab": 17,
  "protein bar": "Doesn't taste great, but it's healthy. Heals 13 HP.",
  "protein barc": 8,
  "protein bars": "health",
  "protein barb": 13,
  "breakfast burger": "Egg between 2 english muffins. Filling enough to start your day. Heals 27 HP.",
  "breakfast burgerc": 12,
  "breakfast burgers": "health",
  "breakfast burgerb": 27,
  "book of life": "The book doesn't actually say anything. You can however feel a powerful pulse emanating from it. Heals a gratifying 75 HP.", # floor 2 special item
  "book of lifec": (6, 3),
  "book of lifes": "health",
  "book of lifeb": 75,
  "study note 2": "Dropped by the subtraction paladin. Seems to be grade 10 material.",
  "study note 2c": "The quadratic formula gives up to 2 values of x for the roots of any quadratic in standard form ax^2 + bx + c. The formula is x = (-b +- sqrt(b^2 - 4ac))/2a. In the formula, the b^2 - 4ac under the square root is known as the determinant and allows us to deduce the number of roots of the quadratic. If it is positive, there are two roots; if it is zero, there is one root; if it is negative, there are no real roots/there are two complex roots.",
  "study note 2s": "unusable",
  "bubble tea": "Very popular among students. Heals 20 HP.",
  "bubble teac": 14,
  "bubble teas": "health",
  "bubble teab": 20,
  "compass": "Not great for slicing, but you're good at stabbing. Deals 8 more damage for 6 attacks.",
  "compassc": 12,
  "compasss": "atk",
  "compasst": 6,
  "compassb": 8,
  "notebook": "Flexible enough to redirect attacks. Decreases damage by 9 for 3 turns.",
  "notebookc": 13,
  "notebooks": "def",
  "notebookt": 3,
  "notebookb": 9,
  "french fries": "Would be nice with some other food, but you can down them in a few bites. Heals 16 HP.",
  "french friesc": 10,
  "french friess": "health",
  "french friesb": 16,
  "whole pizza": "As filling as a full-course meal. Heals 27 HP.",
  "whole pizzac": 17,
  "whole pizzas": "health",
  "whole pizzab": 27,
  "platinum four": "The Platinum Four! Increases your defense by 44 (effectively making you invincible!) for 4 turns by sheer courage.",
  "platinum fourc": (8, 3),
  "platinum fours": "def",
  "platinum fourt": 4,
  "platinum fourb": 44,
  "study note 3": "Dropped by the multiplication mage. Seems to be grade 11 material.",
  "study note 3c": "The special angles are 30, 45, and 60 degrees. sin(30 deg) = 1/2, sin(45 deg) = sqrt(2)/2, sin(60 deg) = sqrt(3)/2; similarly cos(30 deg) = sqrt(3)/2, cos(45 deg) = sqrt(2)/2, cos(60 deg) = 1/2. For the future, 180 degrees = pi radians.",
  "study note 3s": "unusable",
  "scissors": "Longer blade, deeper cuts. Deals 10 more damage for 6 attacks.",
  "scissorsc": 20,
  "scissorss": "atk",
  "scissorst": 6,
  "scissorsb": 10,
  "backpack": "Too small to hold anything, but you can toss it to dampen attacks. Decreases damage by 11 for 3 turns.",
  "backpackc": 19,
  "backpacks": "def",
  "backpackt": 3,
  "backpackb": 11,
  "brown sugar boba": "The brown sugar pearls make it taste much better. Heals 24 HP.",
  "brown sugar bobac": 18,
  "brown sugar bobas": "health",
  "brown sugar bobab": 24,
  "chicken burger combo": "A meaty chicken burger, plus some fries and a drink make a great quick lunch. Heals 30 HP.",
  "chicken burger comboc": 21,
  "chicken burger combos": "health",
  "chicken burger combob": 30,
  "lunch wrap": "A small but easy to digest meal for tight situations. Heals 20 HP.",
  "lunch wrapc": 17,
  "lunch wraps": "health",
  "lunch wrapb": 20,
  "division by zero": "A single, small piece of paper. On it is \"0/0\" written in black ink. You're not too sure what this will do.",
  "division by zeroc": (1, 8),
  "division by zeros": random.choice(["atk", "def", "health"]),
  "division by zerot": random.randint(1, 3),
  "division by zerob": random.randint(200, 300),
  "study note 4": "Dropped by the division gunner. Seems to be grade 12 material.",
  "study note 4c": "The integral of sec(x)dx is ln|sec(x) + tan(x)| + C. Thanks for playing!",
  "study note 4s": "unusable"
}

# lists that store item names per floor, and then another list that stores them in order so we can index the right pool by the player's current floor
itemNames1 = ["bread", "chocolate stick", "extra sharp stick", "crumb", "dusty textbook"]

itemNames2 = ["apple core", "empty crate", "instant boba", "protein bar", "breakfast burger"]

itemNames3 = ["bubble tea", "compass", "notebook", "french fries", "whole pizza"]

itemNames4 = ["scissors", "backpack", "brown sugar boba", "chicken burger combo", "lunch wrap"]

# stores study note names by floor so the program can find which one to drop by indexing with player's current floor
studyNotes = ["study note 1", "study note 2", "study note 3", "study note 4"]

itemPools = [itemNames1, itemNames2, itemNames3, itemNames4]

# stores special items, ordered this way for same reason as study notes
specialItems = ["golden three", "book of life", "platinum four", "division by zero"]

# stores which items the shop on each floor sells 
shopPools = [[], [], [], []]

# will be used to store which items in each shop has been bought. stores numbers to make printing out items easier later
itemStates = [[], [], [], []]

# dictionary storing enemies. stats are self-explanatory, initialtext is for the message indicating what enemy you're fighting, and encountertexts is for messages that appear throughout the fight
enemies = {
  "bogey": {
    "health": 58,
    "atk": 3, # as an actual constant
    "def": 2,
    "crit": 5,
    "miss": 20,
    "xpYield": 5, # as an actual constant
    "moneyYield": 3,
    "initialText": "You are stopped by a brown blob in your tracks. It looks like a chocolate mochi abomination.\n",
    "encounterTexts": ["The blob wobbles aggressively.\n", "The blob hisses.\n", "The blob hops up and down.\n"]
  },
  "rotten apple": {
    "health": 61,
    "atk": 7,
    "def": 2,
    "crit": 5,
    "miss": 20,
    "xpYield": 6,
    "moneyYield": 5,
    "initialText": "As you walk, you find an apple at your feet. It then decided to grow to about your size and start biting you.\n",
    "encounterTexts": ["The apple rolls around.\n", "The apple rests against a wall.\n", "The apple spits out a little of its insides, and then eats it. \n"]
  },
  "dark cloud": {
    "health": 67,
    "atk": 5,
    "def": 3,
    "crit": 5,
    "miss": 20,
    "xpYield": 4,
    "moneyYield": 4,
    "initialText": "Some math student decided to concentrate all his stress into some black miasma to calm down. Now it's your problem to deal with.\n",
    "encounterTexts": ["The cloud floats around.\n", "The cloud splits itself, then reforms.\n", "The cloud sits there, menacingly.\n"]
  },
  "addition ninja": {
    "health": 110,
    "atk": 11,
    "def": 4,
    "crit": 10,
    "miss": 10,
    "xpYield": 25,
    "moneyYield": 10,
    "initialText": "This is a math student that watched too much Naruto. Now he's mad and wants to fill you with his plus-shaped shurikens.\n",
    "encounterTexts": ["The ninja tries to clone himself, then remembers all he can add is cuts to your body.\n", "The ninja does some parkour. You aren't impressed.\n", "The ninja spins his shurikens, then cuts himself.\n"]
  },
  "angry student": {
    "health" : 90,
    "atk": 9,
    "def": 6,
    "crit": 5,
    "miss": 20,
    "xpYield": 13,
    "moneyYield": 9,
    "initialText": "This student cracked under pressure and is now killing anything that moves. Which means you.\n",
    "encounterTexts": ["The student punches a wall.\n", "The student starts screaming.\n", "The student tries deep breathing, but it does nothing.\n"]
  },
  "apple muncher": {
    "health": 107,
    "atk": 6,
    "def": 8,
    "crit": 5,
    "miss": 20,
    "xpYield": 15,
    "moneyYield": 10,
    "initialText": "Remember those math problems where someone buys a massive number of apples? This is that someone, and he's not moving out of your way.\n",
    "encounterTexts": ["The muncher tries to get an apple, but only gets a core.\n", "The muncher places an order for more apples.\n", "The muncher raves on about apples. You tune him out.\n"]
  },
  "quadratic enthusiast": {
    "health": 103,
    "atk": 8,
    "def": 6,
    "crit": 5,
    "miss": 20,
    "xpYield": 14,
    "moneyYield": 8,
    "initialText": "This little prankster likes to throw baseballs at the perfect angle to hit someone in the head. How does he do it? He got a little too into graphing parabolas.\n",
    "encounterTexts": ["The enthusiast throws a ball at a wall, then tries to find the equation of its arc.\n", "The enthusiast throws a ball at a muncher. It lands.\n", "The enthusiast answers an angry call.\n"]
  },
  "subtraction paladin": {
    "health": 150,
    "atk": 14,
    "def": 10,
    "crit": 15,
    "miss": 20,
    "xpYield": 40,
    "moneyYield": 9,
    "initialText": "A theatre student that also happens to be into math got a little too into his role as a paladin. Now he has a god complex and fights anyone he sees.\n",
    "encounterTexts": ["The paladin hoists his axe onto his shoulder, and bounces it on his shoulder.\n", "The paladin lets out a hearty warcry.\n", "The paladin adjusts his helmet.\n"]
  },
  "wave clacker": {
    "health": 137,
    "atk": 16,
    "def": 8,
    "crit": 5,
    "miss": 20,
    "xpYield": 19,
    "moneyYield": 11,
    "initialText": "This trig student got a little too into graphs, so he got clackers just so he could have something to model. Unfortunately, those clackers are also pretty lethal, and heading right for you.\n",
    "encounterTexts": ["The student lets his clackers swing as he visualizes a graph.\n", "The student slows down the clackers to rest his hand.\n", "The student's clackers slip out of his hand and into a wall, so he goes and grabs them.\n"]
  },
  "trigbot": {
    "health": 145,
    "atk": 14,
    "def": 11,
    "crit": 5,
    "miss": 20,
    "xpYield": 23,
    "moneyYield": 8,
    "initialText": "Someone got too tired of using their calculator for trig functions, so they made this robot to do it for them. They forgot to program the 3 laws of robotics, so it's also murderous.\n",
    "encounterTexts": ["The robot sees a mouse, then starts trying to kill it.\n", "The robot sees a triangle on a wall and immediately tries to solve it.\n", "The robot starts thinking of the best way to cut you into triangles.\n"]
  },
  "enlightened bogey": {
    "health": 142,
    "atk": 15,
    "def": 9,
    "crit": 5,
    "miss": 20,
    "xpYield": 21,
    "moneyYield": 9,
    "initialText": "A bogey managed to get its hands on a textbook, learning so much from it that it has ascended to a new plane of consciousness. Not that it doesn't have a physical body that it's trying to attack you with.\n",
    "encounterTexts": ["The bogey seems to be reading another textbook in its mind.\n", "The bogey tries to make a textbook appear, but forgets it can't do that in the physical world.\n", "The bogey starts dancing, but nothing happens.\n"]
  },
  "multiplication mage": {
    "health": 250,
    "atk": 20,
    "def": 15,
    "crit": 10,
    "miss": 5,
    "xpYield": 60,
    "moneyYield": 13,
    "initialText": "This student read a forbidden textbook and gained power over multiplication. Now he can multiply the number of stab wounds you have with his darts.\n",
    "encounterTexts": ["The mage reminisces about the time he gave someone 28 stab wounds.\n", "The mage tries to multiply himself, then realizes he has no idea how clones work.\n", "The mage restocks his dart supply.\n"]
  },
  "straight-curve samurai": {
    "health": 233,
    "atk": 25,
    "def": 16,
    "crit": 20,
    "miss": 20,
    "xpYield": 22,
    "moneyYield": 15,
    "initialText": "When this student had to show off a visual example of derivatives in his calculus class, he decided to use a real katana. Everyone stopped laughing when he cut them all in half.\n",
    "encounterTexts": ["The samurai does some practice swings.\n", "The samurai yells out a one-liner like an anime protagonist.\n", "The samurai starts talking about waifus, but you immediately tune him out.\n"]
  },
  "l'hôpital boxer": {
    "health": 271,
    "atk": 28,
    "def": 14,
    "crit": 20,
    "miss": 20,
    "xpYield": 27,
    "moneyYield": 17,
    "initialText": "This student is at the top of his calc class. He also happens to be a boxer that is planning on sending you to the hospital.\n",
    "encounterTexts": ["The boxer does some practice jabs.\n", "The boxer starts jumping around to psych himself up.\n", "The boxer punches a nearby wall.\n"]
  },
  "integrating pyromaniac": {
    "health": 314,
    "atk": 24,
    "def": 17,
    "crit": 20,
    "miss": 20,
    "xpYield": 35,
    "moneyYield": 20,
    "initialText": "This student likes to \"integrate\" stuff by melting them together with fire. He isn't that good at actual integration, though.\n",
    "encounterTexts": ["The pyromaniac strikes his lighter a few times.\n", "The pyromaniac thinks about making molotovs, then remembers he doesn't have alcohol on him.\n", "The pyromaniac checks how many matches he has in his matchbox.\n"]
  },
  "division gunner": {
    "health": 1729,
    "atk": 29,
    "def": 20,
    "crit": 40,
    "miss": 25,
    "xpYield": 100,
    "moneyYield": 18,
    "initialText": "Unlike the other bosses, the Division Gunner went for full efficiency in his fighting power. That's why he's aiming 2 custom-made rubber band launchers at you.\n",
    "encounterTexts": ["The gunner twirls his launchers.\n", "The gunner checks on his rubber bands.\n", "The gunner shoots a wall.\n"]
  }
}

# lists for storing enemy names, and another list for ordering them by floor to easily grab the right list. we store bosses as the last element in these lists so we can hard code an index when getting them
enemyNames1 = ["bogey", "rotten apple", "dark cloud", "addition ninja"]

enemyNames2 = ["angry student", "apple muncher", "quadratic enthusiast", "subtraction paladin"]

enemyNames3 = ["wave clacker", "trigbot", "enlightened bogey", "multiplication mage"]

enemyNames4 = ["deriving samurai", "l'hôpital boxer", "integrating pyromaniac", "division gunner"]

enemyPools = [enemyNames1, enemyNames2, enemyNames3, enemyNames4]

# variable used to check if player should escape enemy when running
runSuccess = False

# translate internally stored characters to proper ascii art with this dictionary
tileSymbol = {
  "c": "+",
  "v": "|",
  "h": "—",
  "e": " ",
  "p": "@", 
  "d": "*",
  "s": "$",
  "i": "?",
  "U": "^",
  "D": "^"
}

# stores the xp required to get to each level from 1 onwards
xpLevelToProg = [
  15,
  25,
  50,
  75,
  100,
  125,
  150,
  175,
  200,
  225,
  250,
  275,
  300,
  314,
  314,
  314,
  314,
  314
]

# stores the max hp you can have at each level
levelToHealthMax = [
  100,
  104,
  108,
  114,
  121,
  131,
  142,
  159,
  176,
  203,
  231,
  275,
  320,
  392,
  464,
  580,
  697,
  848,
]

# the problems that you have to answer whenever you choose to run from an enemy. if you answer correctly, you get away
floorMath = [
  { # floor 1 questions (gr 9 math)
    "What is the slope of equation y = 2x + 3?": 2,
    "Fill in the blank: the Basel problem describes the sum of the ___ of all squares.": "reciprocals",
    "What is the midpoint of line AB if A = (2, 3) and B = (4, -1)?": "(3, 1)",
    "What is the first term of polynomial 4x + 7x^3 - 13 in standard form?": "7x^3",
    "What is the coefficient of x^2 after combining like terms in polynomial 7y + 9x - 3x^2 + 3y + 2x^2?": -1,
    "When multiplying terms with the same base, do you add or multiply their powers?": "add",
    "What is x, if 24x - 5 = 43?": 2,
    "What is x, if x/3 = 8?": 24,
    "What is the y coordinate of the y-intercept in equation y = 2x + 9?": 9,
    "What is the slope of equation 3y - 15 = 21x?": 7,
    "What is the y coordinate of the y-intercept in equation 6y - 2x = 18?": 3,
    "What is the degree of polynomial x^2 * y^3 + xy^2 - 5?": 5,
    "How many degrees do the angles of a triangle add up to?": 180,
    "Triangle ABC has side lengths AB = 5, AC = 13, and angle ABC = 90 degrees. What is the length of side BC?": 12,
    "How many degrees do a pair of complementary angles add up to?": 90,
    "How many degrees do a pair of supplementary angles add up to?": 180,
    "Fill in the blank: two lines are ___ when they intersect at a 90 degree angle.": "perpendicular",
    "What is the slope of y = 3?": 0,
    "What is the x coordinate of the point of intersection between lines y = 2x + 3 and y = 8x - 9?": 2,
    "True or false: all coefficients must be integers in a standard form linear equation.": "true",
  },
  { # floor 2 questions (gr 10 math)
    "What is the x-coordinate of the vertex of equation y = 2x^2 - 12x + 5?": 3,
    "What is the positive root of equation y = x^2 + x - 6?": 2,
    "Fill in the blank: located in the quadratic formula, the ___ allows us to deduce the number of real roots of a quadratic equation.": "discriminant",
    "True or false: a quadratic can have 1-2 real roots.": "false",
    "What is x, if x is positive and 2x^2 - 5x - 12 = 0?": 4,
    "How many different quadratic forms are there?": 3,
    "What is the value of the definite integral from e^2 to e^14 of ln(x)/x dx?": 96,
    "Fill in the blank: the similar triangle congruencies are commonly abbreviated as AA, SAS, and ___.": "SSS",
    "True or false: sin(x) represents h/o, where h is the hypotenuse side and o is the opposite side.": "false",
    "Fill in the blank: the two methods to solving systems of equations are called substitution and ___.": "elimination",
    "Fill in the blank: inverse cosine has three names—cos^-1, ___, and arccos.": "acos",
    "True or false: the sine law works for any right triangle.": "true",
    "True or false: the trigonometric ratios can be used to identify missing side lengths and angles in any triangle.": "false",
    "True or false: the cosine law works for any triangle, EVEN non-right triangles.": "true",
    "What is the line drawn from the vertex of a triangle to the midpoint of the opposite side called?": "median",
    "At what value x in degrees are sin(x) and cos(x) equal?": 45,
    "True or false: you can complete the square for any quadratic equation.": "true",
    "What is the shape of a quadratic equation's graph called?": "parabola",
    "Fill in the blank: the graph of y = x^2 - 5x + 17 opens ___.": "up",
    "What is the value of (sin(60 deg))^2 + (cos(60 deg))^2?": 1
  },
  { # floor 3 questions (gr 11 math)
    "If f(x) = x^2 + 6, what is f(3)?": 15,
    "True or false: the harmonic series converges.": "false",
    "What is cos(60 deg) as a fraction?": "1/2",
    "What is the parent function of 1/(x + 6)?": "1/x",
    "Calculate 5 + 15 + 45... to 17 terms.": 322850405,
    "Calculate 4 + 7 + 11... to 53 terms.": 4346,
    "Fill in the blank: in any expression y = a*f(k(x - d)) + c, k represents the ___ compression.": "horizontal",
    "Evaluate 125^(5/3).": 3125,
    "Evaluate log(100).": 2,
    "Fill in the blank: the range of y = (x - 4)^2 + 3 is {y | y ∈ R, y ≥ ___}": 3,
    "True or false: domain describes the possible values of a function's output.": "false",
    "True or false: sin(30 deg) = cos(60 deg).": "true",
    "If f(x) = sqrt(x) and g(x) = 5x - 6, what is f(g(11))?": "7",
    "True or false: sqrt(x) = x^(1/2).": "true",
    "Evaluate 27^(2/3).": "9",
    "Is pattern 7, 35, 175... arithmetic or geometric?": "geometric",
    "True or false: sqrt(44) can be simplified.": "true",
    "True or false: sec(x) = 1/sin(x), csc(x) = 1/cos(x), and cot(x) = 1/tan(x).": "false",
    "What is the constant term in the simplified expression of sin^2(x)/(cos(x) + 1)?": 1,
    "What is (cos(30 deg))^2 as a fraction?": "3/4",
  },
  { # floor 4 questions (gr 12 math)
    "What is the derivative of x^2?": "2x",
    "True or false: the derivative of cos(x) is sin(x).": "false",
    "What is the derivative of ln(3x^12) evaluated at 4?": 3,
    "What is x if log(cbrt(x + 2)) = 1/3?": 8,
    "True or false: there is no remainder when x^3 - 2x^2 + 1 is divided by x - 1.": "true",
    "Evaluate f''(-1), if f(x) = 8x^5.": -160,
    "What is the slope, in x and y, on any point of equation x^2 + y^2 = 1?": "-x/y",
    "Fill in the blank: when we want to differentiate an equation with no isolated variable (i.e. that is not a function), we use ___ differentiation.": "implicit",
    "What is the derivative of any constant C?": 0,
    "True or false: a function is differentiable over interval [a, b] if it is also continuous over interval [a, b].": "false",
    "What is the 483rd derivative of -sin(x) evaluated at 0?": 1,
    "What is the 7th derivative of e^2x evaluated at 0?": 128,
    "Fill in the blank: if a function's derivative changes signs before and after a point, the point is labeled an ___ on the original graph.": "extremum",
    "Fill in the blank: if a function's second derivative changes signs before and after a point, the point is labeled a ___ on the original graph.": "point of inflection",
    "True or false: the limit of (-1)^x as x approaches positive infinity is 0.": "false",
    "Fill in the blank: the property of an infinite sum equaling a finite value is referred to as ___.": "convergence",
    "What are the sum of the numerators in the partial fraction expansion of 3/(x^2 + 5x + 6)?": 0,
    "True or false: the derivative of tan(x) is -sec^2(x).": "false",
    "Fill in the blank: the derivative of x^2*sin(x) is ___*x^2 + 2x*sin(x)": "cos(x)",
    "Fill in the blank: the derivative of arctan(x) is 1/(___ + x^2).": "1",
  }
]

# stores how every movement direction changes the coordinates of the player
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

# translates internally stored buff stats to messages
statToName = {
  "atk": "extra damage",
  "def": "damage reduction"
}

# put current player info in db. we're using copy.deepcopy() for playerstats and shoppools because those have lists/dictionaries inside them. if we just use .copy() the copies will contain the original lists/dictionaries instead of copies, meaning the saved versions can be modified outside of this method
def save():
  db["save"] = copy.deepcopy(playerStats) 
  db["inv"] = playerInv.copy()
  db["shop"] = copy.deepcopy(shopPools)
  db["itemStates"] = copy.deepcopy(itemStates)

# loads values saved in the db. deepcopy is being used for reason listed for save
def load():
  # global declaration so we can modify the actual variables
  global playerStats
  global playerInv
  global shopPools
  global playerRoom
  playerStats = copy.deepcopy(dict(db["save"])) # take saved player info from db
  playerInv = list(db["inv"]).copy()
  shopPools = copy.deepcopy(list(db["shop"]))
  itemStates = copy.deepcopy(list(db["itemStates"]))
  playerRoom = master[playerStats["floor"]][playerStats["room"]]

# reassign the values within the db to what the values would be on first run
def delete():
  # reshuffles shop items before saving in db
  for i in range(4):
    random.shuffle(itemPools[i])
    shopPools[i] = itemPools[i][:3]
  db["save"] = { 
    "currentChar": "@", 
    "floor": 0, 
    "room": 0,
    "x": 4,
    "y": 6,
    "atk": 0,
    "def": 0,
    "health": 100,
    "money": 0,
    "xp": 0,
    "xpProg": 0, 
    "crit": 15,
    "miss": 10,
    "buffs": {
      "atk": {},
      "def": {}
    },
    "mapStates": [
      [True, False, False, False, False],
      [True, False, False, False, False],
      [True, False, False, False, False, False],
      [True, False, False, False, False, False]
    ]
  }
  db["inv"] = []
  db["shop"] = copy.deepcopy(shopPools)
  db["itemStates"] = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
  # load save file once reinitialized
  load()
  gameInfo() # print gameinfo on new save

# creates a pause menu with options for save file
def saveScreen():
  # declare global so the function can modify these variables
  global run
  global playerRoom
  # stores all possible pointer positions. when the pointer is moved it's current position is set to whitespace while the new position is set to the pointer
  pointer = ["> ", "  ", "  ", "  ", "  "]
  pointerI = 0
  # prints out menu
  print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
  # while loop for getting keypresses
  while True:
    # pressing ctrl c throws a keyboard interrupt error, so we gotta do this try catch every time we get a key
    try:
      e = getkey()
    except KeyboardInterrupt:
      # reprint menu upon keyboard interrupt. the menu is meant to be reprinted if a key that is not listed below is pressed
      print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
    # move pointer up then reprint menu
    if e == keys.UP:
      pointer[pointerI] = "  "
      # we can simply subtract the pointer position like this without checking for < 0 values due to python's negative index support
      pointerI = (pointerI - 1) % 5
      pointer[pointerI] = "> "
      print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
    # move pointer down then reprint menu
    elif e == keys.DOWN:
      pointer[pointerI] = "  "
      pointerI = (pointerI + 1) % 5
      pointer[pointerI] = "> "
      print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
    # if player confirms selection
    elif e == keys.ENTER:
      # go back to game if pointer was on continue
      if pointerI == 0:
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      # run save function if pointer was on save
      elif pointerI == 1:
        print("Saving...")
        save()
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      # run load function if pointer was on load
      elif pointerI == 2:
        print("Loading last save...")
        load()
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      # confirm if user wants to delete save before either running delete function or going back to game
      elif pointerI == 3:
        print("Are you sure? (y/n)\n")
        try:
          e = getkey()
        except KeyboardInterrupt:
          print("Going back...\n")
          print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
          continue
        # will delete if user presses y. .lower() is there for case insensitive checking
        if e.lower() == "y":
          print("Deleting save...")
          delete()
          printRoom(playerRoom)
          return
        else:
          print("Going back...\n")
          print(
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
      # set boolean used for game loop to false to end game
      elif pointerI == 4:
        print("Goodbye!")
        run = False
        return
    # if player simply presses escape on the screen go back to the game
    elif e == keys.ESCAPE:
      print("Back to Math Temple!\n")
      printRoom(playerRoom)
      return

# function for printing player stats. this was originally meant to be run if the player presses s but is now exclusively run when a room is printed
def stats():
  print(f"Level: {playerStats['xp'] + 1}")
  if playerStats["xp"] <= len(xpLevelToProg):
    print(f"XP: {playerStats['xpProg']}/{xpLevelToProg[playerStats['xp']]}")
  print(f"HP: {playerStats['health']}/{levelToHealthMax[playerStats['xp']]}")
  for i in range(math.ceil(playerStats["health"] / (levelToHealthMax[playerStats["xp"]] / 10))):
    print("█", end="")
  print()
  print(f"Money: ${playerStats['money']}")
  if playerStats["atk"] > 0:
    print(f"Extra damage: {playerStats['atk']}")
  if playerStats["def"] > 0:
    print(f"Damage reduction: {playerStats['def']}")
  print()

# print the player's room
def printRoom(room):
  # iterate through the characters stored in the room list to determine what to print
  for y in range(len(room[0])): # column
    for x in range(len(room) - 1): # row
      tile = room[x][y]
      # print the player if on the player's position
      if x == playerStats["x"] and y == playerStats["y"]:
        print(playerStats["currentChar"], end = " ")
      # decoration is stored decrypted, so no need to index the dictionary used to translate characters
      elif tile in {",", ".", "'", '"', "`"}:
        print(tile + " ", end = "")
      # just print translated verison of character
      else:
        print(tileSymbol[tile] + " ", end = "")
    print() # print \n after each row
  print() # print line break after printing room
  # print stats once done
  stats()

def gameInfo():
  print("Welcome to Math Temple!\nThis game is a dungeon-style RPG game about traversing a math-themed dungeon, defeating enemies, eating food, and collecting study notes.\n\nKey:\n- and | represent walls.\n* represents doors.\n$ represents shops where you can buy items.\n^ represents stairways to higher floors.\n? represents...???\nAll other symbols are decoration.\n\nYour goal is to traverse rooms and floors and to defeat all bosses. XP and money gained by defeating enemies will aid your attack, defense, and health along your journey.\n\nControls:\nArrow keys to move\nEnter to select options\ni to open inventory\nm to view map of the current floor\nesc to exit screens or view save menu\n/ to view this screen again\n\nWhen you're ready, hit enter to start!\n")
  while True: # instructions screen loop
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    if e == keys.ENTER or e == keys.ESC:
      return

# print a map of the floor, mapped to the m key
def printMap():
  # iterates through everything stored in the map layout
  for x in range(len(maps[playerStats["floor"]])):
    for y in range(len(maps[playerStats["floor"]][x])):
      # if tile to print is a room
      if maps[playerStats["floor"]][x][y].isnumeric():
        # print player if room is player's current room
        if int(maps[playerStats["floor"]][x][y]) == playerStats["room"]:
          print("@", end="")
        # print B if room is boss room
        elif int(maps[playerStats["floor"]][x][y]) == 4:
          print("B", end="")
        # print # if room is unvisited, or space if visited
        elif playerStats["mapStates"][playerStats["floor"]][int(maps[playerStats["floor"]][x][y])]:
          print(" ", end="")
        else:
          print("#", end="")
      else:
          print(maps[playerStats["floor"]][x][y], end="")
    print()
  print()
  # reprint player's current room once done
  printRoom(playerRoom)

# move player on keypress
def move(direction):
  # global declaration to modify original variables
  global playerRoom
  global playerInv
  # function for handling player reaching special items
  def specialGet():
    special = specialItems[playerStats["floor"]]
    playerInv.append(special)
    print(f"You acquired the {specialItems[playerStats['floor']].title()}!")
    master[playerStats["floor"]][playerStats["room"]][(items[special + "c"])[0]][(items[special + "c"])[1]] = "e" # change tile of special item to e using a lot of coords
  # roll value to see if player should fight enemy when moving
  encounterChance = int((playerStats["health"]/levelToHealthMax[playerStats["xp"]])*7)
  # boolean to check if player should move
  shouldFight = True
  posChar = playerRoom[playerStats["x"] + dirToCoord[direction + "x"]][playerStats["y"] + dirToCoord[direction + "y"]] # temp variable for the position of the character
  if posChar in {"v", "h"}: # if its a wall block them
    printRoom(playerRoom)
    print("You can't move to that tile!\n")
  elif posChar == "s": # if its a shop run shop
    shop1()
  elif posChar == "i": # if player on item run specialget function
    specialGet()
    playerStats["x"] += dirToCoord[direction + "x"]
    playerStats["y"] += dirToCoord[direction + "y"]
    printRoom(playerRoom)
  else: # otherwise move them
    playerStats["x"] += dirToCoord[direction + "x"]
    playerStats["y"] += dirToCoord[direction + "y"]
    encounter = random.randint(1, 100)
    # if player moves on a door
    if playerRoom[playerStats["x"]][playerStats["y"]] == "d":
      # check if player is moving to boss room and if room has not been visited before
      if not playerStats["mapStates"][playerStats["floor"]][4] and playerStats["room"] + playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])] == 4: # first check is simply to see if player visited boss room. if they did, don't fight boss i forgot mapstate is bool im stupid it was supposed to be sq brackets to index yea
        # ask player if they want to fight boss. if not, keep them in the room and reset coordinate changes
        print("You feel uneasy, do you want to proceed? (Boss room ahead, press enter to move forward)\n")
        try:
          e = getkey()
        except KeyboardInterrupt:
          print("Going back...")
          playerStats["x"] -= dirToCoord[direction + "x"]
          playerStats["y"] -= dirToCoord[direction + "y"]
          printRoom(playerRoom)
          return
        if e == keys.ENTER:
          # activate combat function with boss flag
          combat1(boss=True)
          # player will never be saved on top of a door, but will be on one once they are fighting a boss. end the function before changing room if player's save is loaded, meaning they died
          if playerRoom[playerStats["x"]][playerStats["y"]] != "d":
            return
        # if they decide not to fight
        else:
          print("Going back...")
          playerStats["x"] -= dirToCoord[direction + "x"]
          playerStats["y"] -= dirToCoord[direction + "y"]
          printRoom(playerRoom)
          return
      # the dictionary storing doors for each room handles how much to increment the player's room value by. this grabs that value and adds it
      playerStats["room"] += playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])]
      # update the player's current room
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      # dictionary for handling player placement in new room
      dirToRoom = {
        "up": ["y", len(playerRoom[0]) - 2],
        "down": ["y", 1],
        "left": ["x", len(playerRoom) - 3],
        "right": ["x", 1]
      }
      # change player position
      playerStats[dirToRoom[direction][0]] = dirToRoom[direction][1]
      # if they end up on an item grab it
      if master[playerStats["floor"]][playerStats["room"]][playerStats["x"]][playerStats["y"]] == "i":
        specialGet()
      # mark room as visited
      playerStats["mapStates"][playerStats["floor"]][playerStats["room"]] = True
    # if player reaches stairs going up, add 1 to player floor number and reset room number
    elif playerRoom[playerStats["x"]][playerStats["y"]] == "U":
      # set boolean checking if player should fight on this movement to false
      shouldFight = False
      playerStats["floor"] += 1
      playerStats["room"] = 0
      # update room
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      playerStats["x"] -= dirToCoord[direction + "x"] # move them back so they aren't in the wall anymore
      playerStats["y"] -= dirToCoord[direction + "y"]
      # save once the player changes floors, no matter if it was visited or not
      print("Autosaving...")
      save()
      print("Done!")
    # almost identical to what happens when player reaches stairs going up. only difference is room is set to final room of that floor and floor value goes down
    elif playerRoom[playerStats["x"]][playerStats["y"]] == "D":
      # set boolean checking if player should fight on this movement to false
      shouldFight = False
      playerStats["floor"] -= 1
      playerStats["room"] = 4
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      playerStats["x"] -= dirToCoord[direction + "x"] # move them back so they aren't in the wall anymore
      playerStats["y"] -= dirToCoord[direction + "y"]
      print("Autosaving...")
      save()
      print("Done!")

    # value to heal player's hp by every time they move
    regen = int(levelToHealthMax[playerStats["xp"]]/40)
    # check if player's health is below max to see if they should regenerate
    if playerStats["health"] < levelToHealthMax[playerStats["xp"]]:
      # min is used to make sure the player's health will never go above max
      playerStats["health"] = min(levelToHealthMax[playerStats["xp"]], playerStats["health"] + regen)

    # make player fight if rolled value for encounter is in threshold and player is not in final room and if they just changed floors, as in the last case, death becomes irrelevant
    if 1 <= encounter <= encounterChance and playerStats["room"] < 4 and shouldFight:
      playerStats["currentChar"] = "!"
      printRoom(playerRoom)
      combat1()
      playerStats["currentChar"] = "@"
      printRoom(playerRoom)
    else:
      printRoom(playerRoom)

# combat function
def combat1(boss=False):
  # initialize some variables
  exitCombat = False
  death = False
  combatPI1 = 0
  # if the player is fighting a boss guarantee that the enemy will be the boss of that floor
  if boss:
    enemyName1 = enemyPools[playerStats["floor"]][-1]
  else:
    enemyName1 = random.choice(enemyPools[playerStats["floor"]][:3])
  enemy1 = enemies[enemyName1]
  currentEnemyHealth1 = enemy1["health"]
  print(enemy1["initialText"]) # encounter text
  # function for refreshing combat menu
  def combatPointer1Refresh():
    # allow usage of variable used to store combat menu pointer
    nonlocal combatPI1
    # used for aligning healthbars
    spaces = " "*(6 - len(str(playerStats["health"])))
    print(f"HP: {playerStats['health']}/{levelToHealthMax[playerStats['xp']]}{spaces + enemyName1.title()} HP: {currentEnemyHealth1}/{enemy1['health']}") # label player and enemy health
    for i in range(10): # print player health bar
      numberOfBars = math.ceil(playerStats["health"] / (levelToHealthMax[playerStats["xp"]] / 10))
      if i <= numberOfBars:
        print("█", end = "")
      else:
        print(" ", end = "")
    print("    ", end = "") # print space between health bars
    for i in range(10):
      numberOfBars = math.ceil(currentEnemyHealth1 / (enemy1["health"] / 10))
      if i <= numberOfBars:
        print("█", end = "")
      else:
        print(" ", end = "")
    print("\n") # print line break after health bars

    # print actual combat menu with pointers
    print("ATK INV RUN")
    combatPointer1 = [" ", " "]
    combatPointer1.insert(combatPI1, "^")
    print(" " + "   ".join(combatPointer1))

    # print buffed stats if they are above 0
    if playerStats["atk"] > 0:
      print(f"Extra damage: {playerStats['atk']}")
    if playerStats["def"] > 0:
      print(f"Damage reduction: {playerStats['def']}")
    print()

  combatPointer1Refresh() # initial menu

  # function for handling attacks
  def atk1(enemy):
    nonlocal currentEnemyHealth1
    nonlocal exitCombat
    unvariedAtk = math.floor(4**(1 + 0.2*playerStats["xp"])) # base atk
    atkVariation = int((50**(1/17))**playerStats["xp"]) # variation in atk; at lvl 1 it's +-1 and at lvl 18 (max) it's +- 50
    # roll 2 values to see if player should miss or get a critical attack
    miss = random.randint(1, 100)
    crit = random.randint(1, 100)
    # prioritize miss over crit, player does no damage
    if miss <= playerStats["miss"]:
      playerAtkInt1 = 0
      print("You missed!")
    # player does 1.5 times usual damage if crit
    elif crit <= playerStats["crit"]:
      playerAtkInt1 = int(1.5 * (random.randint(unvariedAtk - atkVariation, unvariedAtk + atkVariation) / (enemy["def"] // 2)) + playerStats["atk"])
      print(f"Critical hit! You dealt {playerAtkInt1} damage to the {enemyName1.title()}!")
    # player does normal amount of damage
    else:
      playerAtkInt1 = int(random.randint(unvariedAtk - atkVariation, unvariedAtk + atkVariation) / (enemy["def"] // 2) + playerStats["atk"])
      print(f"You dealt {playerAtkInt1} damage to the {enemyName1.title()}!")
    # subtract enemy health
    currentEnemyHealth1 -= playerAtkInt1
    # handle buffs affecting player damage
    removeQueue = []
    for buff in playerStats["buffs"]["atk"].keys():
      # decrement buff duration by 1
      playerStats["buffs"]["atk"][buff]["duration"] -= 1
      # if buff duration becomes 0, or runs out, subtract from stat and queue it to be removed
      if playerStats["buffs"]["atk"][buff]["duration"] == 0:
        playerStats["atk"] -= playerStats["buffs"]["atk"][buff]["change"]
        print(f"You lost a buff: -{playerStats['buffs']['atk'][buff]['change']} extra damage.")
        removeQueue.append(buff)
    # remove buffs after subtracting from buffed stat to avoid errors
    for i in removeQueue:
      del playerStats["buffs"]["atk"][i]
    # run enemy death function once player kills enemy and exit combat afterwards
    if currentEnemyHealth1 <= 0:
      enemyDeath1()
      exitCombat = True
      return

  # handles enemy attacks
  def enemyAtk1():
    print() # line break for clarity
    # make variables in overarching function modifiable here
    nonlocal enemy1
    nonlocal death
    # roll values for deciding whether or not enemy will miss or crit
    miss = random.randint(1, 100)
    crit = random.randint(1, 100)
    # prioritize miss over crit
    if miss <= enemy1["miss"]:
      print(f"{enemyName1.title()} missed!")
    # deal 1.5 times more damage if crit
    elif crit <= enemy1["crit"]:
      enemyAtkInt1 = max(math.floor(1.5*random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)) - playerStats["def"], 0)
      playerStats["health"] -= enemyAtkInt1
      print(f"Critical! {enemyName1.title()} deals {enemyAtkInt1} damage.")
    # normal damage if values are not low enough
    else:
      enemyAtkInt1 = random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)
      playerStats["health"] -= enemyAtkInt1
      print(f"{enemyName1.title()} deals {enemyAtkInt1} damage.")
    # if player dies, reload save and end combat
    if playerStats["health"] <= 0:
      print("You died! Loading last save...\n")
      load()
      death = True
    # handle damage decreasing buffs
    removeQueue = []
    for buff in playerStats["buffs"]["def"].keys():
      # decrement buff duration by 1
      playerStats["buffs"]["def"][buff]["duration"] -= 1
      # if buff duration runs out due to decrementation lower stat and queue to be removed
      if playerStats["buffs"]["def"][buff]["duration"] == 0:
        playerStats["def"] -= playerStats["buffs"]["def"][buff]["change"]
        print(f"You lost a buff: -{playerStats['buffs']['def'][buff]['change']} damage reduction.")
        removeQueue.append(buff)
    # remove buffs separately to avoid errors
    for i in removeQueue:
      del playerStats["buffs"]["def"][i]

  # handles enemy death
  def enemyDeath1():
    # make variables in overarching function usable here
    nonlocal exitCombat
    nonlocal enemyName1
    # set combat to end
    exitCombat = True
    print(f"You killed the {enemyName1.title()}.")
    xpGainVariation = int((3**(1/3))**playerStats["room"]) # variation in xp drop
    # generate player's gained xp and money
    xpGain1 = random.randint(enemy1["xpYield"] - xpGainVariation, enemy1["xpYield"] + xpGainVariation)
    moneyGain1 = random.randint(enemy1["moneyYield"] - 1, enemy1["moneyYield"] + 1)
    # add gains
    playerStats["xpProg"] += xpGain1
    playerStats["money"] += moneyGain1
    # check if player is at max level before adding xp
    if len(xpLevelToProg) == playerStats["xp"] + 1:
      print("You're at max level!")
    # add if not max level and handle excess xp on levelup
    else: 
      if playerStats["xpProg"] >= xpLevelToProg[playerStats["xp"]]:
        print("You levelled up!")
        if len(xpLevelToProg) >= playerStats["xp"]:
          playerStats["xpProg"] %= xpLevelToProg[playerStats["xp"]]
        playerStats["xp"] += 1
      # print out how much xp was gained if no level up
      else:  
        print(f"You gained {xpGain1} XP and ${moneyGain1}! (Level {playerStats['xp'] + 1}; {playerStats['xpProg']}/{xpLevelToProg[playerStats['xp']]} to next level)\n")
    # if enemy was a boss, drop the study note and add to player inventory
    if boss:
      print(f"{enemyName1.title()} dropped a study note! It says:")
      print(items[studyNotes[playerStats["floor"]] + "c"])
      playerInv.append(studyNotes[playerStats["floor"]])

  # combat loop for keypresses
  global runSuccess
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    # refresh menu on arrow key press
    if e == keys.LEFT:
      combatPI1 = (combatPI1 - 1) % 3
      combatPointer1Refresh()
    elif e == keys.RIGHT:
      combatPI1 = (combatPI1 + 1) % 3
      combatPointer1Refresh()
    # once player presses enter to confirm choice
    elif e == keys.ENTER:
      # attack if choice was atk
      if combatPI1 == 0:
        atk1(enemy1)
        if exitCombat == True: # check for enemy death here
          exitCombat = False
          return
        enemyAtk1()
        if death:
          printRoom(playerRoom)
          return
        print(random.choice(enemy1["encounterTexts"]))
        combatPointer1Refresh()
      # open inventory if choice was inv
      elif combatPI1 == 1:
        inv()
        combatPointer1Refresh()
      # try to run if choice was run
      elif combatPI1 == 2:
        # deny run request if fighting boss
        if boss:
          print("You can't run from a boss battle!\n")
          combatPointer1Refresh()
        # give player problem to answer to decide if they should escape
        else:
          # if correct answer, escape
          run(playerStats["floor"])
          if runSuccess == True:
            print(f"\nYou fled from the {enemyName1.title()}.\n")
            runSuccess = False
            return
          # otherwise give enemy free attack and bring back to menu
          else:
            print("You answered the problem wrong! Try again next turn.")
            enemyAtk1()
            print(random.choice(enemy1["encounterTexts"]))
            combatPointer1Refresh()

# handles inventory
def inv():
  # if player doesn't have items bring them back to what menu they were on previously
  if len(playerInv) == 0:
    print("Your inventory is empty!\n")
    return

  # set up inventory menu pointer
  invPI = 0

  # print inventory menu
  def invRefresh():
    print("Your inventory (esc to exit):")
    for i in range(0, len(playerInv)):
      if i == invPI:
        print(f"{i + 1}: {playerInv[i]} <")
      else:
        print(f"{i + 1}: {playerInv[i]}")
    print()
  
  invRefresh() # initial inv display

  # while loop for keypresses
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    # move pointer on arrow key press
    if e == keys.UP:
      invPI = (invPI - 1) % len(playerInv)
      invRefresh()
    elif e == keys.DOWN:
      invPI = (invPI + 1) % len(playerInv)
      invRefresh()
    # handle selection once player chooses with enter
    elif e == keys.ENTER:
      # get item they want to use
      currentItem = playerInv[invPI]
      # ask if they want to use the item
      print(items[currentItem] + "\n")
      print("Would you like to use this item? Press enter again to confirm.\n")
      # prompt for keypress
      try:
        confirm = getkey()
      except KeyboardInterrupt:
        invRefresh()
      # enter will confirm usage
      if confirm == keys.ENTER:
        # heal player if item was for healing, then delete from inventory
        if items[currentItem + "s"] == "health":
          playerStats["health"] += items[currentItem + "b"]
          print(f"{items[currentItem + 'b']} HP was restored. You now have {playerStats['health']} HP.\n")
          del playerInv[invPI]
        # print contents of study note if item was a note
        elif items[currentItem + "s"] == "unusable":
          print(items[currentItem + "c"] + "\n")
        # add damage increase or decrease buff to player stats, then delete from inventory
        else:
          playerStats["buffs"][items[currentItem + "s"]][currentItem] = {"change": items[currentItem + "b"], "duration": items[currentItem + "t"]}
          playerStats[items[currentItem + "s"]] += items[currentItem + "b"]
          print(f"New buff: +{items[currentItem + 'b']} {statToName[items[currentItem + 's']]} for {items[currentItem + 't']} turns.\n")
          del playerInv[invPI]
        return
      else:
        # refresh menu if player did not want to use item
        invRefresh()
    # close menu once player presses escape
    elif e == keys.ESCAPE:
      return

# handles running
def run(floor):
  # allow usage of global boolean for checking if player escapes successfully
  global runSuccess
  # get problem to
  mathProblem = random.choice(list(floorMath[floor].keys()))
  mathSolution = str(floorMath[floor][mathProblem])
  print(f"In order to run you must solve the following problem:\n{mathProblem}")
  mathSolInput = input("Enter: ").lower()
  if mathSolInput == mathSolution:
    runSuccess = True
    return
  else:
    return

# shop function
def shop1():
  print("Welcome to the shop! Use arrow keys and enter to select your items below. Press esc to exit.\n")
  # get list of items being sold on this floor
  itemList1 = shopPools[playerStats["floor"]]
  # initialize pointer position
  shopPI1 = 0
  # list for storing what to print depending on if item is bought or not. will be indexed with itemstate value
  itemChar1 = ["# ", "x "]
  # function for refreshing menu
  def shopPointer1Refresh():
    # allow usage of pointer position variable
    nonlocal shopPI1
    # make string for pointer
    itemPointer1 = [" ", " "]
    itemPointer1.insert(shopPI1, "^")
    itemDisplay1 = ""
    # print out items
    for i in range(3):
      itemDisplay1 += itemChar1[itemStates[playerStats["floor"]][i]]
    # print out menu along with player balance
    print(itemDisplay1)
    print(" ".join(itemPointer1))
    print(f"Money: ${playerStats['money']}\n")
  # called when player chooses item
  def itemDesc1(itemName):
    # print description
    print(f"Item: {itemName.title()}\nDescription: {items[itemName]}\nCost: {items[itemName + 'c']}\n\nDo you wish to buy this item? (Press enter again to buy the item. Press esc to go back.)\n")
    # get key to decide whether or not to give item
    while True:
      try:
        e = getkey()
      except KeyboardInterrupt:
        continue
      # confirm selection with enter
      if e == keys.ENTER:
        # check if they have enough money
        if items[itemName + "c"] > playerStats["money"]:
          print("You can't afford that!")
        # give item if they do, subtract cost from balance
        else:
          playerInv.append(itemName)
          print(f"You have bought the {itemName.title()}!\n")
          itemStates[playerStats["floor"]][shopPI1] += 1
          playerStats["money"] -= items[itemName + "c"]
        # refresh shop menu
        shopPointer1Refresh()
        return
      elif e == keys.ESCAPE:
        # refresh shop if they don't want to buy
        shopPointer1Refresh()
        return
  # initial menu
  shopPointer1Refresh()
  # get keys
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    # move and refresh menu on arrow key press
    if e == keys.LEFT:
      shopPI1 = (shopPI1 - 1) % 3
      shopPointer1Refresh()
    elif e == keys.RIGHT:
      shopPI1 = (shopPI1 + 1) % 3
      shopPointer1Refresh()
    # call itemdesc if item they want to buy is not bought
    elif e == keys.ENTER:
      if itemState1[shopPI1] == 0:
        itemDesc1(itemList1[shopPI1])
      # don't if already bought
      else:
        print("You have already bought that item!\n")
        shopPointer1Refresh()
    # leave shop on escape press
    elif e == keys.ESCAPE:
      print("Come back soon!\n")
      printRoom(playerRoom)
      return

if "save" not in db.keys(): # initializes a save file if a save wasn't found
  delete()

# load player save, will exist no matter what due to check earlier
load()

printRoom(playerRoom) # starting room print

while run: # game loop
  try:
    e = getkey()
  except KeyboardInterrupt:
    continue
  # move player on arrow key press
  if e == keys.UP:
    move("up")
  elif e == keys.DOWN:
    move("down")
  elif e == keys.LEFT:
    move("left")
  elif e == keys.RIGHT:
    move("right")
  # print map on m press
  elif e.lower() == "m":
    printMap()
  # open inventory on i press
  elif e.lower() == "i":
    inv()
    printRoom(playerRoom)
  # reprint game instructions on / press
  elif e == keys.SLASH:
    gameInfo()
    printRoom(playerRoom)
  # open save screen on esc press
  elif e == keys.ESCAPE:
    saveScreen()

"""
Sources:
https://replit.com/talk/learn/GetKeys-tutorial-Python/128030
"""
