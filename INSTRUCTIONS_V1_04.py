def instruction():
    instructions = "When you begin, it will show the question on the screen. At the end of the question it will have the four potential answers. Choose one answer and type in 1,2,3,4 to choose your answer. " \
                   "It will then tell you if you were correct or not, then it will show the next question."
    error = "Please type yes or no"
    while True:
        played_before = input("Have you played before? ").lower()
        if played_before == 'yes' or played_before == 'y':
            print('Welcome back!')
            break

            # play instructions if user says no
        elif played_before == 'no' or played_before == 'n':
            print(instructions)
            break

        # retry if user inputs something incorrect
        else:
            print(error)


def ready():
    instructions = "When you begin, it will show the question on the screen. At the end of the question it will have the four potential answers. Choose one answer and type in 1,2,3,4 to choose your answer. " \
                   "It will then tell you if you were correct or not, then it will show the next question."
    error = "Please type yes or no"
    while True:
        prepared = input("Are you ready? ").lower()
        if prepared == 'yes' or prepared == 'y':
            ans_checker()

            # play instructions if user says no
        elif prepared == 'no' or prepared == 'n':
            print(instructions)

        # retry if user inputs something incorrect
        else:
            print(error)


instruction()
ready()
