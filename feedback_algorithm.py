#-------------------------------------------------------------------------------
# Name:        Questions and Feedback
# Purpose:     Part of the 3rd Year Group Project "Dienes Blocks" for Sparx
#              This is the code that deals with questions being asked from the teacher's side
#
# Author:      Christos Karpis
#
# Created:     11/06/2014
# Copyright:   (c) Christos Karpis 2014
#-------------------------------------------------------------------------------

## Other comments: This for now ensures the same question is not repeated,
## but still does not make sure the question can only be repeated once 10 others
## have been asked

import random

# there are 3 levels of questions: easy, medium and hard
# each one has 3 sublevels: 1(easiest), 2 and 3 (hardest)

# generating the question based on the difficulty level
def generateQuestion(question_difficulty, sublevel):
    if question_difficulty == "easy":
        if sublevel == 1:
            question = random.randint(1,10)
        elif sublevel == 2:
            question = random.randint(11,20)
        elif sublevel == 3:
            question = random.randint(21,100)
    elif question_difficulty == "medium":
        if sublevel == 1:
            question = random.randint(101,110)
        elif sublevel == 2:
            question = random.randint(111,200)
        elif sublevel == 3:
            question = random.randint(201,999)
    elif question_difficulty =="hard":
        if sublevel == 1:
            question = random.randint(1000,1100)
        elif sublevel == 2:
            question = random.randint(1100,1200)
        elif sublevel == 3:
            question = random.randint(1200,2999)
    print question_difficulty, question
    return question

def main():
    # generate the start question
    question_difficulty = "easy"
    sublevel = 1
    current_question = generateQuestion(question_difficulty, sublevel)
    attempt_number = 1
    correct = 0
    number_wrong = 0
    while True:
        # send the question via bluetooth
        # receive the answer via bluetooth

        # check answer
        # if the answer is correct
        if answer == current_question:
            # check whether 3 correct ones have been answered in a row
            correct += 1
            if attempt_number == 2:
                correct = 0
            # keep track of the previous question
            previous_question = current_question

            #generate a new question
            if correct == 3: # if 3 correct ones in a row
                sublevel += 1 # go to the next level
                if sublevel > 3:
                    sublevel = random.randint(1,3)
                current_question = generateQuestion(question_difficulty, sublevel)
                correct = 0
                attempt_number = 1
            else:
                # ensure question is not the same as the previous one
                while current_question == previous_question:
                    current_question = generateQuestion(question_difficulty, sublevel)
                attempt_number = 1
        # if the answer is wrong once
        elif answer != current_question and attempt_number == 1:
            correct = 0
            attempt_number = 2
        # if the answer is wrong after retrying
        elif answer != current_question and attempt_number == 2:
            current_question = generateQuestion(question_difficulty, sublevel)
            number_wrong += 1
            if number_wrong == 2:
                if sublevel != 1:
                    sublevel -= 1
                current_question = generateQuestion(question_difficulty, sublevel)
                number_wrong = 0


if __name__ == '__main__':
    main()
