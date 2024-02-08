Assessment Test Engineer Mendix
===============================

Introduction
------------

This assessment consists of two assignments. Each assignment is intended to give
insights on your skills.

Please read the exercises carefully. If you have any questions at all, do not
hesitate to contact us.

After completing the exercises, please send us your results via email.

In your next interview we will discuss your results. The focus will be on your
reasoning and chosen methodologies when tackling the assignment. We will conclude
the interview with an exercise in exploratory testing.

Please treat this exercise as confidential so that we can reuse it for any
future candidates.

Good luck and please enjoy!



The Pet Clinic
--------------

### Background information

Mendix has a customer, *PetVets Inc. – a Pet Clinic*, that uses Mendix to create
and maintain an online booking system for their customers. You are working as a
member of the Mendix Expert Services team. *PetVets Inc.* contacted Mendix to
help them with this specific customer, because they are struggling with
development. Your assignment is to consult with the PetVets Inc. development
team to make the PetVets app fly.

Last year they released the following:

-   Website with calendar to make appointments

-   Availability overview of employees, rooms and equipment.

-   Customers can consult this overview as well

-   Email, SMS and Slack reminders for customers and Employees when an
    appointment is made.

-   Online payments with PayPal

-   Overview of the customers (CRM)



**The PetVets Inc. Scrum Team**

The development team consists of a single scrum team with 5 developers, 1 Test
engineer and a Product Owner. The team has faced some tough luck last year and
the motivation level is below zero.

During the Retrospective the team states they have lost confidence in the
product. There are bugs in the product that show a lack of testing by both
developers and testers. Besides that, there are very unclear requirements, and the
Product Owner has a hard time satisfying the stakeholders, who keep pressing
him.

The last two releases had to be rolled back, because of unpredicted behavior of
the product.

The team thinks that the stakeholders demand too much and are unreasonable with
deadlines. The result is a poor quality product and a decrease in motivation in
the team.

### Exercise description

The team is willing to give it a one last try. Their goal is to restore faith in
the product and the quality they deliver. You are asked to join the team as
second Test Engineer. You will join the team for at least a month and will be part
of the team for the next two sprints. The duration of a sprint is two weeks.

For the next sprint planning, the following 6 stories are on top of the Product
Backlog and are within the average velocity of the team. Before you start, the
development team provides with these stories, so you can prepare and give some
feedback in advance. Before the sprint starts you will have a meeting with the
team.



**User Story 1**

As a Pet Owner  
I want to view available time slots So I can make a new appointment as quick as
possible

*Acceptance criteria:*

-   Should work in IE and Firefox

-   Appropriate candidate should be presented in details

-   Build a user friendly interface for searching

Table Mockup

| Search query:                   | Search results:                   |
|---------------------------------|-----------------------------------|
| Start date/time: [ inputfield ] | Timeslot 1 (Details Veterinarian) |
| End date/time:   [ inputfield ] | Timeslot 2 (Details Veterinarian) |
|                                 | Timeslot 3 (Details Veterinarian) |
|                                 | Timeslot 4 (Details Veterinarian) |



**User Story 2**

As a Pet Owner I want to create a new appointment myself

*Acceptance criteria: *

-   Start and End time must be filled in

-   User can select Veterinarian

-   User can select Space and Equipment



**User Story 3**

As a Pet Owner  
I want to edit a new appointment

*Acceptance criteria:*

-   Start and End time can be changed

-   User can select different Veterinarian

-   User can select Space



**User Story 4**

As a Veterinarian
I want to cancel my appointment

*Acceptance criteria:*

-   Veterinarian must be notified by SMS or email  



**User Story 5**

As a Developer  
I want to remove the Hibernate layer out of the searching calls  
So adding new queries will be easier

*Acceptance criteria:*

-   Online Payment components should be able to register

-   No iFrames allowed!



**User Story 6**

As a Developer  
I want to refactor the current implementation of the consult overview So that it
will be a better maintainable

*Acceptance criteria:*

-   The user should not notice anything




### Exercise 1: Prepare the Sprint

PetVets Inc has scheduled a pre-sprint team meeting. During this meeting you are
expected to share your thoughts and suggestions on the current situation of the
team and on how to approach the upcoming sprint(s).

Try to be concise but complete. Pay attention to:

-   What were your findings from reviewing/inspecting the stories?

-   What would you ask from the Product Owner/Dev Team?

-   Where do you see yourself and the other Test Engineer in the process?

-   How will you interact with the team during the sprint?


### Exercise 2: Expand test coverage

You are tasked with expanding and improving the test coverage of IAmDb; a Python application that implements a basic REST API that provides access to movie information. You can find the source code for IAmDb in the folder `iamdb`. This product is entirely stand-alone, and should be treated as such. E.g. all references in the code to the 'root folder' refer to `test-assessment/iamdb/`. 

This exercise is designed to take you several hours, though the actual time you invest is entirely up to you. We do ask that you explicitly mention (an estimate of) how much time you spent so that we may fairly judge the result. 

In the `test` folder, you will find the outline of a test suite for the IAmDb API. Based on the resources provided in the application folder, expand that test suite to cover all the existing functionality. You should treat the suite as if it were production code, applying all the standards you would if you were working in a professional team of developers. 

We expect you to flesh out the scripts. Feel free to change, update, and expand the test suite in any other ways you see fit. Improvements to the structure and the test framework itself are also perfectly acceptable.

You are also more than welcome to peruse the source code of the API itself. However, be warned that the application is still being developed. You may assume the backend will drastically increase in size and complexity. Your test suite should be engineered with this in mind. 

To gather insight in your process, we would prefer you submit your assessment as a git repository. However, if you are not familiar with git, your submission will still be accepted if you ignore the git instructions below.

Before you get started, run `git init` inside the `iamdb` folder. All your changes should be committed to the resulting repository and the `.git` folder should be included when you submit your results. Again, IAmDb should be considered production code for the purposes of this assessment, which includes your git history. Furthermore; this assessment should be considered confidential information, so please do _not_ upload your repository to a remote git server, such as GitHub. 

While developing the test suite, pay attention to:

- Code quality. Your code should strive to be self-explanatory, with clear variable names, transparent structure, and a minimum of duplication. 

- Test scope. Make sure everything that needs to be tested is tested, while minimizing redundancy. 

- Test structure. Each test in the script should be maintainable, easy to find, transparant in its execution, and have a clear (useful) goal. 

Upon completion, please mail the `iamdb` folder to your contact for this interview process. 


#### Tooling
If your current IDE does not support Python, [Visual Studio Code](https://code.visualstudio.com/download) is a relatively light-weight option. Make sure to install the recommended Python extensions if you wish to exploit the Python linter. 

The instructions for the application assume the user has a Unix-based terminal. We recommend you either complete this section of the assessment on a Mac or Linux device, or install a terminal that mocks the Unix command line on Windows. A decent example is Git Bash, which ships with the [standard Windows Git install](https://git-scm.com/downloads). 
