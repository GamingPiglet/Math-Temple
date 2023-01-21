import random, math, copy # import some builtin modules for operations

from replit import db # import replit module so we can use db for saving
from getkey import getkey, keys # import getkey package so we can use keypresses, keys is for handling keys like enter or tab

run = True # keep game running

vwall = ["c", "v", "v", "v", "v", "v", "v", "c"] # vertical wall

room10 = [vwall, ["h", "s", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], vwall, {tuple([5, 0]): 1}]

room11 = [vwall, ["h", "e", "h", "e", "e", "e", "e", "h"], ["d", "e", "h", "e", "e", "e", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "h", "e", "e", "h", "e", "d"], ["h", "e", "h", "e", "e", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "e", "e", "h", "e", "h"], vwall, {tuple([5, 7]): -1, tuple([2, 0]): 1}]

room12 = [["c", "v", "v", "d", "v", "v", "v", "c"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "d"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["h", "v", "e", "e", "e", "h", "e", "h"], ["h", "e", "e", "h", "e", "e", "e", "h"], ["c", "v", "d", "v", "v", "v", "v", "c"], {tuple([2, 7]): -1, tuple([0, 3]): 1, tuple([9, 2]): 2}]

room13 = [vwall, ["h", "e", "e", "e", "e", "h", "e", "h"], ["h", "h", "e", "h", "e", "e", "e", "h"], ["h", "h", "e", "h", "v", "v", "e", "h"], ["h", "i", "e", "e", "h", "e", "e", "h"], ["h", "v", "v", "v", "h", "e", "v", "h"], ["h", "e", "e", "e", "h", "e", "e", "h"], ["h", "e", "v", "v", "v", "v", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "d", "v", "v", "v", "c"], {tuple([9, 3]): -1}]

room14 = [["c", "v", "d", "v", "v", "v", "v", "c"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "U", "v", "v", "v", "c"], {tuple([0, 2]): -2}]

room20 = [vwall, ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["d", "e", "e", "e", "e", "e", "e", "h"], ["h", "e", "e", "e", "e", "e", "e", "h"], ["c", "v", "v", "D", "v", "v", "v", "c"], {tuple([7, 0]): 1}]

map = [["+", "-", " ", "-", " " "-", "+"], ["|", "3", " ", "2", " ", "4", "|"], ["+", "-", "+", " ", "+", "-", "+"], [" ", " ", "|", "1", "|", " ", " "], [" ", " ", "|", "0", "|", " ", " "], [" ", " ", " ", "-", " ", " ", " "]]

floor1 = [room10, room11, room12, room13, room14]
floor2 = [room20]
floor3 = []
floor4 = []

master = [floor1, floor2, floor3, floor4]

deco = [",", ".", "'", '"', "`"] # decoration list to be picked from

for floor in master: # dw this is O(1)
  for room in floor:
    for column in room:
      for letter in column:
        if letter == "e":
          column[column.index(letter)] = random.choice([random.choice(deco), "e", "e", "e", "e", "e", "e", "e", "e", "e"]) # empty space can be a random decoration (1/10 chance)

playerStats = { # dict to store player stats
  "currentChar": "@", # player char changes to ! once combat begins, so we store the player's current character so we can just index a value once we have to print the player
  "floor": 0, # player position values, x and y are based on 0, 0 in the room being the top left corner
  "room": 0,
  "x": 4,
  "y": 6,
  "atk": 0, # unlike enemies, player atk and def are flat damage increases and decreases respectively
  "def": 0,
  "health": 100, # self-explanatory
  "money": 0,
  "xp": 12, # as a level
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
    [True, False, False, False, False],
    [True, False, False, False, False]
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
  "golden three": "The Golden Three! Increases your attack by a whopping 33 for 2 turns.",
  "golden threec": (4, 1),
  "golden threes": "atk",
  "golden threet": 2,
  "golden threeb": 33,
  "study note 1": "Dropped by the addition ninja. Seems to be grade 9 material.",
  "study note 1c": "put note here",
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
  "study note 2": "Dropped by the subtraction paladin. Seems to be grade 10 material.",
  "study note 2c": "put note here",
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
  "study note 3": "Dropped by the multiplication mage. Seems to be grade 11 material.",
  "study note 3c": "put note here",
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
  "study note 4": "Dropped by the division gunner. Seems to be grade 12 material.",
  "study note 4c": "put note here",
  "study note 4s": "unusable"
}

# lists that store item names per floor, and then another list that stores them in order so we can index the right pool by the player's current floor
itemNames1 = ["bread", "chocolate stick", "extra sharp stick", "crumb", "dusty textbook"]

itemNames2 = ["apple core", "empty crate", "instant boba", "protein bar", "breakfast burger"]

itemNames3 = ["bubble tea", "compass", "notebook", "french fries", "whole pizza"]

itemNames4 = ["scissors", "backpack", "brown sugar boba", "chicken burger combo", "lunch wrap"]

studyNotes = ["study note 1", "study note 2", "study note 3", "study note 4"]

itemPools = [itemNames1, itemNames2, itemNames3, itemNames4]

specialItems = ["golden three"]

# stores which items the shop on each floor sells 
shopPools = [[], [], [], []]

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

# when adding bosses, make sure you put the boss name last for easy grabbing
enemyNames1 = ["bogey", "rotten apple", "dark cloud", "addition ninja"]

enemyNames2 = ["angry student", "apple muncher", "quadratic enthusiast", "subtraction paladin"]

enemyNames3 = ["wave clacker", "trigbot", "enlightened bogey", "multiplication mage"]

enemyNames4 = ["deriving samurai", "l'hôpital boxer", "integrating pyromaniac", "division gunner"]

enemyPools = [enemyNames1, enemyNames2, enemyNames3, enemyNames4]

tileSymbol = {
  "c": "+",
  "v": "|",
  "h": "—",
  "e": " ",
  "p": "@", 
  "d": "*",
  "s": "$",
  "i": "?",
  "U": "s",
  "D": "s"
}

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
  "up": [6, "y"],
  "down": [1, "y"],
  "left": [8, "x"],
  "right": [1, "x"]
}

statToName = {
  "atk": "extra damage",
  "def": "damage reduction"
}

for i in range(4):
  random.shuffle(itemPools[i])
  shopPools[i] = itemPools[i][:3]

def save():
  db["save"] = copy.deepcopy(playerStats) # put current player info in db. we're using deepcopy to avoid lists/dictionaries within these being modified outside of this method
  db["inv"] = playerInv.copy()
  db["shop"] = copy.deepcopy(shopPools)

def load():
  global playerStats
  global playerInv
  global shopPools
  global playerRoom
  playerStats = copy.deepcopy(dict(db["save"])) # take saved player info from db
  playerInv = list(db["inv"]).copy()
  shopPools = copy.deepcopy(list(db["shop"]))
  playerRoom = master[playerStats["floor"]][playerStats["room"]]

def delete():
  db.clear()
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
    "xp": 12,
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
      [True, False, False, False, False],
      [True, False, False, False, False]
    ]
  }
  db["inv"] = []
  db["shop"] = copy.deepcopy(shopPools)
  load()

def saveScreen():
  global run
  global playerRoom
  pointer = ["> ", "  ", "  ", "  ", "  "]
  pointerI = 0
  print("What would you like to do?\n" +
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    if e == keys.UP:
      pointer[pointerI] = "  "
      pointerI = (pointerI - 1) % 5
      pointer[pointerI] = "> "
      print(f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
    elif e == keys.DOWN:
      pointer[pointerI] = "  "
      pointerI = (pointerI + 1) % 5
      pointer[pointerI] = "> "
      print(
        f"{pointer[0]}Continue\n" +
        f"{pointer[1]}Save game\n" +
        f"{pointer[2]}Load save\n" +
        f"{pointer[3]}Delete save\n" +
        f"{pointer[4]}Quit\n")
    elif e == keys.ENTER:
      if pointerI == 0:
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      elif pointerI == 1:
        print("Saving...")
        save()
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      elif pointerI == 2:
        print("Loading last save...")
        load()
        print("Back to Math Temple!\n")
        printRoom(playerRoom)
        return
      elif pointerI == 3:
        print("Are you sure? (y/n)")
        try:
          e = getkey()
        except KeyboardInterrupt:
          continue
        if e.lower() == "y":
          print("Deleting save...")
          delete()
          print("Back to Math Temple!\n")
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
      elif pointerI == 4:
        print("Goodbye!")
        run = False
        return
    elif e == keys.ESCAPE:
      print("Back to Math Temple!\n")
      printRoom(playerRoom)
      return

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
  stats()

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

def move(direction):
  global playerRoom
  global playerInv
  encounterChance = int((playerStats["health"]/levelToHealthMax[playerStats["xp"]])*7)
  posChar = playerRoom[playerStats["x"] + dirToCoord[direction + "x"]][playerStats["y"] + dirToCoord[direction + "y"]] # temp variable for the position of the character
  if posChar in {"v", "h"}: # if its a wall block them
    printRoom(playerRoom)
    print("You can't move to that tile!")
  elif posChar == "s": # if its a shop run shop
    shop1()
  elif posChar == "i":
    special = specialItems[playerStats["floor"]]
    playerInv.append(special)
    print(f"You acquired the {specialItems[playerStats['floor']].title()}!")
    master[playerStats["floor"]][playerStats["room"]][(items[special + "c"])[0]][(items[special + "c"])[1]] = "e" # change tile of special item to e using a lot of coords
    playerStats["x"] += dirToCoord[direction + "x"]
    playerStats["y"] += dirToCoord[direction + "y"]
    printRoom(playerRoom)
  else: # otherwise move them
    playerStats["x"] += dirToCoord[direction + "x"]
    playerStats["y"] += dirToCoord[direction + "y"]
    encounter = random.randint(1, 100)
    if playerRoom[playerStats["x"]][playerStats["y"]] == "d":
      if not playerStats["mapStates"][playerStats["floor"]][4] and playerStats["room"] + playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])] == 4: # first check is simply to see if player visited boss room. if they did, don't fight boss i forgot mapstate is bool im stupid it was supposed to be sq brackets to index yea
        print("You feel uneasy, do you want to proceed? (Boss room ahead, press enter to move forward)\n")
        try: # pressing ctrl c throws a keyboard interrupt error, so we gotta do this try catch every time we get a key
          e = getkey()
        except KeyboardInterrupt:
          print("Going back...")
          playerStats["x"] -= dirToCoord[direction + "x"]
          playerStats["y"] -= dirToCoord[direction + "y"]
          printRoom(playerRoom)
          return
        if e == keys.ENTER:
          combat1(boss = True)
          if playerRoom[playerStats["x"]][playerStats["y"]] != "d":
            return
        else:
          print("Going back...")
          playerStats["x"] -= dirToCoord[direction + "x"]
          playerStats["y"] -= dirToCoord[direction + "y"]
          printRoom(playerRoom)
          return
      playerStats["room"] += playerRoom[-1][tuple([playerStats["x"], playerStats["y"]])]
      playerStats[dirToRoom[direction][1]] = dirToRoom[direction][0]
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      playerStats["mapStates"][playerStats["floor"]][playerStats["room"]] = True
    elif playerRoom[playerStats["x"]][playerStats["y"]] == "U":
      playerStats["floor"] += 1
      playerStats["room"] = 0
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      playerStats["x"] -= dirToCoord[direction + "x"] # move them back so they aren't in the wall anymore
      playerStats["y"] -= dirToCoord[direction + "y"]
      print("Autosaving...")
      save()
      print("Done!")
    elif playerRoom[playerStats["x"]][playerStats["y"]] == "D":
      playerStats["floor"] -= 1
      playerStats["room"] = 4
      playerRoom = master[playerStats["floor"]][playerStats["room"]]
      playerStats["x"] -= dirToCoord[direction + "x"] # move them back so they aren't in the wall anymore
      playerStats["y"] -= dirToCoord[direction + "y"]
      print("Autosaving...")
      save()
      print("Done!")
    if playerStats["health"] < levelToHealthMax[playerStats["xp"]]:
      playerStats["health"] = min(levelToHealthMax[playerStats["xp"]], playerStats["health"] + 2)

    if 1 <= encounter <= encounterChance and playerStats["room"] < 4:
      playerStats["currentChar"] = "!"
      printRoom(playerRoom)
      combat1()
      playerStats["currentChar"] = "@"
      printRoom(playerRoom)
    else:
      printRoom(playerRoom)

runSuccess = False

def combat1(boss=False):
  exitCombat = False
  death = False
  combatPI1 = 0
  if boss:
    enemyName1 = enemyPools[playerStats["floor"]][-1]
  else:
    enemyName1 = random.choice(enemyPools[playerStats["floor"]][:3])
  enemy1 = enemies[enemyName1]
  currentEnemyHealth1 = enemy1["health"]
  print(enemy1["initialText"]) # encounter text
  def combatPointer1Refresh():
    nonlocal combatPI1
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
    
    print("ATK INV RUN")
    combatPointer1 = [" ", " "]
    combatPointer1.insert(combatPI1, "^")
    print(" " + "   ".join(combatPointer1))
    
    if playerStats["atk"] > 0:
      print(f"Extra damage: {playerStats['atk']}")
    if playerStats["def"] > 0:
      print(f"Damage reduction: {playerStats['def']}")
    print()

  combatPointer1Refresh() # initial menu
  
  def atk1(enemy):
    nonlocal currentEnemyHealth1
    nonlocal exitCombat
    unvariedAtk = math.floor(4**(1 + 0.2*playerStats["xp"])) # base atk
    atkVariation = int((50**(1/17))**playerStats["xp"]) # variation in atk; at lvl 1 it's +-1 and at lvl 18 (max) it's +- 50
    miss = random.randint(1, 100)
    crit = random.randint(1, 100)
    if miss <= playerStats["miss"]:
      playerAtkInt1 = 0
      print("You missed!")
    elif crit <= playerStats["crit"]:
      playerAtkInt1 = int(1.5 * (random.randint(unvariedAtk - atkVariation, unvariedAtk + atkVariation) / (enemy["def"] // 2)) + playerStats["atk"])
      print(f"Critical hit! You dealt {playerAtkInt1} damage to the {enemyName1.title()}!")
    else:
      playerAtkInt1 = int(random.randint(unvariedAtk - atkVariation, unvariedAtk + atkVariation) / (enemy["def"] // 2) + playerStats["atk"])
      print(f"You dealt {playerAtkInt1} damage to the {enemyName1.title()}!")
    currentEnemyHealth1 -= playerAtkInt1
    removeQueue = []
    for buff in playerStats["buffs"]["atk"].keys():
      playerStats["buffs"]["atk"][buff]["duration"] -= 1
      if playerStats["buffs"]["atk"][buff]["duration"] == 0:
        playerStats["atk"] -= playerStats["buffs"]["atk"][buff]["change"]
        print(f"You lost a buff: -{playerStats['buffs']['atk'][buff]['change']} extra damage.")
        removeQueue.append(buff)
    for i in removeQueue:
      del playerStats["buffs"]["atk"][i]
    if currentEnemyHealth1 <= 0:
      enemyDeath1()
      exitCombat = True
      return
  
  def enemyAtk1():
    print() # line break for clarity
    nonlocal enemy1
    nonlocal death
    miss = random.randint(1, 100)
    crit = random.randint(1, 100)
    if miss <= enemy1["miss"]:
      print(f"{enemyName1.title()} missed!")
    elif crit <= enemy1["crit"]:
      enemyAtkInt1 = max(math.floor(1.5*random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)) - playerStats["def"], 0)
      playerStats["health"] -= enemyAtkInt1
      print(f"Critical! {enemyName1.title()} deals {enemyAtkInt1} damage.")
    else:
      enemyAtkInt1 = random.randint(enemy1["atk"] - 1, enemy1["atk"] + 1)
      playerStats["health"] -= enemyAtkInt1
      print(f"{enemyName1.title()} deals {enemyAtkInt1} damage.")
    if playerStats["health"] <= 0:
      print("You died! Loading last save...\n")
      load()
      death = True
    removeQueue = []
    for buff in playerStats["buffs"]["def"].keys():
      playerStats["buffs"]["def"][buff]["duration"] -= 1
      if playerStats["buffs"]["def"][buff]["duration"] == 0:
        playerStats["def"] -= playerStats["buffs"]["def"][buff]["change"]
        print(f"You lost a buff: -{playerStats['buffs']['def'][buff]['change']} damage reduction.")
        removeQueue.append(buff)
    for i in removeQueue:
      del playerStats["buffs"]["def"][i]

  def enemyDeath1():
    nonlocal exitCombat
    exitCombat = True
    print(f"You killed the {enemyName1}.")
    xpGainVariation = int((3**(1/3))**playerStats["room"]) # variation in xp drop
    xpGain1 = random.randint(enemy1["xpYield"] - xpGainVariation, enemy1["xpYield"] + xpGainVariation)
    moneyGain1 = random.randint(enemy1["moneyYield"] - 1, enemy1["moneyYield"] + 1)
    playerStats["xpProg"] += xpGain1
    playerStats["money"] += moneyGain1
    if len(xpLevelToProg) == playerStats["xp"] + 1:
      print("You're at max level!")
    else: 
      if playerStats["xpProg"] >= xpLevelToProg[playerStats["xp"]]:
        print("You levelled up!")
        if len(xpLevelToProg) >= playerStats["xp"]:
          playerStats["xpProg"] %= xpLevelToProg[playerStats["xp"]]
        playerStats["xp"] += 1
      else:  
        print(f"You gained {xpGain1} XP and ${moneyGain1}! (Level {playerStats['xp'] + 1}; {playerStats['xpProg']}/{xpLevelToProg[playerStats['xp']]} to next level)\n")
    if enemy1 == enemyPools[playerStats["floor"]][-1]:
      print(f"{enemy1} dropped a study note! It says:")
      print(items[studyNotes[playerStats["floor"]] + "c"])
      playerInv.append(studyNotes[playerStats["floor"]])

  global runSuccess
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    if e == keys.LEFT:
      combatPI1 = (combatPI1 - 1) % 3
      combatPointer1Refresh()
    elif e == keys.RIGHT:
      combatPI1 = (combatPI1 + 1) % 3
      combatPointer1Refresh()
    elif e == keys.ENTER:
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
      elif combatPI1 == 1:
        inv()
        combatPointer1Refresh()
      elif combatPI1 == 2:
        if boss:
          print("You can't run from a boss battle!\n")
          combatPointer1Refresh()
        else:
          run(playerStats["floor"])
          if runSuccess == True:
            print(f"\nYou fled from the {enemyName1.title()}.\n")
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
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    if e == keys.UP:
      (invPI - 1) % 3
    elif e == keys.DOWN:
      (invPI + 1) % 3
    elif e == keys.ENTER:
      currentItem = playerInv[invPI]
      print()
      print(items[currentItem] + "\n")
      print("Would you like to use this item? Press enter again to confirm.\n")
      try:
        confirm = getkey()
      except KeyboardInterrupt:
        invRefresh()
      if confirm == keys.ENTER:
        if items[currentItem + "s"] == "health":
          playerStats["health"] += items[currentItem + "b"]
          print(f"{items[currentItem + 'b']} HP was restored. You now have {playerStats['health']} HP.\n")
          del playerInv[invPI]
        elif items[currentItem + "s"] == "unusable":
          print(items[currentItem + "c"] + "\n")
        else:
          playerStats["buffs"][items[currentItem + "s"]][currentItem] = {"change": items[currentItem + "b"], "duration": items[currentItem + "t"]}
          playerStats[items[currentItem + "s"]] += items[currentItem + "b"]
          print(f"New buff: +{items[currentItem + 'b']} {statToName[items[currentItem + 's']]} for {items[currentItem + 't']} turns.\n")
          del playerInv[invPI]
        return
      else:
        invRefresh()
    elif e == keys.ESCAPE:
      return

def run(floor):
  global runSuccess
  mathProblem = random.choice(list(floorMath[floor].keys()))
  mathSolution = str(floorMath[floor][mathProblem])
  print(f"In order to run you must solve the following problem:\n{mathProblem}")
  mathSolInput = input("Enter: ").lower()
  if mathSolInput == mathSolution:
    runSuccess = True
    return
  else:
    return
    
# also add healthbar and inv in both this and standard menu when moving around

itemState1 = [0, 0, 0] # so it doesn't get redefined in the shop1() function every time

def shop1():
  print("Welcome to the shop! Use arrow keys and enter to select your items below. Press esc to exit.\n")
  global itemState1  
  itemList1 = shopPools[playerStats["floor"]]
  shopPI1 = 0
  itemChar1 = ["# ", "x "]
  def shopPointer1Refresh():
    nonlocal shopPI1
    itemPointer1 = [" ", " "]
    itemPointer1.insert(shopPI1, "^")
    itemDisplay1 = ""
    for i in range(3):
      itemDisplay1 += itemChar1[itemState1[i]]
    print(itemDisplay1)
    print(" ".join(itemPointer1))
    print(f"Money: ${playerStats['money']}\n")
  def itemDesc1(itemName):
    print(f"Item: {itemName.title()}\nDescription: {items[itemName]}\nCost: {items[itemName + 'c']}\n\nDo you wish to buy this item? (Press enter again to buy the item. Press esc to go back.)\n")
    while True:
      try:
        e = getkey()
      except KeyboardInterrupt:
        continue
      if e == keys.ENTER:
        if items[itemName + "c"] > playerStats["money"]:
          print("You can't afford that!")
        else:
          playerInv.append(itemName)
          print(f"You have bought the {itemName.title()}!\n")
          itemState1[shopPI1] += 1
          playerStats["money"] -= items[itemName + "c"]
        shopPointer1Refresh()
        return
      elif e == keys.ESCAPE:
        shopPointer1Refresh()
        return
  shopPointer1Refresh()
  while True:
    try:
      e = getkey()
    except KeyboardInterrupt:
      continue
    if e == keys.LEFT:
      shopPI1 = (shopPI1 - 1) % 3
      shopPointer1Refresh()
    elif e == keys.RIGHT:
      shopPI1 = (shopPI1 + 1) % 3
      shopPointer1Refresh()
    elif e == keys.ENTER:
      if itemState1[shopPI1] == 0:
        itemDesc1(itemList1[shopPI1])
      else:
        print("You have already bought that item!\n")
        shopPointer1Refresh()
    elif e == keys.ESCAPE:
      print("Come back soon!\n")
      printRoom(playerRoom)
      return

if "save" not in db.keys(): # initializes a save file if a save wasn't found
  # just in case some value changes during the save process, we're hardcoding the fields with starting stats
  delete()

load()
printRoom(playerRoom) # starting room print
# indexes player's floor and room and prints it

while run: # game loop
  # if player xp is sufficient run levelup
  try:
    e = getkey()
  except KeyboardInterrupt:
    continue
  if e == keys.UP:
    move("up")
  elif e == keys.DOWN:
    move("down")
  elif e == keys.LEFT:
    move("left")
  elif e == keys.RIGHT:
    move("right")
  elif e.lower() == "m":
    printMap()
  elif e.lower() == "i":
    inv()
    printRoom(playerRoom)
  elif e == keys.ESCAPE:
    saveScreen()

"""
Sources:
https://replit.com/talk/learn/GetKeys-tutorial-Python/128030
"""
