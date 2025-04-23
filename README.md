# revisionio 📝

![main menu](/screenshots/screenshot-main-menu-1.png)

# ⚠️ PROJECT MOVED TO CODEBERG ⚠️

https://codeberg.org/sperchingbird/quiz

This repository has been archived and will not receive further commits. Please go to the Codeberg repo!

--------------------------------------------------------------------------------------------------------

a very simple program I made so you can do some multiple choice questions on various subjects and topics

## What is it? 

revisionio is a text-based program where you can revise subjects by doing simple multiple-choice questions. It currently includes most of my IGCSE elective subjects

## How To Run 🏃

You can run revisionio using two methods:

- Download exe produced by pyinstaller from the releases page
- Download the source code and run the Python file

⚠️ **NOTE: DATA FOLDER IS REQUIRED FOR REVISIONIO TO RUN, PLEASE DO NOT MODIFY OR DELETE IT** ⚠️
> the data folder must be in the same directory as the exe!

## Feature List 

- ability to select different subjects and topics

![subject and topic selection](/screenshots/screenshot-subject-topic-selection-1.png)

- shows you correct answer for a few seconds (default: 3) if you get a question wrong

![correct answer](/screenshots/screenshot-correct-answer.png)
![incorrect answer](/screenshots/screenshot-incorrect-answer.png)

- pop-up images using your default image viewer
  - useful for physics and chemistry questions that require diagrams

![question with image](/screenshots/screenshot-question-image.png)

- different messages appear depending on your score

![very bad score](/screenshots/screenshot-score-fail.png)
![bad score](/screenshots/screenshot-score-poor.png)
![really good score](/screenshots/screenshot-score-amazing-2.png)

- records your previous score for each topic
- records your personal best for each topic
- settings to customise revisionio
  - change how long answer is shown in seconds (default: 3)
  - change input selector (default: '~~>')
  - toggle sfx (default: off)
  - toggle whether previous score is saved (default: on)
    - you could turn this off if you find being reminded of your previous score a bit annoying
    - note: personal best score is always saved

![settings page](/screenshots/screenshot-settings-page.png)

### Buggy 🐛

- sound effects (generated using sfxr)
  - for some reason playing sfx crashes the program randomly, so it's disabled by default

### to be added

- short answer questions (i.e. single word or phrase)
- structured questions (i.e. essay)
- more score messages
- ability to adjust wackiness of score messages (professional -> insane)
- additional revision tools?

## Included Subjects

- physics 🧲
- chemistry 🧪
- computer science 💻
- history 📜

### in progress

- geography 🌍
