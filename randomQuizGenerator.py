#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# Opena and save the states and capital from data file in dict. Keys are states and values are their capitals.

capitals = {}
with open(f'D:\\Python practice\\Projects\\Generate random quiz file\\input\\StatesAndCapitals.txt') as file:
    for line in file:
        (key, value) = line.split(" : ")
        capitals[key] = value
        
# Generate 35 quiz files.
for quizNum in range(35):


    # Create the quiz and answer key files.
    quizFile = open(f'output\capitalsquizQuestions\capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'output\capitalsquizAnswers\capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Paper {quizNum + 1})')
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 36 states, making a question for each for each.
    for questionNum in range(36):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(set(capitals.values()))         
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
         # Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')
         # TODO: Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
        answerKeyFile.write('\n')
    quizFile.close()
    answerKeyFile.close()











