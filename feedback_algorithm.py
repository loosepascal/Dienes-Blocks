#-------------------------------------------------------------------------------
# Name:        Questions and Feedback
# Purpose:     Part of the 3rd Year Group Project "Dienes Blocks" for Sparx
#              This is the code that deals with questions being asked from the teacher's side
#
# Author:      Christos Karpis
#
# Created:     11/06/2014
# Copyright:   (c) Christos Karpis 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

# there are 3 levels of questions: easy, medium and hard
##easy_questions = [1, 3, 5, 9, 13, 17, 16, 19, 8, 20]
question_difficulty = "easy"

def generateQuestion():
    if question_difficulty == "easy":
        question = random.randint(1,20)
    elif question_difficulty == "medium":
        question = random.randint(21, 999)
    elif question_difficulty =="hard":
        question = random.randint(1000, 2999)
    print question_difficulty, question
    return question
# used to keep track of the questions asked
# code to send question via bluetooth

# code to receive answer via bluetooth

#open a text file and put in the question, answer and attempt number

def main():
    while True:
        # generate question
        current_question = generateQuestion()
        # send the question via bluetooth
        # receive the answer via bluetooth
        # check answer
        if answer == current_question:
            correct = True
            previous_question = current_question

if __name__ == '__main__':
    main()
