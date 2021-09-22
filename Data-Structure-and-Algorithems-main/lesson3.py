
import statistics
import random


population_ages = [81, 100, 1, 9, 49, 64, 4, 9, 16, 25, 36]

mean = round(statistics.mean(population_ages))
mode = statistics.mode(population_ages)
median = statistics.median(population_ages)

print(f'Regarding the population:the mean is {mean}; the mode is {mode} and the median is {median}')

# sentence = input('Write your sentence: ')
# sentence = sentence.split()
# D = {}
# for word in sentence:
#     word = word.lower()
#     if word in D:
#         D[word] += 1
#     else:
#         D[word] = 1
#
# print(D)
#
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']


# Paper, scissor, rock

user_pick = input('Your pick? ')
valid_pick = ['paper', 'scissor', 'rock']
while user_pick not in valid_pick:
    user_pick = input(f'Invalid pick. The valid picks are {valid_pick} Your pick? ')
D = {1: 'paper', 2: 'scissor', 3: 'rock'}
computer_pick = random.randint(1,3)
print(D[computer_pick])
if D[computer_pick] == user_pick:
    print(f'EVEN, you and the computer choose {D[computer_pick]}')
elif D[computer_pick] == 'rock' and user_pick == 'paper':
    print(f'The copmputer has choose {D[computer_pick]}. You won!')
elif D[computer_pick] == 'scissor' and user_pick == 'rock':
    print(f'The copmputer has choose {D[computer_pick]}. You won!')
elif D[computer_pick] == 'rock' and user_pick == 'paper':
    print(f'The copmputer has choose {D[computer_pick]}. You won!')
else:
    print(f'You have lost. The computer has choosen {D[computer_pick]}')

another_game = input('Do you wont to play another game? ')
if another_game == 'Yes':
    user_pick = 'De'
