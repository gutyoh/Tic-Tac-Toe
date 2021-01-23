# write your code here
import sys

win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

user_input = input("Enter cells:")


XO_string = user_input

print("---------")
print("|", XO_string[0], XO_string[1], XO_string[2], "|")
print("|", XO_string[3], XO_string[4], XO_string[5], "|")
print("|", XO_string[6], XO_string[7], XO_string[8], "|")
print("---------")

counter = 0

# 1. Check for impossible case:

if XO_string.count('X') - XO_string.count('O') > 1 or XO_string.count('O') - XO_string.count('X') > 1:
    print('Impossible')
    sys.exit()

for win_line in win_lines:
    if XO_string[win_line[0]] == XO_string[win_line[1]] == XO_string[win_line[2]] == 'X':
        counter += 1
    elif XO_string[win_line[0]] == XO_string[win_line[1]] == XO_string[win_line[2]] == 'O':
        counter += 1

if counter > 1:
    print("Impossible")
    sys.exit()

for win_line in win_lines:
    if XO_string[win_line[0]] == XO_string[win_line[1]] == XO_string[win_line[2]] == 'X':
        print(f'X wins')
        sys.exit()
    elif XO_string[win_line[0]] == XO_string[win_line[1]] == XO_string[win_line[2]] == 'O':
        print(f'O wins')
        sys.exit()

# Check for draw case:

if XO_string.count('X') + XO_string.count('O') == 9:
    print('Draw')
    sys.exit()
else:
    print("Game not finished")  # Check for game not finished case:
    sys.exit()
