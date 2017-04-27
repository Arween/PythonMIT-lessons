import random

def selection_level():
    print("Select difficulty level: easy, middle, hard")
    level = input("Level: ")
    # if selected - easy
    if level == 'easy':
        numb_comp = random.randint(1, 10)
        # print(numb_comp)
        easy_level(numb_comp)

    if level == 'middle':
        numb_comp = random.randint(1, 30)
        # print(numb_comp)
        middle_level(numb_comp)

    if level == 'hard':
        numb_comp = random.randint(1, 100)
        # print(numb_comp)
        forms_prompts(numb_comp)
        hard_level(numb_comp)

# function - if selected - easy

def easy_level(numb_comp):

    number = int(input("Your number: "))
    if number == numb_comp:
        print("This game is yours!")
        play_game()
    else:
        print("Try again!")
        easy_level(numb_comp)

# function - if selected - middle

def middle_level(numb_comp):

    n = 0
    flag = False
    while n < 5:
        number = int(input("Your number: "))
        if number == numb_comp:
            # print("ok")
            flag = True
            break
        else:
            # print("ne ok")
            search_region(numb_comp, number)
            search_side(numb_comp, number)
        n += 1

    if flag == True:
        print("This game is yours!")
        play_game()
    else:
        print("You lost this round, detective.")

# function - if selected - hard

def hard_level(numb_comp):

    n = 0
    flag = False
    while n < 10:
        number = int(input("Your number: "))
        if number == numb_comp:
            # print("ok")
            flag = True
            break
        else:
            # print("ne ok")
            search_region(numb_comp, number)
        n += 1

    if flag:
        print("This game is yours!")
        play_game()
    else:
        print("You lost this round, detective.")

# сhecks closely or far

def search_region(numb_comp, number):

    numbers_region = list(range(numb_comp - 5, numb_comp + 5))
    flag = False
    for numb in numbers_region:
        if numb == number:
            flag = True
            # print(numbers_region)
            break
        else:
            flag = False
    if flag == True:
        print("closely!!")
    else:
        print("far!!")

# сhecks "To the left" or "To the right"

def search_side(numb_comp, number):
    if number > numb_comp:
        print("To the left")
    else:
        print("To the right")

# compile promts (even/odd, %3, %5, prime number)

def forms_prompts(numb_comp):
    promts = 'Your promts: '
    if numb_comp % 2 == 0:
        promts += 'even'
    else:
        promts += 'odd'
    if numb_comp % 3 == 0:
        promts += ', divided by 3 without remainder'
    else:
        promts += ', divided by 3 with remainder'
    if numb_comp % 5 == 0:
        promts += ', divided by 5 without remainder'
    else:
        promts += ', divided by 5 with remainder'
    k = 0
    for i in range(1, 11):
        if numb_comp % i == 0:
            k += 1

    if k == 0:
        promts += ', prime number'

    print(promts)

# function "play again"

def play_game():
   print("Play again: yes or no")
   play = input("Play: ")
   if play == 'yes':
      selection_level()
   elif play == 'no':
       print("Poki poki")
   else:
      print("Selected: yes or no!!")
      play_game()

selection_level()