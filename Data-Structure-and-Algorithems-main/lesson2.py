# x = input('Your number? ')
#
# if int(x) < 0:
#     raise ValueError('your numeber is negative')
# if int(x) % 2 == 0:
#     print(f'{x} is an even number')
# else:
#     print(f'{x} is an odd number')
#
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
#Nim game

from random import randint

n_player = input('Number of players? ')

D = {}
for i in range(int(n_player)):
    player_i = input(f'Name of player {i+1} ')
    D[i+1] = player_i
print('And computer of course')
D[int(n_player)+1] = 'Computer'
print(D)

who_start = randint(1,int(n_player) + 2)
print(f'{D[who_start]} starts')

sticks = 12
while sticks > 0:
    take = input(f'{D[who_start]} turn. How many sticks do take (max 3, min 1)?')
    sticks =- int(take)
