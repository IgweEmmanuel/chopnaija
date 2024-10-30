# CHOPNAIJA FOOD SHOP

---

This is a food ordering web application. Users use it to make orders for their food online using the web app.
PROJECT: CHOPNAIJA

![Screenshot 2024-07-06 at 11 34 19](https://github.com/IgweEmmanuel/chopnaija/frontend/public/136444225/Screenshot 2024-10-30 at 13.01.28.png)                                             ![Screenshot 2024-07-06 at 11 37 59](https://github.com/IgweEmmanuel/Project_Edumore/assets/136444225/78182c0a-0124-4366-86a5-5a44c88a1e0a)



ChopNaija - Farm Produce Ecommerce
ChopNaija is an e-commerce platform that connects farmers and customers, enabling users to order fresh farm produce from the comfort of their homes.
Features

User Registration and Authentication: Customers can create accounts, log in, and manage their profiles.
Product Catalog: Customers can browse and search for a variety of farm produce, including fruits, vegetables, grains, and more.
Shopping Cart and Checkout: Customers can add products to their cart, view the cart summary, and complete the checkout process.
Order Management: Customers can view their order history, track the status of their orders, and initiate returns or exchanges.
Farmer Management: Farmers can create and manage their product listings, update inventory, and view sales data.
Admin Dashboard: Site administrators can manage user accounts, product listings, orders, and other platform-wide settings.

Technologies Used

Frontend: React.js, React Router, Axios, Tailwind CSS
Backend: Django, Django REST Framework, SQLite/PostgreSQL
Authentication: JSON Web Tokens (JWT)
Hosting: Vercel (frontend), Heroku (backend)

Installation and Setup

Clone the repository:

bashCopygit clone https://github.com/your-username/chopnaija.git

Install the dependencies:

bashCopy# Frontend
cd chopnaija/frontend
npm install

# Backend
cd chopnaija/backend
pip install -r requirements.txt

Set up the environment variables:

Copy# Frontend
cp .env.example .env
# Update the values in the .env file

# Backend
cp .env.example .env
# Update the values in the .env file

Start the development servers:

bashCopy# Frontend
cd chopnaija/frontend
npm start

# Backend
cd chopnaija/backend
python manage.py runserver

Access the application in your browser:

CopyFrontend: http://localhost:3000
Backend: http://localhost:8000
Contributing
We welcome contributions to the ChopNaija project. If you'd like to contribute, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes and commit them
Push your changes to your forked repository
Submit a pull request to the main repository

License
ChopNaija is licensed under the MIT License. CopyRetryClaude does not have the ability to run the code it generates yet. Claude does not have internet access. Links provided may not be accurate or up to date.Claude can make mistakes. Please double-check responses.

MY EXPERIENCE BUILDING THIS PROJECT:

1. CHALLENGES:
The most technical challenge I encountered this week:
This week, I started out very well and have to hard code my APIs. I did the endpoints ranging from register, generate token, refresh token password reset using the django rest framework yasg. 
In the course of this, I encountered a serious bug issue with an email sending endpoint. I wanted to create an email sending and receiving endpoint that will allow teachers to send emails to students. I have to use MAILGUN. There are other free mailing systems like SENDGRID. I encountered a serious issue connecting it to my backend. I have not resolved it up till now. 
Going on to the frontend, I encountered a serious 401 unauthorized error from the backend when accessing the token endpoint. I googled for a long time and could not get the solution. I tried to incorporate the token refresh endpoint function from the frontend to access it at the backend so that I can get a valid token to access the login endpoint after registration. I am still getting 401 errors.


How I resolved the email challenge:
I have to use the default email from mailgun


The most difficult non-technical challenge I faced:
Time management:
I faced serious time management with my portfolio as I had to juggle between getting a gig task done alongside my portfolio project.
Couple of times, I have to be called at odd hours in the middle of my ALX portfolio project to carry out a coding task demanded by the gig.
Upkeep:
I considered gaining industry skill and at the same time to get money for my upkeep while in the programme. This is why I got the gig in the first place. Going through this programme without working and not having enough means to get enough money to take care of one’s needs is truly frustrating I must say. Thanks be to God almighty who has been coming through for me.


2. COLLABORATION:
I have received help from a peer at the Costian Hub ALX Lagos Nigeria. This is the issue with the front end.


3. PROJECT UPDATES:
Change from LMS to video streaming platform
Reason: this is because of time. I do not need to build my own API but consume available APIs on the internet.


4. PROGRESS:
On a scale of 1 to 10, I would rate my progress a 4.
Progress Assessment: 
In this project of building a Learning Management System, I was able to conclude the backend authentication and user login and registration with django.
I am currently debugging my frontend login and register page for the users (React framework)
I will conclude this week with all other parts like the:
Teacher section
Student section
Course section
Parts of Project completed as planned:
The backend register and login authentication with JWT
Using ‘zustand’ package to store user detail at the frontend (React)
The django rest framework API (drf-yasg) endpoints for:
 Register (http://127.0.0.1:8001/api/v1/user/register/), 
generate token (http://127.0.0.1:8001/api/v1/user/token/), 
refresh token (http://127.0.0.1:8001/api/v1/user/token/refresh/),
password reset (http://127.0.0.1:8001/api/v1/user/password-reset/)
Part of the Project that is incomplete:
The frontend in general
The teacher and student section
Course section
In a section named “Challenges” in your status document, answer:
Explain the most difficult technical challenge you encountered in this second week. This answer must be more than 200 words.
Describe the most difficult non-technical challenge you encountered in this second week. This answer must be more than 200 words.


