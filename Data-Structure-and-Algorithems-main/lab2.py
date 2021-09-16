import random

def is_palyndrome(a):
    a = a.lower()
    paly = False
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            print(f'{a} is not palyndrome')
            break
        else:
            paly = True
    if paly:
        print(f'{a} is palyndrome')



is_palyndrome('Anna')

is_palyndrome('bob')

is_palyndrome('Lorenzo')
#
#
# def guess_number():
#     r = random.randint(1,51)
#     guess = int(input('Your guess? '))
#     l = 0
#     while guess != r:
#
#         if guess > r:
#             print('Your guess is bigger')
#         else:
#             print('Your guess is lower')
#         new_guess = int(input('New guess? '))
#         l += 1
#         guess = new_guess
#     print(f'You get the number in {l} guesses')
#
# guess_number()
#

def nim_game_computer_pick(sticks):
    if sticks < 4:
        move = sticks
        print(f'The computer picks {sticks} sticks and wins')
    elif sticks % 4 == 0:
        print('Comuputer loose :(')
        move = random.randint(1,3)
        print(f'Computer picks {move}')
    elif (sticks-1) % 4 == 0:
        move = 1
        print(f'Computer picks {move}')
    elif (sticks-2) % 4 == 0:
        move = 2
        print(f'Computer picks {move}')
    elif (sticks-3) % 4 == 0:
        move = 3
        print(f'Computer picks {move}')
    return move

def nim_game():
    sticks = 12
    first_move = int(input('Your pick? '))
    if first_move not in range(1,4):
        first_move = int(input('Invalid pick. Your pick? '))
    sticks = sticks - first_move
    print(sticks)
    while sticks > 0:
        comp_move = nim_game_computer_pick(sticks)
        sticks = sticks - comp_move
        if sticks > 0:
            print(f'There are {sticks} remain')
            your_move = int(input('Your pick? '))
            if your_move not in range(1,4):
                your_move = int(input('Invalid pick. Your pick? '))
            sticks = sticks - your_move

nim_game()
