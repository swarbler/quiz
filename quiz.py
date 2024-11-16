import time
import os
import json

# sets q/a list
w, h = 6, 10
multiplechoice = [[0 for x in range(w)] for y in range(h)] 
# [i][0] = question
# [i][1-4] = answers a to d
# [i][5] = correct answer (1-4)

subjects = [
    'geography', 
    'physics', 
    'chemistry', 
    'computer science', 
    'history', 
    'example'
]
with open('topics.json', 'r') as f:
    tdata = json.load(f)
topics = tdata['topics']
hasTopics = tdata['hasTopics']

chosenSubject = 'none'
chosenTopic = 'none'

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
    global chosenTopic

    # loads JSON file data containing all questions
    with open('mcq.json', 'r') as f:
        qdata = json.load(f)

    if subject == 'geography':
        # different topics in geography
        if topic == 'population and settlements' or topic == 'population' or topic == 'populations' or topic == 'settlements' or topic == 'settlement': # different words for same topic
            subtopic = 'population'
        elif topic == 'volcanoes' or topic == 'volcano': # plural or singular
            subtopic = 'volcanoes'
        elif topic == 'earthquakes' or topic == 'earthquake':
            subtopic = 'earthquakes'
        elif topic == 'rivers' or topic == 'river':
            subtopic = 'rivers'
        elif topic == 'coasts' or topic == 'coast':
            subtopic = 'coasts'
        elif topic == 'weather and climate' or topic == 'weather' or topic == 'climate':
            subtopic = 'weather'
        elif topic == 'rainforests' or topic == 'rainforest':
            subtopic = 'rainforests'
        elif topic == 'deserts' or topic == 'desert':
            subtopic = 'deserts'
        elif topic == 'map skills' or topic == 'map':
            subtopic = 'map skills'
        else:
            subtopic = 'general' # quiz with all topics

        chosenTopic = subtopic

        for i in range(10):
            multiplechoice[i] = qdata['geography'][subtopic][i]
    elif subject == 'physics':
        # different topics in physics
        if topic == 'describing motion' or topic == 'motion':
            subtopic = 'describing motion'
        elif topic == 'forces and motion' or topic == 'forces' or topic == 'force':
            subtopic = 'forces and motion'
        elif topic == 'turning effects' or topic == 'turning effect' or topic == 'turning':
            subtopic = 'turning effects'
        elif topic == 'forces and matter' or topic == 'forces and matter':
            subtopic = 'forces and matter'
        elif topic == 'energy transfer':
            subtopic = 'energy transfer'
        elif topic == 'energy resources':
            subtopic = 'energy resources'
        elif topic == 'work and power' or topic == 'work':
            subtopic = 'work and power'
        elif topic == 'kinetic particle model of matter' or topic == 'particle model':
            subtopic = 'kinetic particle model of matter'
        elif topic == 'thermal properties' or topic == 'thermal property':
            subtopic = 'thermal properties'
        elif topic == 'thermal energy transfer' or topic == 'thermal energy':
            subtopic = 'thermal energy transfer'
        elif topic == 'sound':
            subtopic = 'sound'
        elif topic == 'light':
            subtopic = 'kinetic particle model of matter'
        elif topic == 'general properties of waves' or topic == 'properties of waves' or topic == 'waves':
            subtopic = 'general properties of waves'
        elif topic == 'electromagnetic spectrum' or topic == 'electromagnetic waves':
            subtopic = 'electromagnetic spectrum'
        elif topic == 'magnetism' or topic == 'magnet':
            subtopic = 'magnetism'
        elif topic == 'static electricity' or topic == 'static':
            subtopic = 'static electricity'
        elif topic == 'electrical quantities':
            subtopic = 'electrical quantities'
        elif topic == 'electrical circuit' or topic == 'circuit':
            subtopic = 'electrical circuit'
        elif topic == 'electromotive force' or topic == 'emf':
            subtopic = 'electromotive force'
        elif topic == 'electromagnetic induction' or topic == 'induction':
            subtopic = 'electromagnetic induction'
        else:
            subtopic = 'general' # quiz with all topics

        chosenTopic = subtopic
        
        for i in range(10):
            multiplechoice[i] = qdata['physics'][subtopic][i]
    elif subject == 'chemistry':
        # different topics in chemistry
        if topic == 'states of matter' or topic == 'state of matter':
            subtopic = 'states of matter'
        elif topic == 'atomic structure' or topic == 'atoms' or topic == 'atom':
            subtopic = 'atomic structure'
        elif topic == 'chemical bonding' or topic == 'chemical bonds' or topic == 'bonding' or topic == 'bonds':
            subtopic = 'chemical bonding'
        elif topic == 'chemical formulae and equations' or topic == 'chemical formulae' or topic == 'chemical equations' or topic == 'chemical equation' or topic == 'chemical formula' or topic == 'formula' or topic == 'equation':
            subtopic = 'chemical formulae and equations'
        elif topic == 'chemical calculations' or topic == 'calculations':
            subtopic = 'chemical calculations'
        elif topic == 'electrochemistry':
            subtopic = 'electrochemistry'
        elif topic == 'chemical energetics' or topic == 'energetics':
            subtopic = 'chemical energetics'
        elif topic == 'rates of reaction' or topic == 'rate of reaction':
            subtopic = 'rates of reaction'
        elif topic == 'reversible reactions' or topic == 'reverse reactions' or topic == 'reversible' or topic == 'reverse':
            subtopic = 'thermal properties'
        elif topic == 'redox reactions' or topic == 'reduction' or topic == 'oxidation' or topic == 'redox':
            subtopic = 'redox reactions'
        elif topic == 'acids and bases' or topic == 'acids' or topic == 'bases' or topic == 'alkalis':
            subtopic = 'acids and bases'
        elif topic == 'preperation of salts' or topic == 'salts':
            subtopic = 'preperation of salts'
        elif topic == 'periodic table' or topic == 'elements':
            subtopic = 'periodic table'
        elif topic == 'metallic elements' or topic == 'metals':
            subtopic = 'metallic elements'
        elif topic == 'reactivity series' or topic == 'reactivity':
            subtopic = 'reactivity series'
        elif topic == 'extraction and corrosion' or topic == 'extraction':
            subtopic = 'extraction and corrosion'
        elif topic == 'environment':
            subtopic = 'environment'
        elif topic == 'organic chemistry' or topic == 'organic compounds':
            subtopic = 'organic chemistry'
        elif topic == 'experimental design' or topic == 'experiment design' or topic == 'paper 6':
            subtopic = 'experimental design'
        else:
            subtopic = 'general' # quiz with all topics

        chosenTopic = subtopic
        
        for i in range(10):
            multiplechoice[i] = qdata['chemistry'][subtopic][i]
    elif subject == 'computer science':
        # different topics in computer science
        if topic == 'data representation' or topic == 'data':
            subtopic = 'data representation'
        elif topic == 'data transmission' or topic == 'error checking' or topic == 'transmission':
            subtopic = 'data transmission'
        elif topic == 'hardware':
            subtopic = 'hardware'
        elif topic == 'software':
            subtopic = 'software'
        elif topic == 'internet':
            subtopic = 'internet'
        elif topic == 'automation' or topic == 'automated technologies' or topic == 'ai':
            subtopic = 'automation'
        elif topic == 'algorithm design' or topic == 'algorithm':
            subtopic = 'algorithm design'
        elif topic == 'programming' or topic == 'coding':
            subtopic = 'programming'
        elif topic == 'databases' or topic == 'database' or topic == 'sql':
            subtopic = 'databases'
        elif topic == 'boolean logic' or topic == 'logic':
            subtopic = 'boolean logic'
        else:
            subtopic = 'general' # quiz with all topics

        chosenTopic = subtopic
        
        for i in range(10):
            multiplechoice[i] = qdata['computer science'][subtopic][i]
    elif subject == 'history':
        # different topics in computer science
        if topic == 'early weimar germany' or topic == 'early weimar' or topic == '1918-23':
            subtopic = 'Early Weimar Germany (1918-23)'
        elif topic == 'golden age weimar germany' or topic == 'golden age weimar' or topic == '1924-29':
            subtopic = 'Golden Age Weimar Germany (1924-29)'
        elif topic == 'rise of the nazis' or topic == 'early nazis':
            subtopic = 'Rise of the Nazis'
        elif topic == 'nazi germany' or topic == 'nazi rule' or topic == '1933-45':
            subtopic = 'Nazi Germany (1933-45)'
        else:
            subtopic = 'general' # quiz with all topics

        chosenTopic = subtopic
        
        for i in range(10):
            multiplechoice[i] = qdata['history'][subtopic][i]
    elif subject == 'example': # example for testing
        for i in range(10):
            multiplechoice[i] = qdata['example'][i]
    else: # error message if incorrect value is entered
        for i in range(10):
            multiplechoice[i] = qdata['error'][i]
    
def mcq(): # multiple choice questions
    for i in range(10):
        question = multiplechoice[i][0]
        answerA = multiplechoice[i][1]
        answerB = multiplechoice[i][2]
        answerC = multiplechoice[i][3]
        answerD = multiplechoice[i][4]
        correctAnswer = multiplechoice[i][5]

        # displays chosen subject and topic
        print('Subject:\t' + chosenSubject)
        print('Topic:  \t' + chosenTopic)
        print('')

        # asks with question # and some formatting
        print('Question ' + str(i + 1) + ': ' + question + '?')
        print('')
        print('Choose one option:')
        print('1 : ' + answerA)
        print('2 : ' + answerB)
        print('3 : ' + answerC)
        print('4 : ' + answerD)
        print('')
        userAnswer = input('~~> ')
        userAnswerNum = 0

        # if users type a word instead of a number, userAnswerNum set to 0
        try:
            userAnswerNum = int(userAnswer)
        except:
            userAnswerNum = 0

        if userAnswerNum == correctAnswer:
            print('You got it right!')
        else:
            # tells user correct answer
            print('You got it wrong! The actual answer was: ' + str(correctAnswer))
        
        dotdotdot()

def structured(): # structured questions
    pass 
    # read essay text file and send to teacher for marking? (longer essay-style questions)
    # type into quiz program and get marks based on keywords? (shorter  questions only)

while True:
    # choose subject to study
    print('Select a subject to study:')
    print('')
    for i in subjects: # dynamic amount of subjects
        print('~ ' + i)
    print('')
    userSubject = input('~~> ').lower() # sets answer as lowercase to avoid miscasing

    userHasTopic = False

    # if user mistypes subject, set userAnswer as 'error'
    try:
        if hasTopics[userSubject]: # ask for topic if subject has them
            # choose topic to study
            print('')
            print('Select a topic to study:')
            print('')
            for i in topics[userSubject]: # dynamic amount of subjects
                print('~ ' + i) # prints subjects as a list
            print('')
            userTopic = input('~~> ').lower()  # sets answer as lowercase to avoid miscasing
            userHasTopic = True
    except:
        userSubject = 'error'

    dotdotdot()

    chosenSubject = userSubject

    if userHasTopic:
        setSubject(userSubject, userTopic)
    else:
        setSubject(userSubject)
        chosenTopic = 'N/A'
    mcq()
    structured()

