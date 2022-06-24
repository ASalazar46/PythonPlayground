# Capstone Project Redux

## Project Number: 8

## Team: Andrew Salazar

### Overview

Acquire data from a database and display it on a dashboard.

### Context

A rough remake of the project I worked on for my engineering capstone projects (EE396 & EE496). This project was focused on gathering weather pattern data of the local area, retrieving and managing the data on a server, and displaying it on a website dashboard for analysis. There were multiple teams working on different parts of the project. My team was assigned to maintain the website dashboard that displays the data. For the time I was contracted to work on this project, I found it to be a huge learning experience. In my adventure to learn Python, I decided to redo this project using Python and Python-based frameworks. I don't have access to the project's documentation and source code for reference anymore (because I graduated), so what I mean by "rough remake" is this: I will do all of the work I remember doing for this project, in addition to patching in missing project pieces with new things.

### Goals

- Experience more Python application building.
- Write more design documents.
- Complete project according to a proposed solution.

### Achieved Milestones

- [6/23/2022] Project files created.

### Proposed Solution

asdf

#### Front-end things

asdf

#### Back-end things

asdf

#### Database and data management

The gathering and management of data was handled by the rest of the teams in the project. Since these teams are nonexistent in this project redux, I will need to find a way to gather weather pattern data. There are a two ways I can go about this:

- Find an already existing file containing weather pattern data
- Randomly generate data values

Regardless of the data collection method the data needs to be stored in a database. Since there is no database server that I can access, the next best thing is to host a serverless database on this machine as I work on this project redux. As a consequence, this project will use SQLite instead of PostGresSQL as its database language. The good news is that Python supports the use of SQLite3 as a module in the standard Python library. Once the data is stored in the database, the back-end software can access it via a representative state transfer (REST) API and the front-end can display it.

### Current Progress/Solution
