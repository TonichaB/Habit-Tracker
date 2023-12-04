# Habit Tracker

Welcome to my Habit Tracker, a Python-based terminal application allowing users to create, track and view habits to promote a healthier lifestyle.<br>
You can access the live application [here!](https://habit-tracker-tb-f3dc632b7d99.herokuapp.com/)

## Contents
- [Site Goals](#site-goals)
    - [Project Goals](#project-goals)
    - [Project Outcomes](#project-outcomes)
        - [Creation of a Data Model](#creation-of-a-data-model)
        - [Features](#features)
            - [Existing Features](#existing-features)
            - [Future Enhancements](#future-enhancements)
        - [User Options and Instructions](#user-options-and-instructions)
        - [Handling of User Input](#handling-of-user-input)
        - [Libraries Imported](#libraries-imported)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stores](#user-stories)
- [Logic Flow](#logic-flow)
- [Technologies](#technologies)
    - [Libraries](#libraries)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Local Cloning](#local-cloning)
    - [Google Sheets Set Up](#google-sheets-set-up)
    - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
    - [Resources](#resources)
    - [Acknowledgements](#acknowledgements)

<br>

### Site Goals

#### Project Goals

For this project, I had the following goals to be met:<br>

- Creation of a Data Model
- Features
- Handling of User Input
- User Options and Instructions
- Libraries Imported

#### Project Outcomes

The above mentioned Project Goals have been addressed as per the below.

##### Creation of a Data Model

Through the use of Google Sheets and the logic contained within the project code I have created a structured representation of the data and relationships. Each worksheet within the Google Sheet corresponds to a entity type, with the rows within the worksheets representing instances of those entities. The data model can be broken down as follows:<br>

1. User Accounts:<br>
There is a worksheet named 'user_accounts' that stores the user credentials (username and hashed password). Each row within this worksheet represents a user account.
2. Habits:<br>
There is a worksheet named 'habits_list' that stores the information about the habits (habit name and frequency). Each row wihtin this worksheet represents a habit, which is associated with a specific user.
3. Habit Log:<br>
There is a worksheet named 'habit_log' that stores the user habits (username, habit name, and date the habit was logged). Each row within this worksheet represents a instance of a logged habit.
4. Object-Oriented Design:<br>
By utilising classes for 'HabitTracker', 'HabitOperations', and 'Functions' I have been able to encapsulate the behaviour relating to the user operations, habits and general functions.

##### Features

###### Existing Features

Within this project I have included a number of features/functions that addressses a users expectations when interacting with the application. <br>

- Start Page- When the user starts the application they see a welcome statement and are presenting with the options to log in or register.<br>
![Start Up]()<br>
- Log In - If the user chooses to log in, they will be asked to enter their username and password which will be validated against the Google Sheet before allowing the user to proceed.<br>
![Log In]()<br>
- Register - If the user chooses to register an account, they will be asked to provide a new username and password which is then saved to the Google Sheet (so long as the requirements are met). The user is then also asked to confirm habits they would like to track using the Add New Habit function outlined further below.<br>
![Register]()<br>
- Main Menu - Once the user has logged in/ registered, they will be taken to the Main Menu with a list of options they can choose from.<br>
![Main Menu]()<br>
- Update Password - From the Main Menu, the user can select to update their password. When selected they will be asked to enter their old password, which is compared to the password saved to Google Sheets; if this matches the user can then input a new password which will replace the previously saved data. <br>
![Update Password]()<br>
- Add New Habit - From the Main Menu, the user can select to add a new habit which will be saved to the habits_list worksheet. The input will check to make sure the habit chosen hasn't already been saved within the worksheet to avoid duplications.<br>
![Add New Habit]()<br>
- Delete Habit - From the Main Menu, the user can select to delete a chosen habit. They will be asked to confirm the habit name and if this matches withing the habits_list worksheet the user is asked to confirm they are still happy to delete the habit. Once confirmed the data is removed from the worksheet.<br>
![Delete Habit]()<br>
- Change Habit Frequency - From the Main Menu, the user can select to change the frequency associated with a saved habit. They will need to input the habit name, and then will be asked to confirm the new frequency to be associated with this habit in the habits_list worksheet.<br>
![Change Habit Frequency]()<br>
- Log Today's Habits - From the Main Menu, the user can select to log their completed habits for the current date. This function will dsplay the saved habits specific for the current user, and will allow them to highlight their completed habits using the spacebar, and when they click enter the completed habits are confirmed and the habit_log worksheet is updated with the habit and date confirmed for the user.<br>
![Log Today's Habits]()<br>
- View Habits - From the Main Menu, the user can select the option to view habits, which will take them to a new option screen. This screen will give the user a choice to either view the completed habits for the current date, or to view the completed habits for a set time period.<br>
![View Habits]()<br>
- View Today's Habits - From the View Habits menu, the user can select to view the habits for the current date. This will present them with any habits currently saved to the habit_log worksheet, where the corresponding date saved matches the current date. <br>
![View Today's Habits]()<br>
- View Habits for a Selected Period - From the View Habits menu, the user can select to view completed habits that have been saved within a specified time period. The user will be asked to confirm a start and end date for the data to be filtered through. As long as the user has used the correct date format, the filtered habits will then be presented to the user before returning them to the Main Menu.<br>
![View Habit's for Selected Period]()<br>
- Log Out - From the Main Menu, the user can choose to log out of their account. If selected the user will return to the Start Up screen where they are asked again to either log in or register.
- Delete Account - From the Main Menu, the user can select the option to delete their account. If selected, the user is first asked to confirm they are sure they want to delete their account. If confirmed yes all saved details within the Google Sheet that is associated with that username will be deleted; if they confirm no the user is taken back to the Main Menu. <br>
![Delete Account]()<br>
- Quit - From the Main menu, the user can choose to exit the application altogether using the Quit option. When selected the user will see a message to confirm the application is quitting, following which the terminal will clear and the application will end.<br>
![Quit]()

###### Future Enhancements

Whilst I am happy with the current features within this project, with additional time I could include:<br>

- Habit Examples- If a user is struggling to think of a habit to track, a new function could include the ability to view examples of habits that other users have saved (making sure not to include the user details associated with the saved habit) that they could then select to track themselves.
- Fix Deprication Warning- Whilst for this project it was not necessary to fix the Deprication warning in relation to the gspread library, with more time I would refactor the code to utilise 'google-auth' over 'oauth2client'. Please see [Bugs](#bugs) below noting how I have chosen to address this in the meantime.

##### User Options and Instructions

So as to provide accessibility and a smooth user experience, whenever a user is presented with a question or input request they will be given instructions on how to action each step. This includes the following examples:<br>

- Text Input Required<br>
Throughout the application there are a few different functions that will require the user to type a response to a question presented. Whenever this occurs the user will be advised on any specific requirements for the text input to be provided.<br>
![Text Input Required]()
- Option Selection Required<br>
There are 4 occassions in this project where the user is presented with options to choose from (Log In/Register, Main Menu, View Habit Options and Log Today's Habits). For these functions the user will be advised to use their arrow keys to navigate the options, and to press enter to select.<br>
![Option Selection Required]()<br>
- Multiple Choice Selection<br>
When the user selects to log their habits for the current date, they will be presented with a list of the habits saved specifically for that user. They will be given instructions on how to navigate the options presented, how to select which option to log, how to toggle the options and how to invert the options.<br>
![Multiple Choice Selection]()<br>

##### Handling of User Input

Each time a user provides any form of input to the terminal, their response will be validated and the user will be informed whether their input has been successful or not. 

##### Libraries Imported

I have imported a number of libraries within this project to improve the overall functionality and user experience. Details for the specific libraries included are show [here](#libraries).

### User Experience

#### Target Audience

This project has been created for a target audience of young adults/adults from any background. In particular for users who would like to follow a healthier lifestyle by building up regular habits they are able to track daily.

#### User Stories

First Time User:<br>

> *"As a new user, I would like to register for a new account"*
>
> *"As a new user, I would like to create new habits to be tracked"*
>
> *"As a new user, I would like to receive directions on how to 
> navigate through the application"*
>
> *"As a new user, I have not used CLI before and would like to know
> my inputs are valid"*

Returning User:<br>

> *"As a returning user, I would like to log in using previously
> created credentials"*
>
> *"As a returning user, I would like to view my completed habits
> for a specific time period"*

All Users:<br>

> *"As a user, I would like to confirm my completed habits for the
> current date"*
>
> *"As a user, I would like the option to delete my account and all
> stored data associated with my account"*
>
> *"As a user, I would like the option to change my password"*

### Logic Flow

Given the complexity of this project I spend some time planning the logic required for the application to run efficiently and to give a general idea on how to best approach each stage. To do this I created a flowchart that mapped out each function that allowed me to follow the logic through the application as this was developed.<br>

As I worked through the project I would come up with new ideas for the logic flow and features to be included, and so the flowchart changed during the development process. Below shows the comparison for the initial flowchart created, and the final flowchart reflecting the current application.<br>

Initial Flowchart:<br>
![Initial Flowchart]()<br>

Final Flowchart:<br>
![Final Flowchart]()

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
9. Visual Paradigm- I have used this website to create the initial flowchart for my project. Click [here](#logic-flow) to view the flowchart.
10. [Mermaid.Live](https://mermaid.live/)- As the prject developed and became more complicated, I found this website beneficial. With the assistance of ChatGPT I was able to convert my code into mermaid.js syntax, and when pasting this to the above site a flowchart is generated for the logic flow of the project.

#### Libraries

The following Libraries have been imported for this project:<br>
1. gspread - This library is used to link the program to Google Sheets where the main data has been stored.
2. questionary - This library is used to create an aesthetically pleasing and user friendly command line interface
3. os - This library is used to create a function to clear the terminal thereby reducing the clutter on screen for a better user experience, taking into account the operating system being used by the user.
4. bcrypt - This library has been used to encrypt the password data provided by a user, offering additional security for the user data.
5. datetime - This library has been used to allow the program to pull the current date for the user interaction which is used when logging and viewing tracked habits.
6. re - This library (which stands for regular expressions) has been used when validating usernames and passwords to ensure the user input matches the requirements set out in the validation functions.
7. time - This library has been used to create a time delay prior to clearing the terminal so the user can see any printed messages applicable for their actions.
8. shutup - This library has been used to allow the files to ignore the deprecation warning relating to the gspread library.

### Testing

### Bugs

When developing the project there were a few bugs I came accross that thankfully I was able to fix to allow the application to run correctly.

1. Unable to view terminal output.<br>
At the start of the development process I attempted to use the 'keyboard' library within Python, however this type of library was not compatible with the Code Institute Respository Template, and therefore prevented the terminal from running the project successfully. For this reason I chose to instead utilise the Questionary library which allowed the project to run in the terminal, whilst also presenting the code in a user-friendly manner.

2. Unable to Delete Habit. <br>
When creating the function for a user to delete a chosen habit from the database, an error occured whereby the user was not given the opportunity to input the details for the habit to be deleted, and instead the terminal would continuously print that the habit could not be located. This was caused by an error with the initial request for user input. I have been able to resolve this and now the user can input the details of the habit they would like to remove. <br>
Delete Habit Bug:<br>
![Delete Habit Bug]()<br>
Delete Habit Fixed:<br>
![Delete Habit Fixed]()<br>

3. Deprecation Warning.<br>
Part way through the development of the project I noticed a deprecation warning would appear when running the project in the terminal. After looking into the issue being raised in this warning (please see further details within the [Resources](#resources) section below) I was able to determine that the warning would not affect the functionality of the project and therefore I could choose to ignore this warning. I chose to utilise a library within python called 'shutup' which would set the workspace to ignore these warnings. As this would remove any warnings of this type, I chose not to implement this solution until all other aspects of the project had been completed so I would not miss any other warnings that could negatively impact the project.<br>
Deprication Warning:<br>
![Deprication Warning]()<br>

4. Password Validation.<br>
Towards the end of the project, when testing it's functionality, I can accross an issue with the password validation function whereby any password entered by a user in the log in/register functions was not correctly validating the password input provided. Using print statements to assist with debugging, I was able to determine the bug occured due to the requirements for the password being contradictory. Passwords created were allowed to include special characters initially, however were then given a condition to only allow alphanumeric characters. Once the condition for alphanumeric characters was removed the validation function worked as intended and the password was confirmed.<br>
Password Validation Bug:<br>
![Validate Password Bug]()<br>
Password Validation Fix:<br>
![Validate Password Fix]()<br>

5. Logging Completed Weekly/Monthly Habits.<br>
When testing the function to allow the user to log their completed habits for the current date, I noticed that only the daily habits were being saved within the habit_log worksheet.<br>


6. Deleted Account- Removing All Stored Habits.<br>
When testing the function to delete an account, I noticed that not all of the saved habits associated with the user's username were being deleted.<br>
![Delete Account Bug]()

### Deployment

The following sections explain how this project has been deployed.

#### Version Control

I have created this project using the Code Anywhere IDE with all changes being pushed to the github repository named 'Habit_Tracker'.<br>

The following git commands have been utilised throughout the development process in order to push changes to the above mentioned respository: <br>

- git add . - This command will add the file(s) to the staging area before they are commited to the local repository.
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

This project makes use of Google Sheets to store all data required. Please see the following steps to create your own copy of the worksheet used and how to connect this within the cloned repository.<br>

1. If you do not already have an account with Google you will need to sign up [here](https://accounts.google.com/Signup). Make sure to use a personal account rather than any shared business accounts to keep the data secure.
2. In order to maintain the security of the data for my project, I have restricted access to the original sheet. The credentials also will not be included in the cloned repository, therefore you will need to create a new sheet. **Make sure the name of the sheet is saved as *habit_tracker* so this can be correctly linked to the cloned repository.**
3. Below shows how the sheet needs to be set up for the application to run smoothly:<br>
User Accounts Worksheet: <br>
![User Accounts Worksheet]()<br>
Habits List Worksheet: <br>
![Habits List Worksheet]()<br>
Habits Log Worksheet: <br>
![Habits Log Worksheet]()<br>
4. Once you have the sheet set up correctly, you will need to activate the API credentials. A detailed guide to set this up can be found [here](https://docs.gspread.org/en/latest/oauth2.html). As part of this guide you will create a JSON file which should be downloaded as saved to your local machine, we will need this file for the next step.
5. Now that you have created and saved your JSON credentials file, we want to download this to the root of the project. To do this drag the file from your downloads(or wherever you have this saved locally) directly into the IDE workspace. Make sure to re-name this file as *creds.json*.
6. Within the newly saved *creds.json* file locate the client_email and copy the value shown (**do not include the quotes**). Now return to your sheet and select the *Share* button to the top-right. Paste the copied client email and ensure *Editor* is selected, and untick the *Notify People* option. You can now click *Share* which will allow the IDE workspace to now access and edit the sheet.
7. As the creds.json file contains sensitive information, we do not want this file to be pushed to the repository. To prevent this go to your .gitignore file within the IDE workspace and add creds.json on a new line. You can now save the file using CTRL-S, and push the changes using the [Version Control](#version-control) commands noted above.<br>

The cloned repository already contains the required code to connect the project to the sheet created in Google Sheets, so as long as you have followed the above steps correctly this will run smoothly when deployed to Heroku (see below for [Heroku Deployment](#heroku-deployment)).

#### Heroku Deployment

This project has been deployed to [Heroku](https://dashboard.heroku.com/apps), this being a Platform as a Service (PaaS). This enables developers the ability to build, run and operate applications in the cloud as is required as per the [Project Goals](#project-goals) for this project.<br>

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