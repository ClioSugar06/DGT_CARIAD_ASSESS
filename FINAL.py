# set up function here
def instruction():
    instructions = "When you begin, it will show the question on the screen. At the end of the question " \
                   "it will have the four potential answers. \n"\
                   "Choose one answer and type in 1,2,3,4 to choose your answer. \n"\
                   "It will then tell you if you were correct or not, then it will show the next question."
    error = "Please type yes or no"
    while True:
        print('--------')
        played_before = input("Have you played before? ").lower()
        if played_before == 'yes' or played_before == 'y':
            print('Welcome back!')
            break

            # play instructions if user says no
        elif played_before == 'no' or played_before == 'n':
            print('--------')
            print(instructions)
            break

        # retry if user inputs something incorrect
        else:
            print(error)


def ready():
    instructions = "When you begin, it will show the question on the screen. At the end of the question " \
                   "it will have the four potential answers. \n"\
                   "Choose one answer and type in 1,2,3,4 to choose your answer. \n"\
                   "It will then tell you if you were correct or not, then it will show the next question."
    error = "Please type yes or no"
    while True:
        print('--------')
        prepared = input("Are you ready? ").lower()
        if prepared == 'yes' or prepared == 'y':
            print("Lets go!")
            break

            # play instructions if user says no
        elif prepared == 'no' or prepared == 'n':
            print('--------')
            print(instructions)

        # retry if user inputs something incorrect
        else:
            print(error)


def ans_checker(question, error_message):
    while True:
        try:
            print('--------')
            ans = int(input(question))
            print('--------')
            break
        except:
            print(error_message)

    return ans

# main *****


instruction()
ready()
score = 0

# first question
question_1 = "What is the biggest planet in our solar system? 1- Earth 2- Mars 3- Jupiter 4- Saturn  "
error_message = "That is not a choice, try again"
ans1 = ans_checker(question_1, error_message)
question_1_guess = ans1

if question_1_guess == 3:
    print("correct")
    score += 1
else:
    print("Incorrect")

# second call here

question_2 = "What animals have wings, beaks and only two feet? 1- lions 2- birds 3- rabbits 4- cats"
error_message = "That is not a choice, try again"
ans2 = ans_checker(question_2, error_message)
question_2_guess = ans2

if question_2_guess == 2:
    print("Correct!")
    score += 1

else:
    print("Incorrect")

# third call here
question_3 = "Which of the following is the correct answer to: 3x7? 1- 23 2- 44 3- 68 4- 21"
error_message = "That is not a choice, try again"
ans3 = ans_checker(question_3, error_message)
question_3_guess = ans3

if question_3_guess == 4:
    print("Correct!")
    score += 1

else:
    print("Incorrect")

question_4 = "What is the most important meal of the day? 1- breakfast 2- lunch 3- dinner 4- snack time"
error_message = "That is not a choice, try again"
ans4 = ans_checker(question_4, error_message)
question_4_guess = ans4

if question_4_guess == 1:
    print("Correct!")
    score += 1

else:
    print("Incorrect")

question_5 = "Which of the following are native New Zealand animals? 1- Kiwi 2- Kea 3-Tui 4- All of the above"
error_message = "That is not a choice, try again"
ans5 = ans_checker(question_5, error_message)
question_5_guess = ans5

if question_5_guess == 4:
    print("Correct!")
    score += 1

else:
    print("Incorrect")

print('--------')
print("Congrats! You got", score, "right!!!!!")
