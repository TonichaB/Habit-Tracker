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

#### Future Enhancements

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

### Bugs

### Deployment

The following sections explain how this project has been deployed.

#### Version Control

I have created this project using the Code Anywhere IDE with all changes being pushed to the github repository named 'Habit_Tracker'.<br>

The following git commands have been utilised throughout the development process in order to push changes to the above mentioned respository: <br>

- git add - This command will add the file(s) to the staging area before they are commited to the local repository.
- git commit -m "message" - This command commits any changes to the local repository queue in readiness to be pushed. Details of the changes made will replace the "message" section of the command.
- git push - This is the final command used to push all committed entries to the repository on github.

#### Local Cloning

In order to clone this repository to be used locally please follow these steps:<br>

1.  At the top of this page select *<> Clone* to open the drop down menu, and make sure that *HTTPS* is selected.
2. Copy the repository link shown to the clipboard.
3. Open your IDE of choice (**git must be installed**).
4. Type the following into the IDE terminal: 'git clone *paste the copied git url*' <br>

The project will now be cloned to your local machine for use. If you wish to run the project within your terminal run the following command: '*python run.py*'

#### Google Sheets Set Up

#### Heroku Deployment

This project has been deployed to [Heroku](), this being a Platform as a Service (PaaS). This enables developers the ability to build, run and operate applications in the cloud as is required as per the [Project Goals](#project-goals) for this project.<br>

In order to deploy the project you must follow these steps: <br>

1. First ensure you have logged in, or signed up for an account with Heroku. Once logged in you can continue to follow the next steps.
2. From the Dashboard page you will need to select *New* located in the top-right corner. From here select *Create new app* from the drop down menu.
3. You will be asked to create a name for the application. All application names must be unique accross the entire Heroku network, for example I have used 'habit-tracker-tb' as this represents the project name for easy reference, alongside my initials. Once you have created your name you can confirm the primary language used as *Python*. Lastly you will need to choose a region closest to you (EU or USA), and then you can select *Create App*.
4. We now need to amend the settings, specially the environment variables, to allow the application to run correctly once deployed. Go to the *Settings* tab and then *Reveal Config Vars*. You will see two input boxes, the first for KEY and a second for VALUE. The following variables will need to be added:<br>
    - KEY = PORT , VALUE = 8000
    - KEY = CREDS , VALUE = *Here you will need to copy and paste the contents of the creds.json file you have created in the [Google Sheets Set Up](#google-sheets-set-up) section above*
Once the above has been updated, select *Add*
5. After adding the above variables, scroll down to *Buildpacks* and select *Add buildpack*. Heroku will give you a few options you can select from using their officially supported packs, for this project we will need the *python* and *node.js* packs. The order in which you show the buildpacks is important. **For this reason make sure to select Python first, and then Node.js.** Don't worry if you get these wrong, after adding you can drag the packs to rearrange their order. Don't forget to click *Save Changes*.
6. Now that we have set up the variables, and added our buildpacks we can start the process of deploying the project. Go back to the top of the page and select the *Deploy* tab. Go to the *Deployment Method* section and select *GitHub*, where you can then select to *Connect to GitHub*. You will need to search for the repository name in the repo-name section and select *Connect* once the correct repository has been found. **Go back to [Local Cloning](#local-cloning) if you have not already cloned the GitHub repository.**
7. We are now ready to deploy, so scroll down the page until you see *Manual Deploys* where you will want to select *Deploy Branch*. This will now start to create the application being deployed- this can take some time so please be patient! When ready you will see an option to *View* which will open the deployed project in a new tab showing the project within a mock terminal.<br>

If you have followed all above steps correctly the project will now be connected and deployed to Heroku.

### Credits

Within this section I have noted the resources used when building the project, and acknowledgements towards those who have supported me in the journey.

#### Resources

Given the complexity of this project I have made use of a number of resources to help me bring my ideas to life.

1. [Questionary](https://questionary.readthedocs.io/en/stable/pages/quickstart.html#quickstart) - I have used this guidance to learn how to first install and import the questionary library, and then to also understand how to best include the library functions within my own project code.
2. [W3Schools- datetime](https://www.w3schools.com/python/python_datetime.asp) - I have used this guidance to learn how to import and make use of the datetime library required to pull the current date the application is being used, and to pull data for specific date periods as required by a user.
3. [GitHub- Password Storage](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md#argon2id) - When deciding which library to use for the encryption of passwords I referred to this guidance. This allowed me to consider the differences between the current known libraries (bcrypt, argan2 and scrpyt) and how they would benefit my project. Given the scope of the project, whilst it is acknowledged that argan2 appears to be the better algorithms, I felt it would be better to make use of the bcrypt library which required less hashing time and has had more history of testing with other developers.
4. [Pypi- bcrypt](https://pypi.org/project/bcrypt/) - Once I had made the decision to use the bcyrpt enscryption library, I have referred to this guidance to assist in writing the code I needed to encrypt the passwords input by a user.
5. [W3Resource- Validations](https://www.w3resource.com/python-exercises/python-conditional-exercise-15.php) - Towards the end of the project I decided I wanted to also include a validation function for both the username and password a user can use. This guidance helped me to understand the logic that would be required when validating a password, which I was then able to use as a reference point to also validate the username input.
6. [Scaler- Clear Screen](https://www.scaler.com/topics/how-to-clear-screen-in-python/) - I have made use of this guidance when creating the functions to clear the terminal screen at certain stages within the project, whilst also applying a time delay so that any printed messages can still be read by a user before the terminal is cleared.
7. [gspread directory](https://docs.gspread.org/en/latest/oauth2.html) - When running my code, I noticed a deprication warning would appear to note "client_factory will be replaced by gspread.hhtp_client types". I have used this guidance to determine the reason for this warning, which appears to relate to the version of gspread being used which utilises 'oauth2client' which has since been deprecated by Google in favour of 'google-auth'. I have referred to this warning in the above section for [Bugs](#bugs) to note how I have chosen to address this.
8. [Stack Overflow- Deprication Warnings](https://stackoverflow.com/questions/879173/how-to-ignore-deprecation-warnings-in-python) - I have referred to this guidance when trying to resolve the deprecation warning as noted above. Please see the [Bugs](#bugs) section for further details on the method chosen.

#### Acknowledgements

I would like to thank my mentor Luke who has continued to help me with my coding journey, offering constructive feedback to make the most of my new skills in learning Python.<br>

I also want to thank Sherry_lead on slack who stepped in when I was first starting this project and facing a mental barrier to get started. Working with Sherry helped me to get over the intiial barier as a result of an incompatable keyboard library I was trying to use. Her encouragement and support were instrumental in inspiring me to get started with this project.<br>

Lastly I would like to thank the Slack community as a whole with Code Institute, who are always ready to offer a helping hand or words of encouragement whilst on this learning journey.