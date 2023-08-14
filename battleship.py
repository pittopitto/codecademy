class Battleship:

    def __init__(self, name, length): #, direction = 0):
        # direction = 0 -> Horizontal
        # direction = 1 -> Vertical
        self.name = name
        self.length = length
        #self.direction = direction
        self.ship = [1] * self.length

    def __repr__(self):
        text = 'The ' + self.name + ' is ' + str(self.length) + ' cells long.'
        #text += " ".join(str(item) for item in self.ship)+'\n'
        return text

class BattleGrid:

    def __init__(self):
        self.battlegrid = {
            'A': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'B': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'C': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'D': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'E': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'F': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'H': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'J': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }
    
    def __repr__(self):
        grid = '  1 2 3 4 5 6 7 8 9 10\n' 
        #print("  1 2 3 4 5 6 7 8 9 10")
        for key, values in self.battlegrid.items():
            grid += key+' '+' '.join(str(item) for item in values)+'\n'
        return grid

    def allocate_ship(self, letter, number):
        
        if self.battlegrid[letter][number] == 1:
            print("There's another ship here!")
        self.battlegrid[letter][number] = 1
        
# Functions outside classes go here

def assign_ship(grid, ships):
    for ship in ships:
        print("Where would you like to place the " + ship.name + " of length "+ str(ship.length) + "?")
        letter = input("Please enter a letter between A and J\n").upper()
        number = int(input("Please enter a number between 0 and 9\n"))
        direction = input("Please type 0 for horizontal, or 1 for vertical\n")
        
        if direction == 0:
            for i in ship.length:
                grid.allocate_ship(letter, i)
        elif direction == 1:
            for i in ship.length:
                grid.allocate_ship(chr(ord(letter)+i), number) #ord converts letter into ASCII, and chr converts ASCII into letter
        else:
            print("Error!")

        print(grid)
    print("All ships have been allocated to the grid!")
    return grid

#Set up the game

grid = [BattleGrid(), BattleGrid()]

battleships = [
    Battleship('Carrier', 5),
    Battleship('Battleship', 4),
    Battleship('Cruiser', 3),
    Battleship('Submarine', 3),
    Battleship('Destroyer', 2)
]

# Begin the game

print("\n\n=======================================")
print("=== Welcome to the Battleship Game! ===")
print("=======================================\n\n")

print("Each player has 5 ships.\n")
for battleship in battleships:
    print(battleship)

print("\nOne player needs to leave the room, so the other player can allocate the ships.\n")

for i in grid:
    print("Player " + str(grid.index(i) + 1) + ", please assign your ships to the grid!\n")
    print(i)
    newgrid = assign_ship(i, battleships)