# djangoAPI

This repository consists of a set of API endpoints using Django REST Framework and MySQL database. 

#### How to run a local instance on Windows (after Python 3 has been installed):
1. Create a new folder <i> $mkdir djangoAPI </i>
2. Change directory to djangoAPI <i> $cd djangoAPI </i>
3. Create a virtual environment <i> $python3 -m venv myvenv</i>
4. Activate your virtual environment <i> $myvenv\Scripts\activate </i>
5. Change directory to myvenv <i> $cd myvenv </i>
6. Add in the requirements.txt in this folder
7. Install the required libraries via <i> $pip install -r requirements.txt </i>
8. Add in the ticketapi folder in this folder
9. Change directory to the ticketapi folder <i> $cd ticketapi </i>
10. Run the server locally <i> $python3 manage.py runserver </i>


#### In mySQL console, we have to create a database, a user and grant all privileges to that user since the database connection was configured that way in the settings: 

$CREATE DATABASE relationships;

$CREATE USER 'ticketUser'@'localhost' IDENTIFIED BY 'password';

$GRANT ALL PRIVILEGES ON relationships.* TO 'ticketUser'@'localhost';


