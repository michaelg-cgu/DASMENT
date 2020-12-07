# Food For Thought
Food for Thought is a software project team bring clients interactive charts and graphs to better understand their date


## Management Components:
**Management is divided into two websources:**
Milestones can be tracked with [Trello](https://trello.com/b/544N7aI3/dp-project)
Daily Tasks can be viewed with [KanBanFlow](https://kanbanflow.com/board/H8yaMCi)


**Several key components to addres are as follows:**
What foods can affect your appetite, your digestive system  
Interactive binary/boolean model based on what you eat 
Forecast an appropriate (carbs, fat, protein) or overall diet breakdown
Mapping local Yelp restaurants/specific items on Whole Foods app/linking general recipes based on likes + avoid foods that irritate 


# Part A
## Product:
**Health Application Highlights**
This web application leverages Health data to produce various health risks in chart format. Additionally, the tool is an application that can be used to track restaurants and specific foods that did not make me feel well. Eventually, this application produces a list of food and restaurants, derived from my dietary needs (and energy level), providing a list of good foods to eat, restaurants to enjoy, etc. 
## Research:
**Several key components to addres are as follows:**
What foods can affect your appetite, your digestive system  
Interactive binary/boolean model based on what you eat 
Forecast an appropriate (carbs, fat, protein)x or overall diet breakdown
Mapping local Yelp restaurants/specific items on Whole Foods app/linking general recipes based on likes + avoid foods that irritate

## User Stories (as of Part A):

As a User, I want to log in 

As a User, I want to ensure only certain people have access to my content 

As a User, I want to upload Health data in a particular format 

As a User, I want to provide a link my doctor could click on and see my Health, risk factors, and journal of restaurants  

As a User, I want to track locations where food made me feel sick and create a list of restaurants to avoid with particular items 

As a User, I want to know Location (as it relates to stress) or Water quality at water fountain after feeling sick 

As a User, I want the web application to be mobile ready 

As a User, I want to use a database to remember specific foods or restaurants that made me sick 

As a User, I would like a network of restaurants that made others with similar issues sick (if I say I gluten sensitive, I want to know what restaurants in an area may adhere to gluten sensitivity. User driven) 

As a User, I want to upload photos of food 

As a User, I want to upload restaurant lists 

As a User, I want a GUI  

As a User, I want to upload notes, date specific 

As a User, I want to edit and delete notes but I may not want the database to overwrite old notes 

As a User, I want to upload photos of myself for an avatar (profile photo) 

As a User, I want charts of Health data 

As a User, I want a matrix of Health data with key findings of these attributes 

As a User, restaurants and past foods should auto populate as journal is updated 

## Estimated Timeline, Part A
Login Function 
I want to log in – 1 week 
I want to ensure only certain people have access to my content – 1 week 
I want a GUI – 2.5 weeks 
I want to provide a link my doctor could click on and see my Health, risk factors, and journal of restaurants –  3 weeks 
Iwant to upload photos of myself for an avatar (profile photo) - 1 week 

Upload 
I want to upload Health data in a particular format – 1 week 
I want to upload photos of food – 1 week 
I want to upload restaurant lists – 1 week  
I want to upload notes, date specific – 1 week 

Beautify – 1.5 weeks  
Mobile responsivity – 72 hours  

Database design 
I want to track locations where food made me feel sick and create a list of restaurants to avoid with particular items – 1.5 weeks 
I want to edit and delete notes but I may not want the data base to overwrite old notes – 1.5 weeks  
I want to upload notes, date specific – 1 week 

Database integration with web application 
I want a matrix of Health data with key findings of these attributes – 3.5 weeks 
If possible, restaurants and past foods should auto populate as journal is updated – 3 weeks  

**Project Estimate: 10 weeks**

## Stakeholders:
Peers and Colleagues looking for health feedback

## Tasks and Roles:
(These are subject to change)
Samah Basit - Database / Developing
Deven Penchel - Designer / Developing
Michael Garcia - PM / Developing
Ali Nusair - Database / Developing


# Part B
**Decompose your user stories into tasks.**
Team Members: Michael Garcia (MG), Samah Basit (SB), Ali Nusair (AN), Deven Panchal (DP) 
 
* As a user, I want to log in and create an individual profile for myself (priority 10) 
*Frontend Django implementation: 1 week, MG*
* As a user, I want to upload my health data in a particular format and have a section to add/update notes (priority 10) 
*Frontend building questionnaire: 2 days, SB*
*Update sensitivities as they arise*
* As a user, I want to view output of my health statistics compared to general population and other users (priority 20) 
*Visualization component of end result compared to gen pop: 1.5 weeks, MG*
*Visualization component of end result compared to users: 1.5 weeks, MG*
* As a user, I want to receive recommendation and alternative paths based on my health data (priority 20) 
*Recommendations on sensitivity based on upload info: 1 week, AN*
*Alternative suggestions: 1 week, AN*
* As a user, I want a component where I can be directed toward alternatives based on location (priority 30) 
*Frontend locational component: 3 days, DP*
*Backend implementation sourcing GIS data: 1 week, DP*

**Outline what features will be in Milestone 1.0 of your project.** 
1. Designed Database  
2. Login Function
3. Registration Function
5. Upload Feature 
5. Baseline User Graphs derived from Data Research
6. Proposed Mockup  
7. testing  

**Build the iterations (at most 2) that will compose your Milestone 1.0. Record the total days of work and the time it will take for your team to complete that work.**
*Iteration 1 (2 weeks):*
1. Design Database  
2. Login Function with Django Implementation 
3. Upload Feature  
  
*Iteration 2 (2 weeks):*
1. Create Visualizations 
2. Create Recommendations and Alternatives 

**Make sure you have dealt with velocity before breaking into iterations.** 

Milestone 1.0 Timeline: (Oct 5 - Nov 3 - 1Milestone, 2 iterations) Total days of work = 21 days
Starting velocity: 0.35 
Total: 10 hrs/ week 
Velocity calculations? 

4 (persons) X 21(days) X 0.35(V) = 29.4 Amount of work for Milestone 1.0



**Allocate tasks to each team member and record the allocation.** 
As a user, I want to log in and create an individual profile for myself (priority 10) - MG
As a user, I want to upload my health data in a particular format and have a section to add/update notes (priority 10) - SB
As a user, I want to view output of my health statistics compared to general population and other users (priority 20) - All
As a user, I want to receive recommendation and alternative paths based on my health data (priority 20) - AN
As a user, I want a component where I can be directed toward alternatives based on location (priority 30)  - DP

**Create a burn down chart for monitoring your team’s progress.**
* found in projimg folder

**Include evidence that you are meeting for periodic stand up meetings with your teammates, ideally at least twice a week.**
Meeting notes occur at this [link](https://trello.com/b/EF1Bg16A/ist-303-project). View meeting cards

**Ensure that your development and testing environment is set up. Be sure to have some working functional (however rudimentary) and test code in your repository.**
# Testing Environment:
**for Mac:**
Download files from this [location](https://github.com/michaelg-cgu/DASMENT/edit/master/README.md)
Install the following:
* venv
* django
* python3 
* pytest

## install commands:
1. Open the terminal
2. type: python --version
ensure python is installed
if installed, >3.0 continue
3. type: python3 -m pip3 install --user virtualenv
4. in the terminal, navigate to the virtualenv folder using cd commands (change directory)
5. type source venv/bin/activiate
6. verify that (base) has changed to (venv)
7. in venv, type the following:
pip3 install django
pip3 install pillow
pip3 install crispy-forms
8. in venv, change directory again to downloaded github repo. 
9. Navigate to DASEMENT -> FoodforThought
10. in command line, type: ls
11. verify that Manage.py appears
12. type the following: 
python3 manage.py runserver
13. open browser, type the following into the URL: localhost:8000

## Testing
We use pytest-django
* install pytest by pip3 install pytest --user
* install django testing by pip3 install pytest-django
* install cov testing by pip3 install pytest-cov
* Do this both inside and outside of virtual env if you run into errors
* in the terminal, navigate to FoodforThought directory, enter the following:
$ pytest -v
* To change files for testing, for testing, edit pytest.ini
* Coverage Testing: $ coverage run -m pytest
* Coverage Report: coverage report -m to see results on terminal
$ coverage html


## FAQS:
* if runserver error occurs when typing python3 -manageserver, ensure Django is installed in virtual environment
* if no such directory error occurs when running Manage.py or starting up venvironment, ensure you are in the proper place to start the virtual environment or manage.py


# Part C
## Milestone 1 Deliverables:​
* Design Database​
* Ensure user data is stored in backend​
* Login functionality – authentication​
* Login functionality – pass data to backend​
* Create User Registration Form​
* Pass registration data to the backend​
* User Data fields to research​
* Deploy Food Allergy Survey​
* Deploy Seasonal Allergy Survey

Updated burnchart found in proj image


# Part D
## Milestone 2 Deliverables:​

