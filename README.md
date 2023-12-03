# Habit Tracker

Welcome to my Habit Tracker, a Python-based terminal application allowing users to create, track and view habits to promote a healthier lifestyle.<br>
You can access the live application [here!](https://habit-tracker-tb-f3dc632b7d99.herokuapp.com/)

## Contents
- [Site Goals](#site-goals)
    - [Project Goals](#project-goals)
    - [Project Outcomes](#project-outcomes)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Expectations](#user-expectations)
    - [User Stories](#user-stories)
- [Logic Flow](#logic-flow)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Technologies](#technologies)
    - [Libraries](#libraries)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

<br>

### Site Goals

#### Project Goals

#### Project Outcomes

### User Experience

#### Target Audience

#### User Expectations

#### User Stories

### Logic Flow

### Features

### Future Enhancements

### Technologies

The main technologies I have utilised within this project include:<br>
1. Heroku- The project has been deployed on Heroku. See [Deployment](#deployment) to see the guide for deployment.
2. Code Anywhere- I have used CodeAnywhere as the IDE to edit and push changes  for the project.
3. Python- This project has been written using the Python language.
4. JavaScript- The script required to run the Code Institute mock terminal is done using JavaScript
5. Google Cloud- In order to enable the API's required for this project I have used Google Cloud.
6. Google Sheets- Storage of the data used within this project is contained within a Google Sheets worksheet.
7. Github- After code has been pushed it has been stored within Github.
8. ChatGPT 3.5- To assist with debugging I have utilised the [open.AI ChatGPT](https://openai.com/blog/chatgpt) model.
9. Visual Paradigm- I have used this website to create the flowchart for my project. Click [here](#logic-flow) to view the flowchart.

#### Libraries

The following Libraries have been imported for this project:<br>
1. gspread - This library is used to link the program to Google Sheets where the main data has been stored.
2. questionary - This library is used to create an aesthetically pleasing and user friendly command line interface
3. os - This library is used to create a function to clear the terminal thereby reducing the clutter on screen for a better user experience, taking into account the operating system being used by the user.
4. bcrypt - This library has been used to encrypt the password data provided by a user, offering additional security for the user data.
5. datetime - This library has been used to allow the program to pull the current date for the user interaction which is used when logging and viewing tracked habits.
6. re - This library (which stands for regular expressions) has been used when validating usernames and passwords to ensure the user input matches the requirements set out in the validation functions.
7. time - This library has been used to create a time delay prior to clearing the terminal so the user can see any printed messages applicable for their actions.

### Testing

### Deployment

### Credits

#### Resources

Given the complexity of this project I have made use of a number of resources to help me bring my ideas to life.

1. [Questionary](https://questionary.readthedocs.io/en/stable/pages/quickstart.html#quickstart) - I have used this guidance to learn how to first install and import the questionary library, and then to also understand how to best include the library functions within my own project code.
2. [W3Schools- datetime](https://www.w3schools.com/python/python_datetime.asp) - I have used this guidance to learn how to import and make use of the datetime library required to pull the current date the application is being used, and to pull data for specific date periods as required by a user.
3. [GitHub- Password Storage](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md#argon2id) - When deciding which library to use for the encryption of passwords I referred to this guidance. This allowed me to consider the differences between the current known libraries (bcrypt, argan2 and scrpyt) and how they would benefit my project. Given the scope of the project, whilst it is acknowledged that argan2 appears to be the better algorithms, I felt it would be better to make use of the bcrypt library which required less hashing time and has had more history of testing with other developers.
4. [Pypi- bcrypt](https://pypi.org/project/bcrypt/) - Once I had made the decision to use the bcyrpt enscryption library, I have referred to this guidance to assist in writing the code I needed to encrypt the passwords input by a user.
5. [W3Resource- Validations](https://www.w3resource.com/python-exercises/python-conditional-exercise-15.php) - Towards the end of the project I decided I wanted to also include a validation function for both the username and password a user can use. This guidance helped me to understand the logic that would be required when validating a password, which I was then able to use as a reference point to also validate the username input.
6. [Scaler- Clear Screen](https://www.scaler.com/topics/how-to-clear-screen-in-python/) - I have made use of this guidance when creating the functions to clear the terminal screen at certain stages within the project, whilst also applying a time delay so that any printed messages can still be read by a user before the terminal is cleared.

#### Acknowledgements

I would like to thank my mentor Luke who has continued to help me with my coding journey, offering constructive feedback to make the most of my new skills in learning Python.<br>

I also want to thank Sherry_lead on slack who stepped in when I was first starting this project and facing a mental barrier to get started. Working with Sherry helped me to get over the intiial barier as a result of an incompatable keyboard library I was trying to use. Her encouragement and support were instrumental in inspiring me to get started with this project.<br>

Lastly I would like to thank the Slack community as a whole with Code Institute, who are always ready to offer a helping hand or words of encouragement whilst on this learning journey.