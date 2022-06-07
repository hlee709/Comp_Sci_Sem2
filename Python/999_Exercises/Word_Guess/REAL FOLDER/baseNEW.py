import random
wordlist = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(1)
        
num = random.randrange(12972)
answer = word_list[num]
print(answer)

a = 0
for i in range(0, 6):
    guess = input("Guess the word!: ")
    if guess == answer:
        print("U guessed the word!")
        a = 1
        break
    else:
        print("guess again..: ")
if a == 0:
    print("you lost :( The word was " + answer)

f.close()