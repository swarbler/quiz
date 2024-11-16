import time
import os
import json

# sets q/a list
w, h = 6, 10
multiplechoice = [[0 for x in range(w)] for y in range(h)] 
# [i][0] = question
# [i][1-4] = answers a to d
# [i][5] = correct answer (1-4)

subjects = ['geography', 'physics', 'chemistry', 'computer science', 'history', 'example']
topics = {
    'geography': [
        'population and settlements',
        'volcanoes',
        'earthquakes',
        'rivers',
        'coasts',
        'weather and climate',
        'rainforests',
        'deserts',
        'map skills'
    ],
    'physics': [
        'describing motion',
        'forces and motion',
        'turning effects',
        'forces and matter',
        'energy transfer',
        'energy resources',
        'work and power', 
        'kinetic particle model of matter', 
        'thermal properties', 
        'thermal energy transfer', 
        'sound',
        'light', 
        'general properties of waves', 
        'electromagnetic spectrum', 
        'magnetism', 
        'static electricity', 
        'electrical quantities', 
        'electrical circuit',
        'electromotive force',
        'electromagnetic induction'
    ],
    'chemistry': [
        'population and settlements',
        'volcanoes',
        'earthquakes',
        'rivers',
        'coasts',
        'weather and climate',
        'rainforests',
        'deserts',
        'map skills'
    ],
    'computer science': [
        'population and settlements',
        'volcanoes',
        'earthquakes',
        'rivers',
        'coasts',
        'weather and climate',
        'rainforests',
        'deserts',
        'map skills'
    ],
    'history': [
        'population and settlements',
        'volcanoes',
        'earthquakes',
        'rivers',
        'coasts',
        'weather and climate',
        'rainforests',
        'deserts',
        'map skills'
    ]
}
hasTopics = {
    'geography': True, 
    'physics': True, 
    'chemistry': True, 
    'computer science': True, 
    'history': True, 
    'example': False
}

# small 'loading screen'
def dotdotdot():
    for dot in range(2): # repeats twice
        print('.', end='') # no new line after each dot
        time.sleep(0.5) # small delay between each dot
    print('.') # new line after last dot
    time.sleep(1) # longer delay after last dot
    print('\033c', end='') # clear terminal


# sets questions and answers based on subject and topic
def setSubject(subject='example', topic='none'):
    # loads JSON file data containing all questions
    with open('mcq.json', 'r') as f:
        data = json.load(f)

    if subject == 'geography':
        geography = data['geography']
        # different topics in geography
        if topic == 'population and settlements' or topic == 'population' or topic == 'settlements' or topic == 'settlement': # different words for same topic
            for i in range(10):
                multiplechoice[i] = geography['population'][i]
        elif topic == 'volcanoes' or topic == 'volcano': # plural or singular
            for i in range(10):
                multiplechoice[i] = geography['volcanoes'][i]
        elif topic == 'earthquakes' or topic == 'earthquake':
            for i in range(10):
                multiplechoice[i] = geography['earthquakes'][i]
        elif topic == 'rivers' or topic == 'river':
            for i in range(10):
                multiplechoice[i] = geography['rivers'][i]
        elif topic == 'coasts' or topic == 'coast':
            for i in range(10):
                multiplechoice[i] = geography['coasts'][i]
        elif topic == 'weather and climate' or topic == 'weather' or topic == 'climate':
            for i in range(10):
                multiplechoice[i] = geography['weather'][i]
        elif topic == 'rainforests' or topic == 'rainforest':
            for i in range(10):
                multiplechoice[i] = geography['rainforests'][i]
        elif topic == 'deserts' or topic == 'desert':
            for i in range(10):
                multiplechoice[i] = geography['deserts'][i]
        elif topic == 'map skills' or topic == 'map':
            for i in range(10):
                multiplechoice[i] = geography['map skills'][i]
        else:
            # quiz with all topics
            pass
    elif subject == 'example': # example for testing
        for i in range(10):
            multiplechoice[i] = data['example'][i]
    else: # error message if incorrect value is entered
        for i in range(10):
            multiplechoice[i] = data['error'][i]

def mcq(): # multiple choice questions
    for i in range(10):
        question = multiplechoice[i][0]
        answerA = multiplechoice[i][1]
        answerB = multiplechoice[i][2]
        answerC = multiplechoice[i][3]
        answerD = multiplechoice[i][4]
        correctAnswer = multiplechoice[i][5]

        # asks with question # and some formatting
        print('Question ' + str(i + 1) + ': ' + question + '?')
        print('')
        print('Choose one option:')
        print('1 : ' + answerA)
        print('2 : ' + answerB)
        print('3 : ' + answerC)
        print('4 : ' + answerD)
        print('')
        userAnswer = input('Your answer: ')
        userAnswerNum = 0

        # if users type a word instead of a number, userAnswerNum set to 0
        try:
            userAnswerNum = int(userAnswer)
        except:
            userAnswerNum = 0

        if userAnswerNum == correctAnswer:
            print('You got it right!')
        else:
            print('You got it wrong! The actual answer was: ' + str(correctAnswer))
        
        dotdotdot()

def structured(): # structured questions
    pass 
    # read essay text file and send to teacher for marking? (longer essay-style questions)
    # type into quiz program and get marks based on keywords? (shorter  questions only)

while True:
    # choose subject to study
    print('Which subject would you like to test yourself with?')
    print('')
    print('Choose one option:')
    for i in subjects: # dynamic amount of subjects
        print('- ' + i)
    print('')
    userSubject = input('Your answer: ').lower() # sets answer as lowercase to avoid miscasing

    userHasTopic = False

    # if user mistypes subject, set userAnswer as 'error'
    try:
        if hasTopics[userSubject]: # ask for topic if subject has them
            # choose topic to study
            print('Which topic would you like to test yourself with?')
            print('')
            print('Choose one option:')
            for i in topics[userSubject]: # dynamic amount of subjects
                print('- ' + i) # prints subjects as a list
            print('')
            userTopic = input('Your answer: ').lower()  # sets answer as lowercase to avoid miscasing
            userHasTopic = True
    except:
        userSubject = 'error'

    dotdotdot()

    if userHasTopic:
        setSubject(userSubject, userTopic)
    else:
        setSubject(userSubject)
    mcq()
    structured()

