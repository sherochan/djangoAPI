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

#### Testing: Please run on the local server these commands 
Users(Teachers) have to be added first as a superuser. To add new Teacher, in the virtual environment , run this <i> $python manage.py createsuperuser </i> and follow the instructions. Next, head to the admin page and log in with the credentials of any Teacher on the local instance http://127.0.0.1:8000/admin/ . Go to the Relationship tab to add all the Teachers first. Next, go to the Students tab and add all the emails of the students and register them to the different Teachers.

1. Endpoint: POST /api/register
- Run this in your local browser by entering http://127.0.0.1:8000/api/register/
- This endpoint allows for multiple existing Student objects to be registered to an existing Teacher object in the database
2. Endpoint: GET /api/commonstudents?teacher_email=teacherken@40example.com
- Run this in your local browser by entering http://127.0.0.1:8000/api/commonstudents/?teacher_email=teacherken@40example.com
- however, please note that the response body and the query do not match the one stated in pdf.
3. Endpoint: POST /api/suspend
- Run this in your local browser by entering http://127.0.0.1:8000/api/suspend/
- this endpoint allows for the update of a Student object on his/her suspension
4. Endpoint: GET /api/retrievefornotifications/
- Run this in your local browser http://127.0.0.1:8000/api/retrievefornotifications/
- this endpoint allows a specified teacher to send notification and return it in terms of the students 
- however, please note that the response body do not match the one stated in pdf.
#### Disclaimer: Since the Django REST framework is something new to me and that this was done under a time constraint, please note that this application is a work in progress and might not fulfill some parts of the requirements in the pdf file.


