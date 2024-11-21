import time
import os
import json
import random
import sys

from PIL import Image

# sets q/a list
w, h = 7, 10
multiplechoice = [[0 for x in range(w)] for y in range(h)] 
# [i][0] = question
# [i][1-4] = answers a to d
# [i][5] = correct answer (1-4)
# [i][6] = image path (may be empty)

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
hasTopicsAbbrv = tdata['hasTopicsAbbrv']
abbrvDef = tdata['abbrvDef']

endSignal = ["ENDHERE", "A", "B", "C", "D", -1]

chosenSubject = 'none'
chosenTopic = 'none'
mcqLength = 10

mcqTotal = 0

with open('messages.json', 'r') as f:
    sdata = json.load(f)
mcqMessages = sdata['mcq']

def dotdotdot():
    """small loading screen"""
    for dot in range(2): # repeats twice
        print('.', end='', flush=True) # no new line after each dot
        time.sleep(.5) # small delay between each dot
    print('.')
    time.sleep(1) # longer delay after last dot
    print('\033c', end='') # clear terminal


# sets questions and answers based on subject and topic
def set_subject(subject='example', topic='none'):
    """sets questions and answers based on subject and topic"""
    global chosenTopic
    global mcqLength

    # loads JSON file data containing all questions
    with open('mcq.json', 'r') as f:
        qdata = json.load(f)
    
    mcqLength = 10

    match subject:
        case 'geography':
            # different topics in geography
            match topic:
                case 'population and settlements' | 'population' | 'populations' | 'settlements' | 'settlement': # different words for same topic
                    subtopic = 'population'
                case 'volcanoes' | 'volcano': # plural or singular
                    subtopic = 'volcanoes'
                case 'earthquakes' | 'earthquake':
                    subtopic = 'earthquakes'
                case 'rivers' | 'river':
                    subtopic = 'rivers'
                case 'coasts' | 'coast':
                    subtopic = 'coasts'
                case 'weather and climate' | 'weather' | 'climate':
                    subtopic = 'weather'
                case 'rainforests' | 'rainforest':
                    subtopic = 'rainforests'
                case 'deserts' | 'desert':
                    subtopic = 'deserts'
                case 'map skills' | 'map':
                    subtopic = 'map skills'
                case _:
                    subtopic = 'general' # quiz with all topics

            chosenTopic = subtopic

            for i in range(10):
                if qdata['geography'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['geography'][subtopic][i]
        case 'physics':
            # different topics in physics
            match topic:
                case 'decribing motion' | 'motion':
                    subtopic = 'describing motion'
                case 'forces and motion' | 'forces' | 'force':
                    subtopic = 'forces and motion'
                case 'turning effects' | 'turning effect' | 'turning':
                    subtopic = 'turning effects'
                case 'forces and matter' | 'force and matter':
                    subtopic = 'forces and matter'
                case 'energy transfer' | 'energy':
                    subtopic = 'energy transfer'
                case 'work and power' | 'work':
                    subtopic = 'work and power'
                case 'kinetic particle model of matter' | 'particle model':
                    subtopic = 'kinetic particle model of matter'
                case 'thermal properties' | 'thermal property':
                    subtopic = 'thermal properties'
                case 'thermal energy transfer' | 'thermal energy':
                    subtopic = 'thermal energy transfer'
                case 'sound':
                    subtopic = 'sound'
                case 'light':
                    subtopic = 'kinetic particle model of matter'
                case 'general properties of waves' | 'properties of waves' | 'waves':
                    subtopic = 'general properties of waves'
                case 'electromagnetic spectrum' | 'electromagnetic waves':
                    subtopic = 'electromagnetic spectrum'
                case 'magnetism' | 'magnet':
                    subtopic = 'magnetism'
                case 'static electricity' | 'static':
                    subtopic = 'static electricity'
                case 'electrical quantities':
                    subtopic = 'electrical quantities'
                case 'electrical circuit' | 'circuit':
                    subtopic = 'electrical circuit'
                case 'electromotive force' | 'emf':
                    subtopic = 'electromotive force'
                case 'electromagnetic induction' | 'induction':
                    subtopic = 'electromagnetic induction'
                case _:
                    subtopic = 'general' # quiz with all topics

            chosenTopic = subtopic
            
            for i in range(10):
                if qdata['physics'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['physics'][subtopic][i]
        case 'chemistry':
            # different topics in chemistry
            match topic:
                case 'states of matter' | 'state of matter':
                    subtopic = 'states of matter'
                case 'atomic structure' | 'atoms' | 'atom':
                    subtopic = 'atomic structure'
                case 'chemical bonding' | 'chemical bonds' | 'bonding' | 'bonds':
                    subtopic = 'chemical bonding'
                case 'chemical formulae and equations' | 'chemical formulae' | 'chemical equations' | 'chemical equation' | 'chemical formula' | 'formula' | 'equation':
                    subtopic = 'chemical formulae and equations'
                case 'chemical calculations' | 'calculations':
                    subtopic = 'chemical calculations'
                case 'electrochemistry':
                    subtopic = 'electrochemistry'
                case 'chemical energetics' | 'energetics':
                    subtopic = 'chemical energetics'
                case 'rates of reaction' | 'rate of reaction':
                    subtopic = 'rates of reaction'
                case 'reversible reactions' | 'reverse reactions' | 'reversible' | 'reverse':
                    subtopic = 'thermal properties'
                case 'redox reactions' | 'reduction' | 'oxidation' | 'redox':
                    subtopic = 'redox reactions'
                case 'acids and bases' | 'acids' | 'bases' | 'alkalis':
                    subtopic = 'acids and bases'
                case 'preperation of salts' | 'salts':
                    subtopic = 'preperation of salts'
                case 'periodic table' | 'elements':
                    subtopic = 'periodic table'
                case 'metallic elements' | 'metals':
                    subtopic = 'metallic elements'
                case 'reactivity series' | 'reactivity':
                    subtopic = 'reactivity series'
                case 'extraction and corrosion' | 'extraction':
                    subtopic = 'extraction and corrosion'
                case 'environment':
                    subtopic = 'environment'
                case 'organic chemistry' | 'organic compounds':
                    subtopic = 'organic chemistry'
                case 'experimental design' | 'experiment design' | 'paper 6':
                    subtopic = 'experimental design'
                case _:
                    subtopic = 'general' # quiz with all topics

            chosenTopic = subtopic
            
            for i in range(10):
                if qdata['chemistry'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['chemistry'][subtopic][i]
        case 'computer science':
            # different topics in computer science
            match topic:
                case 'data representation' | 'data':
                    subtopic = 'data representation'
                case 'data transmission' | 'error checking' | 'transmission':
                    subtopic = 'data transmission'
                case 'hardware':
                    subtopic = 'hardware'
                case 'software':
                    subtopic = 'software'
                case 'internet':
                    subtopic = 'internet'
                case 'automation' | 'automated technologies' | 'ai':
                    subtopic = 'automation'
                case 'algorithm design' | 'algorithm':
                    subtopic = 'algorithm design'
                case 'programming' | 'coding':
                    subtopic = 'programming'
                case 'databases' | 'database' | 'sql':
                    subtopic = 'databases'
                case 'boolean logic' | 'logic':
                    subtopic = 'boolean logic'
                case _:
                    subtopic = 'general' # quiz with all topics

            chosenTopic = subtopic
            
            for i in range(10):
                if qdata['computer science'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['computer science'][subtopic][i]
        case 'history':
            # different topics in computer science
            match topic:
                case 'early weimar germany' | 'early weimar' | '1918-23':
                    subtopic = 'Early Weimar Germany (1918-23)'
                case 'golden age weimar germany' | 'golden age weimar' | '1924-29':
                    subtopic = 'Golden Age Weimar Germany (1924-29)'
                case 'rise of the nazis' | 'early nazis':
                    subtopic = 'Rise of the Nazis'
                case 'nazi germany' | 'nazi rule' | '1933-45':
                    subtopic = 'Nazi Germany (1933-45)'
                case _:
                    subtopic = 'general' # quiz with all topics

            chosenTopic = subtopic
            
            for i in range(10):
                if qdata['history'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['history'][subtopic][i]
        case 'example': # example for testing
            for i in range(10):
                multiplechoice[i] = qdata['example'][i]
    
def mcq():
    """multiple choice questions"""
    dotdotdot()

    mcqTotal = 0 # resets total

    for i in range(mcqLength):
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

        # displays question # with length of MCQ shown
        print('Question ' + str(i + 1) + ' out of ' + str(mcqLength))
        print('')

        # asks question
        print(str(question) + '?')
        print('')

        # try to display image 
        try:
            imagePath = multiplechoice[i][6]
            img = Image.open(imagePath)
            img.show()
        except:
            pass
            

        # asks user to pick an option
        print('Choose one option:')
        print('1 : ' + str(answerA))
        print('2 : ' + str(answerB))
        print('3 : ' + str(answerC))
        print('4 : ' + str(answerD))
        print('')
        userAnswer = input('~~> ').strip()
        userAnswerNum = 0

        # if users type a word instead of a number, userAnswerNum set to 0
        try:
            userAnswerNum = int(userAnswer)
        except:
            userAnswerNum = 0
        
        correctAnswerText = str(multiplechoice[i][correctAnswer])

        if userAnswerNum == correctAnswer or userAnswer.lower() == correctAnswerText.lower():
            print('You got it right!')
            mcqTotal += 1
        else:
            # tells user correct answer
            print('You got it wrong!\nThe actual answer was: ' + str(correctAnswer) + ' (' + correctAnswerText + ')')
        
        dotdotdot()

    # displays chosen subject and topic
    print('Subject:\t' + chosenSubject)
    print('Topic:  \t' + chosenTopic)
    print('')

    # sets bar fill, score message, and mark based on score
    if mcqLength == 5:
        # scales score by 2
        # e.g. 2/5 = 4/10, 5/5 = 10/10

        barFill = '⣿' * (mcqTotal * 2) # amount of ⣿ is score * 2
        barSpaces = ' ' * (10 - (mcqTotal * 2)) # amount of spaces is 10 - score * 2

        scoremsg = mcqMessages[mcqTotal * 2][random.randrange(0, 5)]
        mark = mcqMessages[mcqTotal * 2][5]
    else:
        barFill = '⣿' * mcqTotal # amount of ⣿ is score
        barSpaces = ' ' * (10 - mcqTotal) # amount of spaces is 10 - score

        scoremsg = mcqMessages[mcqTotal][random.randrange(0, 5)]
        mark = mcqMessages[mcqTotal][5]
    
    # prints total score for user
    print('SCORE ~ ' + str(mcqTotal) + '/' + str(mcqLength) + '\tMARK ~ ' + mark)
    print('[' + barFill + barSpaces + ']')
    print('')
    print(' > ' + scoremsg)
    print('')
    input('~~> ')

    dotdotdot()

def structured():
    """structured questions"""
    pass
    # read essay text file and send to teacher for marking? (longer essay-style questions)
    # type into quiz program and get marks based on keywords? (shorter  questions only)

def call_error(param, errorType='none'):
    dotdotdot()

    # something went wrong (Fire Font-k)
    print('')                                                                                                             
    print('                           )    )                                           )                                   ')
    print('             )      (   ( /( ( /( (          (  (    (  (      (         ( /(   (  (    (                (  (   ')
    print(' (    (     (      ))\\  )\\()))\\()))\\   (     )\\))(   )\\))(    ))\\  (     )\\())  )\\))(   )(    (    (     )\\))(  ')
    print(' )\\   )\\    )\\  \' /((_)(_))/((_)\\((_)  )\\ ) ((_))\\  ((_)()\\  /((_) )\\ ) (_))/  ((_)()\\ (()\\   )\\   )\\ ) ((_))\\  ')
    print('((_) ((_) _((_)) (_))  | |_ | |(_)(_) _(_/(  (()(_) _(()((_)(_))  _(_/( | |_   _(()((_) ((_) ((_) _(_/(  (()(_) ')
    print('(_-</ _ \\| \'  \\()/ -_) |  _|| \' \\ | || \' \\))/ _` |  \\ V  V // -_)| \' \\))|  _|  \\ V  V /| \'_|/ _ \\| \' \\))/ _` |  ')
    print('/__/\\___/|_|_|_| \\___|  \\__||_||_||_||_||_| \\__, |   \\_/\\_/ \\___||_||_|  \\__|   \\_/\\_/ |_|  \\___/|_||_| \\__, |  ')
    print('                                            |___/                                                       |___/   ')
    print('')

    if errorType == 'subject':
        print('"' + param + '" is not a valid subject. Please try again.')
    elif errorType == 'does_not_exist':
        print('"' + param + '" does not exist yet. Please try again later.')
    else:
        print('"' + param + '" is not a valid input. Please try again.')
    print('')
    input('~~> ')

    dotdotdot()

def test():
    global chosenSubject
    global chosenTopic

    dotdotdot()

    # choose subject to study
    print('Select a subject to study:')
    print('')
    for i in subjects: # dynamic amount of subjects
        print('~ ' + i)
    print('')
    userSubject = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    userTopic = 'none'

    userHasTopic = False
    subjectError = False    

    # checks whether subject is included in hasTopics list
    try:
        if hasTopics[userSubject]:
            chosenSubject = userSubject
            userHasTopic = True
        else:
            chosenSubject = userSubject
    except:
        # if not in the hasTopics list, check if it is included in hasTopicsAbbrv list
        try:
            if hasTopicsAbbrv[userSubject]: # ask for topic if subject has them
                chosenSubject = abbrvDef[userSubject] # sets chosenSubject to non-abbreviated form
                userHasTopic = True
            else:
                chosenSubject = abbrvDef[userSubject] # sets chosenSubject to non-abbreviated form
        except:
            # calls error if subject is invalid
            subjectError = True

    if userHasTopic:
        # choose topic to study
        print('')
        print('Select a topic to study:')
        print('')
        for i in topics[chosenSubject]: # dynamic amount of subjects
            print('~ ' + i) # prints subjects as a list
        print('')
        userTopic = input('~~> ').lower()  # sets answer as lowercase to avoid miscasing

        set_subject(chosenSubject, userTopic)
    else:
        set_subject(chosenSubject)
        chosenTopic = 'N/A'
    
    if subjectError:
        call_error(userSubject, 'subject')
    else:
        mcq()
        structured()

while True:
    # Revisionio (Big Money-se)
    print(' _______                       __            __                      __           ')
    print('|       \\                     |  \\          |  \\                    |  \\          ')
    print('| $$$$$$$\\  ______  __     __  \\$$  _______  \\$$  ______   _______   \\$$  ______  ')
    print('| $$__| $$ /      \\|  \\   /  \\|  \\ /       \\|  \\ /      \\ |       \\ |  \\ /      \\ ')
    print('| $$    $$|  $$$$$$\\\\$$\\ /  $$| $$|  $$$$$$$| $$|  $$$$$$\\| $$$$$$$\\| $$|  $$$$$$\\')
    print('| $$$$$$$\\| $$    $$ \\$$\\  $$ | $$ \\$$    \\ | $$| $$  | $$| $$  | $$| $$| $$  | $$')
    print('| $$  | $$| $$$$$$$$  \\$$ $$  | $$ _\\$$$$$$\\| $$| $$__/ $$| $$  | $$| $$| $$__/ $$')
    print('| $$  | $$ \\$$     \\   \\$$$   | $$|       $$| $$ \\$$    $$| $$  | $$| $$ \\$$    $$')
    print(' \\$$   \\$$  \\$$$$$$$    \\$     \\$$ \\$$$$$$$  \\$$  \\$$$$$$  \\$$   \\$$ \\$$  \\$$$$$$ ')
    print('')                                                                              
    # made by sbird (Small Slant)
    print('                 __      __              __   _        __')
    print('  __ _  ___ ____/ /__   / /  __ __  ___ / /  (_)______/ /')
    print(' /  \' \\/ _ `/ _  / -_) / _ \\/ // / (_-</ _ \\/ / __/ _  / ')
    print('/_/_/_/\\_,_/\\_,_/\\__/ /_.__/\\_, / /___/_.__/_/_/  \\_,_/  ')
    print('                           /___/                         ')
    print('')
                                                                                                                                                                                                                                                                                         
    # choose subject to study
    print('What would you like to do?')
    print('')
    print('~ test')
    print('~ settings')
    print('~ quit')
    print('')
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing

    match userAction:
        case 'test' | 'tests' | 't':
            test()
        case 'settings' | 'setting' | 's':
            call_error(userAction, 'does_not_exist') # settings page does not exist yet
        case 'quit' | 't':
            sys.exit(0)
        case _: # invalid input
            call_error(userAction)

