"""
1- Given a list of numbers, create a function that returns a list where all similar adjacent
elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
"""

import random


def reduce_list(list):
    for i in range(len(list)):
        list[i] = round(list[i])
    print(list)


reduce_list([1, 2, 3.3])

print("======================================")

"""
2-​​Consider dividing a string into two halves
Case 1:

The length is even, the front and back halves are the same length.

Case 2:
The length is odd, we’ll say that the extra char goes in the front half.
E.g. ‘abced’, the front half is ‘abc’, the back half’de.

Given 2 strings, a and b, return a string of the form:
(a-front + b-front) + (a-back +b-back)

"""


def divide_string(*args):
    front = ""
    back = ""
    for arg in args:
        length = len(arg)
        if length % 2:  # odd
            front += arg[:length//2+1]
            back += arg[length//2+1:]
        else:
            front += arg[:length//2]
            back += arg[length//2:]

    print(f"front: {front}, back: {back}")


divide_string("mariam", "bakry")

"""
3- Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.E.X.
[1,5,7,9] -> True
[2,4,5,5,7,9] -> False

"""


def is_deffirent(*args):
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            if args[i] == args[j]:
                return False

    return True


print("[1,5,7,9] : ", is_deffirent(1, 5, 7, 9))
print("[2,4,5,5,7,9] :  ", is_deffirent(1, 5, 5, 7, 9))

# 4- Given unordered list, sort it using algorithm bubble sort


def bubble_sort(list):
    flag = True
    for i in range(len(list)):
        if not flag:
            return list

        flag = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                flag = True
    return list


print("sorted list: ", bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


"""
5- Gusses game

- Your game generates a random number and gives only 10 tries for the 
  user toguess that number.
- Get a user input and compare it with the random number.
- Display a hit message to the user in case the use number is smaller or 
  bigger ofthe random number.
- If the user type number is out of range(100),
  display a message that is not allowedand don’t count this as try.
- If user type a number that has been entered before, display a hint message anddon’t
  count this as try
- In case the user entered a correct number within the 10 tries,
  display acongratulations message and let your application guess 
  another random numberwith the remain number of tries.
- If the user finishes all his tries, 
  display a message to ask him if he wants to playagain or not.
"""

def guessing_game(tries=10):
    n = 1
    rand = random.randint(0, 100)
    gusses = set()
    while n <= tries:
        print(f"\ntry number: {n}")
        guess = int(input(f"\nEnter number:\n"))
        if guess > 100 or guess < 0:
            print("\nonly numbers between 0 and 100 try again\n")
            continue
        if guess in gusses:
            print("\nyou already guessed this number before try again\n")
            continue

        gusses.add(guess)
        if guess > rand:
            print("\ntry smaller\n")
        elif guess < rand:
            print("\ntry bigger\n")
        else:
            print(f"\nYou are guessing right now the answer is {guess}\n")
            answer = input(f"\nDo you want to play again?y(yes):n(no)\n")
            if answer.lower() == "y" or answer.lower() == "yes":
                guessing_game()
            break
        n += 1
    if n > 10:
        print("\nGame Over\n")
        answer = input(f"\nDo you want to play again?y(yes):n(no)\n")
        if answer.lower() == "y" or answer.lower() == "yes":
            guessing_game()


guessing_game(tries=10)