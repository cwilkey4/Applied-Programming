# Overview

This project utilizes a Python software application to interact with a hotel-management database. It is capable of executing basic queries necessary for managing data. It takes user inputs (generally prompting numberical inputs) for navigation. It is possible to check a guest into and out of a room, "clean" the rooms, and review the conditions of every room in the hotel. 

I used to work at a hotel, and the idea of structuring a similar database has crossed my mind before. Admittedly, there is plenty that could be done to improve this project (data for guests, payment information, reservation details, and employees would all be beneficial), but this is a start, with which I am satisfied. 

[Software Demo Video](https://youtu.be/Q6UWrMWaIzU)

# Relational Database

I am using a hotel management database that focuses on the rooms. It records the room number, the type of room it is, the status of that room, and whether or not someone has rented it out. 

There is a "rooms" table with four columns: 
- room_number (INT, Primary Key)
- status (TEXT, records whether a room is 'clean' or 'dirty')
- room_type (TEXT, stores information on the type of bed and room matches that room number)
- availability (TEXT, keeps track of whether the room is 'occupied' or 'vacant')

# Development Environment

- Python
- VSCode
- SQLite and the sqlite3 library.

# Useful Websites

- [w3schools](https://www.w3schools.com/)
- [sqlitetutorial](https://www.sqlitetutorial.net/)

# Future Work

- Originally, I had planned to include more tables until I realized it would be a considerably larger project than what was here. I would like to record other information, such as employees, reservation information, guest details, and payment type. 
- I would like to practice working more with SQLite Studio and the Command Prompt. I got to use them both briefly in the introductory steps but ultimately did not implement either one of them in the final project.
- Additionally, though it is fine to go down a few rabbit holes while learning, it might be wise to focus more on the ultimate objective. Sometimes, coming up with and visualizing exactly what I want is difficult to do, so it's easy to get sidetracked. It might be a good idea to time myself in order to keep track of how much progress a certain course of action makes.