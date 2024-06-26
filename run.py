import random
# Import random package to be able to create random integers


'''
############################### Game_Board class ##############################
'''


class Game_Board:
    '''
    Game Board initialization and other related Functions:
        - place_ship   -->>   Place a ship on the Game_Board
        - display      -->>   Display the Game_Board
        - check_hit    -->>   Check if there's a hit at the given coordinates
        - mark_hit     -->>   Mark a hit at the given coordinates
        - mark_miss    -->>   Mark a miss at the given coordinates
        - is_ship_sunk -->>   Check if a ship is sunk
    '''
    def __init__(self, game_size):
        # Initialize the Game_Board with a given game_size
        self.game_size = game_size
        # Create a 2D grid representing the Game_Board filled with 'O's
        self.grid = [['O' for _ in range(game_size)] for _ in range(game_size)]
        # List to store the ships' positions
        self.ships = []

    def place_ship(self, ship):
        x, y, game_size, orientation = ship
        if orientation == 'h':
            # If the orientation is horizontal, place the ship horizontally
            for i in range(game_size):
                self.grid[y][x + i] = 'X'
        else:
            # If the orientation is vertical, place the ship vertically
            for i in range(game_size):
                self.grid[y + i][x] = 'X'

        # Add the ship's position to the list of ships
        self.ships.append(ship)

    def display(self, hide_ships=False):
        print("  " + " ".join(str(i) for i in range(self.game_size)))
        for i in range(self.game_size):
            row = " ".join(self.grid[i][j] if not hide_ships or
                           self.grid[i][j] == 'O' else 'S'
                           for j in range(self.game_size))
            print(f"{i} {row}")

    '''
    method display_fleet_status aims to display
    the remaining ships for both the player and the opponent.
    '''
    def display_fleet_status(self):
        print("\nPlayer's Fleet:")
        print("Remaining Ships: ", len(self.ships))
        print("\nEnemy's Fleet:")
        print("Remaining Ships: ", len(self.ships))

    def check_hit(self, x, y):
        return self.grid[y][x] == 'X'

    def mark_hit(self, x, y):
        self.grid[y][x] = 'H'

    def mark_miss(self, x, y):
        self.grid[y][x] = 'M'

    def is_ship_sunk(self, ship):
        x, y, game_size, orientation = ship
        if orientation == 'h':
            for i in range(game_size):
                if self.grid[y][x + i] != 'H':
                    return False
        else:
            for i in range(game_size):
                if self.grid[y + i][x] != 'H':
                    return False
        return True


'''
############################ Battleship_Game class ##########################
'''


class Battleship_Game:
    '''
    Battleship Game initialization and other related Functions:
    - __init__             -->>   Initialize the game
    - generate_enemy_ships -->>   Generate enemy ships with random positions
    - play_game            -->>   Start the game loop
    - enemy_turn           -->>   Enemy's turn to attack
    - get_user_input       -->>   Get user input for coordinates

    '''
    def __init__(self, game_size):
        self.game_size = game_size
        # Create the player's and enemy's boards
        self.Game_Board = Game_Board(game_size)
        self.enemy_board = Game_Board(game_size)

        # List to store the enemy's ships' positions
        self.enemy_ships = []

        # Generate enemy ships
        self.generate_enemy_ships()

    def generate_enemy_ships(self):
        ship_sizes = [2]
        for game_size in ship_sizes:
            # Randomly choose horizontal or vertical orientation
            orientation = random.choice(['h', 'v'])
            if orientation == 'h':
                # If horizontal, generate random x and y
                # within the Game_Board game_size
                x = random.randint(0, self.game_size - game_size)
                y = random.randint(0, self.game_size - 1)
            else:
                # If vertical, generate random x and y
                # within the Game_Board game_size
                x = random.randint(0, self.game_size - 1)
                y = random.randint(0, self.game_size - game_size)
            # Create a ship with its position and orientation
            # Place the ship on the enemy's Game_Board
            # Add the ship to the list of enemy ships
            ship = (x, y, game_size, orientation)
            self.enemy_board.place_ship(ship)
            self.enemy_ships.append(ship)

    def play_game(self):
        while True:
            # Display the player's Game_Board
            # Display the enemy's Game_Board with hidden ships
            print("\nYour Game_Board:")
            self.Game_Board.display()
            print("\nEnemy Game_Board:")
            self.enemy_board.display(hide_ships=True)

            # Display fleet status
            self.Game_Board.display_fleet_status()
            self.enemy_board.display_fleet_status()

            # Get the user's input for coordinates to attack
            x, y = self.get_user_input()

            # Check if the attack hits an enemy ship
            # Mark the hit on the enemy's Game_Board
            # Check if any enemy ship is sunk
            # Mark the miss on the enemy's Game_Board
            if self.enemy_board.check_hit(x, y):
                print("Hit!")
                self.enemy_board.mark_hit(x, y)
                for ship in self.enemy_ships:
                    if self.enemy_board.is_ship_sunk(ship):
                        print("######## You sunk an enemy ship! ###########")
            else:
                print("Miss!")
                self.enemy_board.mark_miss(x, y)

            # Check if all enemy ships are sunk
            if all(self.enemy_board.grid[i][j] != 'X'
                   for i in range(self.game_size)
                   for j in range(self.game_size)):
                print('####################################################')
                print("############# Congratulations! You've won! #########")
                print('####################################################')
                break
            # Enemy's turn
            self.enemy_turn()

    def enemy_turn(self):
        x = random.randint(0, self.game_size - 1)
        y = random.randint(0, self.game_size - 1)
        if self.Game_Board.check_hit(x, y):
            print(f"Enemy hit your ship at {x}, {y}!")
            self.Game_Board.mark_hit(x, y)
        else:
            print(f"Enemy missed at {x}, {y}!")

    def get_user_input(self):
        while True:
            try:
                x = int(input("Enter X coordinate (0-{}): "
                              .format(self.game_size - 1)))
                y = int(input("Enter Y coordinate (0-{}): "
                              .format(self.game_size - 1)))
                if not (0 <= x < self.game_size and 0 <= y < self.game_size):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Coordinates must be integers within the "
                      "Game_Board game_size.")
        return x, y


'''
############################## Main ##################################
# Start the game by creating a Battleship Game instance
# with a given Game_Board game_size
'''

if __name__ == "__main__":
    print('##########################################################')
    print('######## Welcome to the Ultimate Battleship Game #########')
    print('##########################################################')
    while True:
        try:
            game_size = int(
                input(
                    "Enter the Game size of the Game_Board "
                    "(It should be greater than 1):"))
            if game_size <= 1:
                raise ValueError
            break
        except ValueError:
            print(
                "Invalid input! The Game size must be an integer > 1.")
    game = Battleship_Game(game_size)
    game.play_game()
