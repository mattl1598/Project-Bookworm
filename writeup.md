# AQA A Level Computer Science Project Writeup

## Analysis
### Background to and identification of problem
#### Overview of Scenario and Current User setup
Hampshire County Councils School Library Service loans large numbers of books (200+) to schools in Hampshire.
Their current system is limited to tracking number of books loaned.
The current system is managed using a group of "three?" excel spreadsheets for managing school data, 
subscription information and loan details. 

### Description of current system

 **insert excel spreadsheet analysis** 
### Data collection and research
#### Questionnaire:
Survey made on Enalyzer.

Question 1:
![Screen cap of question 1](https://github.com/mattl1598/Project-Bookworm/blob/master/survey/q1.PNG "Question 1")

Question 2:
![Screen cap of question 2](https://github.com/mattl1598/Project-Bookworm/blob/master/survey/q2.PNG "Question 2")

Question 3:
![Screen cap of question 3](https://github.com/mattl1598/Project-Bookworm/blob/master/survey/q3.PNG "Question 3")

Question 4:
![Screen cap of question 4](https://github.com/mattl1598/Project-Bookworm/blob/master/survey/q4.PNG "Question 4")

Question 5:
![Screen cap of question 5](https://github.com/mattl1598/Project-Bookworm/blob/master/survey/q5.PNG "Question 5")
#### Results:
 **\*Insert Results here***

### Identification of prospective users
The users would be the librarians at the Hampshire School Library Service who could use it to manage the loans easier.
### Identification of user needs and acceptable limitations
####Features requested:

#### Features priority based on number of suggestions:

### Data sources and destinations
### Data Volumes
### Object analysis diagram
### Analysis data dictionary and ERD
### Realistic appraisal of the feasibility of potential solutions
### Justification of chosen solution
## Design
### Overall System Design
### Description of modular structure of system 
### Definition of data requirements 
### Identification of appropriate storage media
### Entity relationship diagram(Normalised)
### Identification of processes and suitable algorithms for data transformation

### Class and object diagrams 
### User interface design (HC)
#### Books Details:
Text boxes: title, author, genre, released, binding, age, label, blurb, image.
* Title: Book title and subtitle (maybe??) 
* Author: authors. pretty self explanatory
* Genre: genre of book
* Released: release date
* binding: should be paperback or hard cover. doesnt work. can be repurposed.
* age: age rating ("mature" or "not mature")
* label: blank. can be repurposed.
* blurb: the book blurb.

Canvas: image
* image: book cover image

Buttons: save changes, close, revert to online data.
* Save changes: gets the data from the editable text boxes and saves it to a database.
* close: closes the window.
* revert to online data: deletes the database version of the book details and lets the program use the google books data instead.

Image:
 ![Screen cap of books details](https://github.com/mattl1598/Project-Bookworm/blob/master/gui%20images/book%20details%20(image%20error).PNG "Books Details")



### Hardware specification 
#### Input Devices 
#### Output Devices
#### Storage devices
#### Processor and Memory requirements
### Description of measures planned for security and integrity of data and system security
### Overall test strategy 
### Testing
## System Maintenance
### System Overview
### Sampled Detailed Algorithms

## User Guide 
### Contents

## Evaluation
## Program Code
