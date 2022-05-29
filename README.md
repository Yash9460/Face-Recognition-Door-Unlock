# Microsoft-engage22

![language](https://img.shields.io/badge/-Microsoft%20Engage%2022-bluevoilet)
![language](https://img.shields.io/github/languages/top/Yash9460/Mentorsoft-engage22?style=for-the-badge)
![language](https://img.shields.io/github/last-commit/Yash9460/Mentorsoft-engage22?style=for-the-badge)


This project is being developed for Microsoft Engage 2022 mentorship program. This is a Facial Recognition Project


It is currently hosted on heroku.



Watch video demo <a href = "https://youtu.be/F9h0vMX6oZc" target = "_blank">here</a>

## Goals

- The main goal of this project is for security by face recognition. This can be beneficial for society, including increasing safety and security, preventing crimes, and reducing human interaction. 
- Also this app has a voice bot which will open only when the app is unlocked after recognizing the user's face.
- This voice bot (named "Jarvis") is an ai personal assistant that can perform various task by taking voice commands by users like if user says "Open Google", then it can execute the command and opens the Google Chrome and if user says "Search {Anything} on Google" then this app will search that thing and give the results to the user.

## High level design

- I have designed this app by following way :- 
    
    1. I have used harrcasscade classifier algorithm for my module
    2. First, when the user will click on capture button of the web app, the capture script of python will run and it will capture some set of images as sample to recognise
    3. Second, in the training script of model, the jpeg images converted into numpy array in form of integer and the model got trained
    4. After training the model, when the user clicks on unlock button, the face unlock script of python will run and if the user matches with the captured images then the app will be unlocked, and Jarvis greet to the user and asking for the commands to execute.

## Implementation details

- Collect training data

    First, the capture script of python will run and it will capture some set of images as sample to recognise

- Train the model 

     In the training script of model, the jpeg images converted into numpy array in form of integer and the model got trained
     we need to train the software by inserting new pictures into the database. The system will be able to learn and identify images of faces and can then compare them      with other images that we haven’t trained it with.

     To build a good system, we need to start by taking a picture of a person’s face. Then extracting the most important facial features like the eyes, nose, mouth,        and eyebrows.

     We can extract various data points such as distance between specific points on the face or angles of the face etc., which are important for identifying different      faces.

- Testing of software

     In this phase, it recognizing faces when it is in “live” mode (recognizing faces when they are in real-time). 
     If the face matches with the dataset, then app will be unlocked otherwise app will locked

## Learning / Challenges

- While deploying, I have learnt various types of datasets, error resolving and learn more about the APIs.

- Although the most challenging part is to converting the jpeg images into numpy integer arrays while training the model and also implementation of python script into frontend web application.

## Tech Stack:

- OpenCV
- Machine learning
- Streamlit
- Html/CSS
- Python
- Git


## Features:

- Face unlock system
- Jarvis ("Personal desktop assisstant")
- Providing Security
- Preventing crimes

#### If you like it please give it a star!! ⭐
