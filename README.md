# CHOPNAIJA FOOD SHOP

---

This is a food ordering web application. Users use it to make orders for their food online using the web app.
PROJECT: EDUMORE - (Education Re-imagined)

![Screenshot 2024-07-06 at 11 34 19](https://github.com/IgweEmmanuel/Project_Edumore/assets/136444225/949af463-bc69-41c4-8caa-4d7323bc0e54)                                             ![Screenshot 2024-07-06 at 11 37 59](https://github.com/IgweEmmanuel/Project_Edumore/assets/136444225/78182c0a-0124-4366-86a5-5a44c88a1e0a)



Edumore is an educational web application that answers the pain points of teachers and students and schools as well. Helping students learn through videos and texts. Also helps teachers collaborate by sharing notes and ideas for improved performance and efficiency in their teaching delivery and students' performance.

​

My Personal Story on Edumore:

Hey Chiboy why is your note not up to date? My teacher cleaned the board before I could finish copying from the board. 
Chiboy you failed again this term! Mummy yelled at Chiboy.

​

Teaching Computer Studies and Data Processing for four years has exposed me to first hand experience with what teachers, students and parents pass through in secondary and primary schools as regarding the issue of performance and notes.

It has always been a serious issue when it comes to note, assingments and exams.

I could remeber teachers been penalized for students/pupil's notes not been up to date. 

Ofcourse you know that note taking is key to the success of any student and I don't bame the school managements for taking some actions sometimes. But the teachers deserve some rest too on this isse.



We actually need more better ways to stop students from failing and stop all these shouts on teachers and even the management to offer bettre services to parents.

To this note Edumore was born to offer the MORE better solutions to the note issues and extends profficiency among teachers through collabortion with fellow teachers. This is so that student's performance can increase and teachers knowledge become excellent in their areas through collaboration and school managements achieving better results.

​

It offers the following features:

1. Collaboration

2. Notes in pdf/doc formats

3. Notes in Videos

4. Student's access to these materials.

​

This helps teacher's work to be less stressful and students copy less note while using that time to listen more in class and study with the platform.

​

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


