import random
secret = random.randint(1,50)
print(secret)
print('Guess the number between 1 to 50: ')
for i in range(1,7):
    guess = int(input('take a guess: '))
    if guess < secret:
        print('Your guess is too low')
    elif guess > secret:
        print('Your guess is too high')
    else:
        break
if guess == secret:
    print("you guessed my number in "+ str(i) + ' guess!')
else:
    print("Nope The number was :"+ str(secret))