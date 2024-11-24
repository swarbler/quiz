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
with open('./data/topics.json', 'r') as f:
    topicData = json.load(f)

SUBJECTS = topicData['subjects'] # lists of subjects
TOPICS = topicData['topics'] # list of topics per subject
HAS_TOPICS = topicData['hasTopics'] # for checking whether each subject has topics
HAS_TOPICS_ABBRV = topicData['hasTopicsAbbrv'] # for checking whether each abbrv subject has topics
ABBRV_DEF = topicData['abbrvDef'] # for converting abbrv subjects to full name

END_SIGNAL = ["ENDHERE", "A", "B", "C", "D", -1]

# sets questions and answers based on subject and topic
def set_subject(subject='example', topic='none'):
    """sets questions and answers based on subject and topic"""
    global chosenTopic, mcqLength, topicError

    # loads JSON file data containing all questions
    with open('./data/mcq.json', 'r', encoding="utf8") as f:
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
                if qdata['geography'][subtopic][i] == END_SIGNAL:
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
                if qdata['physics'][subtopic][i] == END_SIGNAL:
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
                if qdata['chemistry'][subtopic][i] == END_SIGNAL:
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
                if qdata['computer science'][subtopic][i] == END_SIGNAL:
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
                if qdata['history'][subtopic][i] == END_SIGNAL:
                    mcqLength = i
                    return
                multiplechoice[i] = qdata['history'][subtopic][i]
        case 'example': # for testing
            for i in range(10):
                multiplechoice[i] = qdata['example'][i]


#* SETS SCORE MESSAGES FROM JSON FILE *#
# mcq[score][0-4] = 5 score messages per possible score

with open('./data/messages.json', 'r', encoding="utf8") as f:
    messageData = json.load(f)
MCQ_MESSAGES = messageData['mcq']


#* SETS SETTINGS FROM JSON FILE *#
# [setting] = setting

def read_setting(param):
    """reads setting from json file"""

    with open('./data/settings.json', 'r', encoding="utf8") as f:
        settingsdata = json.load(f)
    return settingsdata[param]

def set_setting(param, data):
    """writes new setting to json file"""

    with open('./data/settings.json', 'r', encoding="utf8") as f:
        settingsdata = json.load(f)
    
    settingsdata[param] = data

    with open('./data/settings.json', 'w', encoding='utf-8') as f:
        json.dump(settingsdata, f, ensure_ascii=False, indent=4)


#* SETS PAST SCORES FROM JSON FILE *#
# past_scores.json
# [subject][topic][0] = whether topic has been tested before (0 or 1)
# [subject][topic][1] = past score (0-10)

# top_scores.json
# [subject][topic][0] = whether topic has been tested before (0 or 1)
# [subject][topic][1] = personal best (0-10)

def read_score(subject, filePath='./data/past_scores.json', topic='none'):
    """reads score from json file"""

    with open(filePath, 'r', encoding="utf8") as f:
        scoredata = json.load(f)
    
    try:
        return scoredata[subject][topic]
    except:
        return scoredata[subject]

def set_past_score(subject, score=0, filePath='./data/past_scores.json', topic='none'):
    """writes new score to json file"""

    with open(filePath, 'r', encoding="utf8") as f:
        scoredata = json.load(f)
    
    try:
        scoredata[subject][topic] = score
    except:
        scoredata[subject] = score

    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(scoredata, f, ensure_ascii=False, indent=4)

def reset_score(filePath='./data/past_scores.json'):
    """resets score json file"""

    with open('./data/clean_scores.json', 'r', encoding="utf8") as f:
        cleanscoredata = json.load(f)

    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(cleanscoredata, f, ensure_ascii=False, indent=4)


#* DECLARES GLOBAL VARIABLES *#
chosenSubject, chosenTopic = 'none', 'none'
mcqLength, mcqTotal = 10, 0


#* DECLARES SETTINGS *#
viewLength = read_setting('questionViewLength')
selector = read_setting('inputSelector')
sfxEnabled = read_setting('soundEffects')
save = read_setting('savePreviousScores')


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

def showToggle(param=1):
    """shows either ON or OFF"""
    if param:
        return 'ON'
    else:
        return 'OFF'

def call_error(param, errorType='none', minR=0, maxR=0):
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

    match errorType:
        case 'subject':
            print('"' + param + '" is not a valid subject. Please try again.')
        case 'topic':
            print('"' + param + '" is not a valid topic. Please try again.')
        case 'does_not_exist':
            print('"' + param + '" does not exist yet. Please try again later.')
        case 'range':
            print('"' + param + '" is not a valid input. You must input a number between ' + str(minR) + ' and ' + str(maxR) + '. Please try again')
        case _:
            print('"' + param + '" is not a valid input. Please try again.')
    print('')
    input(selector)

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
        userAnswer = input(selector).strip()
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
        
        dotdotdot(viewLength)

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

        scoremsg = MCQ_MESSAGES[mcqTotal * 2][random.randrange(0, 5)]
        mark = MCQ_MESSAGES[mcqTotal * 2][5]
    else:
        barFill = '⣿' * mcqTotal # amount of ⣿ is score
        barSpaces = ' ' * (10 - mcqTotal) # amount of spaces is 10 - score

        scoremsg = MCQ_MESSAGES[mcqTotal][random.randrange(0, 5)]
        mark = MCQ_MESSAGES[mcqTotal][5]
    
    # prints total score
    print('SCORE ~ ' + str(mcqTotal) + '/' + str(mcqLength) + '\tMARK ~ ' + mark)
    print('[' + barFill + barSpaces + ']')
    print('')
    print(' > ' + scoremsg)
    print('')

    # prints previous score
    prevExists = read_score(chosenSubject, filePath='./data/past_scores.json', topic=chosenTopic)[0] # does not show previous score if does not exist
    prevScore = read_score(chosenSubject, filePath='./data/past_scores.json', topic=chosenTopic)[1]
    prevMark = MCQ_MESSAGES[prevScore][5]

    if prevExists and save: # checks whether savePreviousScores is true
        print('PREVIOUS SCORE ~ ' + str(prevScore) + '/' + str(mcqLength) + '\tPREVIOUS MARK ~ ' + prevMark)
        
        # message based on how current score compares with previous score
        if not prevScore and not mcqTotal:
            print(' > You got a zero again?')
        elif prevScore == mcqTotal:
            print(' > Consistent effort')
        elif prevScore * 2 == mcqTotal:
            print(' > You doubled your previous score!')
        elif prevScore * 3 == mcqTotal:
            print(' > You tripled your previous score!')
        elif prevScore < mcqTotal:
            print(' > You got a higher score than last time')
        elif prevScore > mcqTotal:
            print(' > You got a lower score than last time')
        print('')

    # prints personal best score
    pbExists = read_score(chosenSubject, './data/top_scores.json', chosenTopic)[0] # does not show personal best if does not exist
    pbScore = read_score(chosenSubject, './data/top_scores.json', chosenTopic)[1]
    pbMark = MCQ_MESSAGES[prevScore][5]

    # tells user if new personal best is made
    if pbExists:
        if pbScore >= mcqTotal:
            print('PERSONAL BEST ~ ' + str(pbScore) + '/' + str(mcqLength))
        else:
            print('OLD PERSONAL BEST ~ ' + str(pbScore) + '/' + str(mcqLength))
            print(' > New personal best!')
    else:
        print(' > New personal best!')
    print('')

    input(selector)

    # sets current score as previous score
    if save: # only saves previous score if setting is enabled
        set_past_score(chosenSubject, [1, mcqTotal], './data/past_scores.json', chosenTopic)
    
    # sets current score as personal best if higher than previous personal best
    if mcqTotal > pbScore:
        set_past_score(chosenSubject, [1, mcqTotal], './data/top_scores.json', chosenTopic)

    dotdotdot()

def structured():
    """structured questions"""

    pass
    # read essay text file and send to teacher for marking? (longer essay-style questions)
    # type into quiz program and get marks based on keywords? (shorter  questions only)

def setting_page():
    global viewLength, selector, sfxEnabled, save

    while True:
        # title text (Big Money-nw)
        print('                     $$\\     $$\\     $$\\                               ')
        print('                     $$ |    $$ |    \\__|                              ')
        print(' $$$$$$$\\  $$$$$$\\ $$$$$$\\ $$$$$$\\   $$\\ $$$$$$$\\   $$$$$$\\   $$$$$$$\\ ')
        print('$$  _____|$$  __$$\\\\_$$  _|\\_$$  _|  $$ |$$  __$$\\ $$  __$$\\ $$  _____|')
        print('\\$$$$$$\\  $$$$$$$$ | $$ |    $$ |    $$ |$$ |  $$ |$$ /  $$ |\\$$$$$$\\  ')
        print(' \\____$$\\ $$   ____| $$ |$$\\ $$ |$$\\ $$ |$$ |  $$ |$$ |  $$ | \\____$$\\ ')
        print('$$$$$$$  |\\$$$$$$$\\  \\$$$$  |\\$$$$  |$$ |$$ |  $$ |\\$$$$$$$ |$$$$$$$  |')
        print('\\_______/  \\_______|  \\____/  \\____/ \\__|\\__|  \\__| \\____$$ |\\_______/ ')
        print('                                                   $$\\   $$ |          ')
        print('                                                   \\$$$$$$  |          ')
        print('                                                    \\______/           ')
        print('')
                                                                                                                                                                                                                                                                                            
        # choose setting to change (or exit settings page)
        print('What would you like to do?')
        print('~ set duration answer is shown (' + str(viewLength) + ')')
        print('~ set input selector (' + selector.strip() + ')')
        print('~ toggle sound effects (' + showToggle(sfxEnabled) + ')')
        print('~ toggle whether previous scores are saved (' + showToggle(save) + ')')
        print('~ exit')
        print('')
        userAction = input(selector).lower().strip()

        match userAction:
            case 'set duration answer is shown' | 'set answer duration' | 'answer duration' | 'answer' | 'set wait duration' | 'wait duration' | 'set wait' | 'wait':
                userInput = input('Enter new duration (in seconds): ').strip()

                try:
                    if int(userInput) > 30 or int(userInput) <= 0:
                        call_error(userInput, 'range', 1, 30)
                    else:
                        set_setting('questionViewLength', int(userInput))
                        viewLength = read_setting('questionViewLength')

                        dotdotdot()
                except:
                    call_error(userInput)
            case 'set input selector' | 'set selector' | 'selector' | 'set input' | 'input':
                userInput = input('Enter new input selector: ').strip()

                set_setting('inputSelector', userInput + ' ')
                selector = read_setting('inputSelector')
                
                dotdotdot()
            case 'toggle sound effects' | 'sound effects' | 'sound effect' | 'togle sound' | 'sound' | 'toggle sfx' | 'sfx':
                if sfxEnabled:
                    set_setting('soundEffects', 0)
                else:
                    set_setting('soundEffects', 1)
                
                sfxEnabled = read_setting('soundEffects')
                
                dotdotdot()
            case 'toggle whether previous scores are saved' | 'toggle previous scores' | 'previous scores' | 'toggle previous score' | 'previous score' | 'toggle save' | 'save':
                if save:
                    set_setting('savePreviousScores', 0)
                else:
                    set_setting('savePreviousScores', 1)

                save = read_setting('savePreviousScores')
                
                dotdotdot()
            case 'exit' | 'e':
                dotdotdot(0)

                return
            case _: # invalid input
                call_error(userAction)


#* PROGRAM *#
while True:
    # title text (Big Money-se)
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
    print('|| made by sbird ||')
    print('')
                                                                                                                                                                                                                                                                                         
    # choose subject to study
    print('What would you like to do?')
    print('')
    print('~ test')
    print('~ settings')
    print('~ quit')
    print('')
    userAction = input(selector).lower() # sets answer as lowercase to avoid miscasing

    match userAction:
        case 'test' | 'tests' | 't':
            dotdotdot()

            # choose subject to study
            print('Select a subject to study:')
            print('')
            for i in SUBJECTS: # dynamic amount of subjects
                print('~ ' + i)
            print('')
            userSubject = input(selector).lower() # sets answer as lowercase to avoid miscasing
            userTopic = 'none'

            userHasTopic = False
            subjectError = False    

            # checks whether subject is included in hasTopics list
            try:
                if HAS_TOPICS[userSubject]:
                    chosenSubject = userSubject
                    userHasTopic = True
                else:
                    chosenSubject = userSubject
            except:
                # if not in the hasTopics list, check if it is included in hasTopicsAbbrv list
                try:
                    if HAS_TOPICS_ABBRV[userSubject]: # ask for topic if subject has them
                        chosenSubject = ABBRV_DEF[userSubject] # sets chosenSubject to non-abbreviated form
                        userHasTopic = True
                    else:
                        chosenSubject = ABBRV_DEF[userSubject] # sets chosenSubject to non-abbreviated form
                except:
                    # calls error if subject is invalid
                    subjectError = True

            topicError = False

            if userHasTopic:
                # choose topic to study
                print('')
                print('Select a topic to study:')
                print('')
                for i in TOPICS[chosenSubject]: # dynamic amount of subjects
                    print('~ ' + i) # prints subjects as a list
                print('')
                userTopic = input(selector).lower()  # sets answer as lowercase to avoid miscasing

                set_subject(chosenSubject, userTopic)
            else:
                set_subject(chosenSubject)
                chosenTopic = 'N/A'
            
            if subjectError:
                call_error(userSubject, 'subject')
            elif not topicError: # does not run test if invalid topic
                mcq()
                # structured()
        case 'settings' | 'setting' | 'set' | 's':
            dotdotdot(0)

            setting_page()
        case 'quit' | 'q':
            sys.exit(0)
        case _: # invalid input
           call_error(userAction)
