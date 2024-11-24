import time
import os
import json
import random
import sys

from PIL import Image

#* SETS MCQ QUESTIONS ARRAY *#
w, h = 7, 10 # width and height of list

# [subject][topic][0] = question
# [subject][topic][1-4] = answers a to d
# [subject][topic][5] = correct answer (1-4)
# [subject][topic][6] = whether question contains image (0 or 1, default is 0)

multiplechoice = [[0 for x in range(w)] for y in range(h)] # sets list full of 0s

#* SETS TOPIC DATA FROM JSON FILE *#
with open('topics.json', 'r') as f:
    tdata = json.load(f)

subjects = tdata['subjects'] # lists of subjects
topics = tdata['topics'] # list of topics per subject
hasTopics = tdata['hasTopics'] # for checking whether each subject has topics
hasTopicsAbbrv = tdata['hasTopicsAbbrv'] # for checking whether each abbrv subject has topics
abbrvDef = tdata['abbrvDef'] # for converting abbrv subjects to full name

endSignal = ["ENDHERE", "A", "B", "C", "D", -1]

# sets questions and answers based on subject and topic
def set_subject(subject='example', topic='none'):
    """sets questions and answers based on subject and topic"""
    global chosenTopic
    global mcqLength
    global topicError

    # loads JSON file data containing all questions
    with open('mcq.json', 'r', encoding="utf8") as f:
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
                    topicError = True
                    call_error(topic, 'topic')
                    return

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
                case 'thermal properties' | 'thermal property' | 'thermal' | 'heat':
                    subtopic = 'thermal properties'
                case 'sound':
                    subtopic = 'sound'
                case 'light':
                    subtopic = 'kinetic particle model of matter'
                case 'electromagnetic spectrum' | 'electromagnetic waves' | 'general properties of waves' | 'properties of waves' | 'waves':
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
                    topicError = True
                    call_error(topic, 'topic')
                    return

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
                case _:
                    topicError = True
                    call_error(topic, 'topic')
                    return

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
                    topicError = True
                    call_error(topic, 'topic')
                    return

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
                case 'life in nazi germany' | 'life in nazi rule' | 'life in nazi':
                    subtopic = 'Life in Nazi Germany'
                case _:
                    topicError = True
                    call_error(topic, 'topic')
                    return

            chosenTopic = subtopic
            
            for i in range(10):
                if qdata['history'][subtopic][i] == endSignal:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['history'][subtopic][i]
        case 'example': # for testing
            for i in range(10):
                multiplechoice[i] = qdata['example'][i]


#* SETS SCORE MESSAGES FROM JSON FILE *#
# mcq[score][0-4] = 5 score messages per possible score

with open('messages.json', 'r', encoding="utf8") as f:
    sdata = json.load(f)
mcqMessages = sdata['mcq']


#* SETS SETTINGS FROM JSON FILE *#
# [n] = nth setting 

def read_setting(param):
    """reads setting from json file"""

    with open('settings.json', 'r', encoding="utf8") as f:
        settingsdata = json.load(f)
    return settingsdata[param]

def set_setting(param, data):
    """writes new setting to json file"""

    with open('settings.json', 'r', encoding="utf8") as f:
        settingsdata = json.load(f)
    
    settingsdata[param] = data

    with open('settings.json', 'w', encoding='utf-8') as f:
        json.dump(settingsdata, f, ensure_ascii=False, indent=4)


#* SETS PAST SCORES FROM JSON FILE *#
# [subject][topic][0] = whether topic has been tested before (0 or 1)
# [subject][topic][1] = past score (0-10)

def view_past_score(subject, topic='none'):
    """reads setting from json file"""

    with open('past_scores.json', 'r', encoding="utf8") as f:
        scoredata = json.load(f)
    
    try:
        return scoredata[subject][topic]
    except:
        return scoredata[subject]

def set_past_score(subject, score=0, topic='none'):
    """writes new setting to json file"""

    with open('past_scores.json', 'r', encoding="utf8") as f:
        scoredata = json.load(f)
    
    try:
        scoredata[subject][topic] = score
    except:
        scoredata[subject] = score

    with open('past_scores.json', 'w', encoding='utf-8') as f:
        json.dump(scoredata, f, ensure_ascii=False, indent=4)


#* DECLARES GLOBAL VARIABLES *#
chosenSubject, chosenTopic = 'none', 'none'
mcqLength, mcqTotal = 10, 0


#* DECLARES ERROR FLAGS *#
topicError = False


#* DECLARES FUNCTIONS *#
def dotdotdot(length=1):
    """small loading screen"""

    for dot in range(2): # repeats twice
        print('.', end='', flush=True) # no new line after each dot
        time.sleep(.5) # small delay between each dot
    print('.')
    time.sleep(length) # longer delay after last dot
    print('\033c', end='') # clear terminal

def call_error(param, errorType='none'):
    """error message"""

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
    if errorType == 'topic':
        print('"' + param + '" is not a valid topic. Please try again.')
    elif errorType == 'does_not_exist':
        print('"' + param + '" does not exist yet. Please try again later.')
    else:
        print('"' + param + '" is not a valid input. Please try again.')
    print('')
    input('~~> ')

    dotdotdot()


#* DECLARES QUIZ COMPONENTS *#
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
            if multiplechoice[i][6]:
                imagePath = './images/' + chosenSubject + '/' + chosenTopic + '/q' + str(i + 1) + '.png' 
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
        
        dotdotdot(3)

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


#* PROGRAM *#
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

            topicError = False

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
            elif not topicError: # does not run test if invalid topic
                mcq()
                # structured()
        case 'settings' | 'setting' | 's':
            call_error(userAction, 'does_not_exist') # settings page does not exist yet
        case 'quit' | 't':
            sys.exit(0)
        case _: # invalid input
            call_error(userAction)
