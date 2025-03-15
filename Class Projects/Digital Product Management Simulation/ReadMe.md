# Digital Product Management Simulation

This project is a simulation of digital product management processes, focusing on sprint management and user story tracking. It allows users to create sprints, add user stories, complete tasks, and generate reports, all while simulating progress over time.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Features

- **Sprint Management**: Create and manage multiple sprints with specified durations.
- **User Stories**: Add user stories with descriptions, acceptance criteria, and priorities.
- **Completion Tracking**: Mark user stories as completed and track their status.
- **Progress Simulation**: Simulate the completion of user stories over a specified number of days.
- **Data Persistence**: Save and load sprint and user story data using JSON files.
- **Reporting**: Generate detailed reports of sprints and their user stories.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maiyarehal/Digital_Product_Management_Simulation
   cd <repository-directory>

2. Make sure you have Python 3 installed on your machine. You can download it from python.org.

3. No additional libraries are required; the code uses standard Python libraries.

## Usage 

1. Navigate to the project directory:
   ```bash
   cd <project-directory>

2. Run the main program:
   ```bash
   python main.py

3. The program will attempt to load existing sprints from sprints.json. If the file doesn't exist, it will create a new sprint and user stories.


## File Structure
```graphql
project/
│
├── user_story.py        # Contains the UserStory class
├── sprint.py            # Contains the Sprint class
├── product_management.py # Contains the ProductManagement class
└── main.py              # Main program execution file
