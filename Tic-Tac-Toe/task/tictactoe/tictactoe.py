import sys


def print_grid():
    print("---------")
    print("|", B[0][0], B[0][1], B[0][2], "|")
    print("|", B[1][0], B[1][1], B[1][2], "|")
    print("|", B[2][0], B[2][1], B[2][2], "|")
    print("---------")


B = [['_', '_', '_'],
     ['_', '_', '_'],
     ['_', '_', '_']]

play_counter = 0

print_grid()  # Print the grid

while True:

    coordinate_list = [0, 0]

    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            break
        except ValueError:
            print("You should enter numbers!")

    while True:
        if 1 <= x <= 3 and 1 <= y <= 3:
            coordinate_list[0] = x
            coordinate_list[1] = y
            break
        else:
            print("Coordinates should be from 1 to 3!")
            try:
                x, y = map(int, input("Enter the coordinates: ").split())
                if 1 <= x <= 3 and 1 <= y <= 3:
                    coordinate_list[0] = x
                    coordinate_list[1] = y
                break
            except ValueError:
                print("You should enter numbers!")

    if play_counter < 9:
        for i in range(len(B)):
            if i == coordinate_list[0] - 1:
                for j in range(len(B[i])):
                    if j == coordinate_list[1] - 1:
                        if B[i][j] == '_' and play_counter % 2 == 0 and play_counter < 9:
                            B[i][j] = 'X'
                            play_counter += 1
                        elif B[i][j] == '_' and play_counter % 2 == 1 and play_counter < 9:
                            B[i][j] = 'O'
                            play_counter += 1
                        else:
                            print("This cell is occupied! Choose another one!")
                            break
                break

    if play_counter > 4:

        # Check for X win-cons:

        # Horizontal wincons:
        if B[0][0] == 'X' and B[0][1] == 'X' and B[0][2] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        elif B[1][0] == 'X' and B[1][1] == 'X' and B[1][2] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        elif B[2][0] == 'X' and B[2][1] == 'X' and B[2][2] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        # Vertical wincons:
        elif B[0][0] == 'X' and B[1][0] == 'X' and B[2][0] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        elif B[0][1] == 'X' and B[1][1] == 'X' and B[2][1] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        elif B[0][0] == 'X' and B[1][2] == 'X' and B[2][2] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        # Diagonal wincons:
        elif B[0][0] == 'X' and B[1][1] == 'X' and B[2][2] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

        elif B[0][2] == 'X' and B[1][1] == 'X' and B[2][0] == 'X':
            print_grid()
            print("X wins")
            sys.exit()

    if play_counter > 4:

        # Check for O win-cons:

        # Horizontal wincons:
        if B[0][0] == 'O' and B[0][1] == 'O' and B[0][2] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        elif B[1][0] == 'O' and B[1][1] == 'O' and B[1][2] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        elif B[2][0] == 'O' and B[2][1] == 'O' and B[2][2] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        # Vertical wincons:
        elif B[0][0] == 'O' and B[1][0] == 'O' and B[2][0] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        elif B[0][1] == 'O' and B[1][1] == 'O' and B[2][1] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        elif B[0][0] == 'O' and B[1][2] == 'O' and B[2][2] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        # Diagonal wincons:
        elif B[0][0] == 'O' and B[1][1] == 'O' and B[2][2] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

        elif B[0][2] == 'O' and B[1][1] == 'O' and B[2][0] == 'O':
            print_grid()
            print("O wins")
            sys.exit()

    if play_counter == 9:
        print_grid()
        print("Draw")
        sys.exit()

    print_grid()
