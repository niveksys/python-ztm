from random import randint
import sys

# generate a number 1~10
start = int(sys.argv[1])
end = int(sys.argv[2])
answer = randint(start, end)

# input from user?
# check that input is a number 1~10
while True:
    try:
        guess = int(input(f'guess a number {start}~{end}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
    except ValueError:
        print('please enter a number')
        continue

# check if a number is the right guess. Otherwise ask again
