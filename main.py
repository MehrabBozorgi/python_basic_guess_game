guess_count = 0
guess_limit = 3
secret_number = 9

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Win!')
        break
else:
    print('You Lost !')
