from random import randrange

AMOUNT_OF_GAMES = 10000

board = range(1, 101)

ladders = {2: 23,
           6: 45,
           20: 59,
           52: 72,
           57: 96,
           71: 92}

snakes = {98: 40,
          87: 49,
          84: 63,
          73: 15,
          56: 8,
          50: 5,
          43: 17}

def main():
    sum = 0
    for _ in range(AMOUNT_OF_GAMES):
        pass
        # play game and add to sum
        sum += play_game() 

    average = sum / AMOUNT_OF_GAMES
    print(f"Average amount of moves made: {average}")

def play_game() -> int:
    moves_made = 0
    position = 1
    while position != 100:
        moves_made += 1

        position += randrange(1, 7) # move a dice roll

        if position > 100: # go back if overshoot
            position = 200 - position

        if position in snakes:
            position = snakes[position]

        if position in ladders:
            position = ladders[position]
        
    return moves_made


if __name__ == "__main__":
    main()
