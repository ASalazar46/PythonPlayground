# Capstone Project Redux

## Project Number: 8

## Team: Andrew Salazar

### Overview

Acquire data from a database and display it on a dashboard.

### Context

A rough remake of the project I worked on for my engineering capstone projects (EE396 & EE496). For the time I was contracted to work on this project, I found it to be a huge learning experience. In my adventure to learn Python, I decided to redo my team's part of the project using Python and Python-based frameworks. I don't have access to the project's documentation and source code for reference anymore (because I graduated), so what I mean by "rough remake" is this: I will do all of the work I remember doing for this project, in addition to patching in missing project pieces with new things.

### Goals

- Experience larger scale Python application building.
- Write more design documents.
- Complete project according to a proposed solution.

### Achieved Milestones

- [6/23/2022] Project files created.
- [6/24/2022] Planning of application started.

### Proposed Solution

#### Front-end things

~~There are many web development frameworks available. Still choosing...~~ I have chosen to learn Django and use it for this project redux. The main reason is because this framework, along with Python, was a suggestion for the choice of software to overhaul the HTML/CSS version of the dashboard. The reason why we went with Javascript and Javascript frameworks instead was because we were learning those softwares in class at the time. It makes sense to use Django and Python for this project redux because I am learning Python. However, I will need some time to go through the Django tutorial and get familiar with the basics of it. However, again, I do have a general idea on what this project may have for content.

A lot of websites have a landing page. We did not make one in the original project, but I may as well make one in this redux. There will be a landing page that contains links to the following pages:

- An 'About Us' section, where it briefly talks about the project's purposes and the people behind the scenes.
- Four buttons (boxes?) that direct users to the data. I say four boxes because there were four teams collecting data, and they were stored in four different databases. In this redux, there can be as much as I want, but I choose four.
- Images, color scheme, and other general design patterns to make the page look pretty and professional (as possible).

In the pages that will display the data, they should have:

- Boxes containing the most recent data points
- Boxes containing an average of the data points
  - Starting with overall, then weekly, monthly, and yearly later on
- A graph plotting the data points

At the top of each page should be a navigation bar. It should contain:

- A clickable logo that directs the user to the landing page when clicked.
- Four buttons that direct the user to the data pages.

#### Back-end things

I am unsure of how the back-end will work with Django, but I'm sure the tutorial will give an overview of how the back-end works. If not, then Django's official documentation may do that. However, the back-end should be able to communicate with the database, and call the necessary database query to retrieve data.

#### Database and data management

The gathering and management of data was handled by the rest of the teams in the project. Since these teams are nonexistent in this project redux, I will need to find a way to gather weather pattern data. There are two ways I can go about this:

- Find an already existing file containing weather pattern data
- Randomly generate data values

Regardless of the data collection method the data needs to be stored in a database. Since there is no database server that I have access to, the next best thing is to host a serverless database on this machine as I work on this project redux. As a consequence, this project will use SQLite instead of PostGresSQL as its database language. The good news is that Python supports the use of SQLite3 as a module in the standard Python library. Once the data is stored in the database, the back-end software can access it and pass it to the front-end for display.

### Current Progress/Solution
