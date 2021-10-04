from collections import Counter


try:
    file = open('try.txt', 'r')
except FileNotFoundError:
    print('You are an idiot, choose a file in the laptop or the correct path')
    raise


file_read = file.read()

file.close()

file_read = file_read.split(' ')
# print(file_read)
# file_read.count('and')

list_of_word = []
for i in file_read:
    i = i.replace(',','').replace('.','').replace('[','').replace('\n','').replace(']','').lower()
    list_of_word.append(i)

bella = Counter(list_of_word)
print(bella)
print(type(bella))

D = {}
for word in list_of_word:
    if word in D.keys():
        D[word] += 1
    else:
        D[word] = 1
print(D['by'])
