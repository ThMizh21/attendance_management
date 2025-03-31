**Attendance Management System**
Description
The Attendance Management System is a web application designed to manage student attendance using face recognition technology. The project is built with Python, utilizing FastAPI, Pydantic, and SQLModel for the backend, and dlib for face recognition. It handles the attendance marking based on the time of arrival, with users categorized into Admin, Teacher, and Student roles.

**Key Features:**
**Admin:**

Add users (students and teachers)

View all attendance records (by class and student)

**Teacher:**

View their own attendance records and their students' attendance.

**Student:**

View their individual attendance records.

Optionally mark their attendance using face recognition (without logging in).

**Face Recognition:**

Attendance is automatically marked based on the time of arrival (Before/On 9:00 AM: Present, After 9:00 AM: Late, After 11:30 AM: Absent).

The system uses 68 facial landmarks for identification.

**User Authentication:**

Login is required to view attendance data, and passwords are hashed for security.

Each user has a unique UUID as their identifier.

Installation
**Requirements:**
Python 3.7+

FastAPI

SQLModel

dlib (for face recognition)

Cloudinary (for image storage)

Setting up the Environment:
Clone the repository:

bash
Copy
git clone <your-repository-url>
cd <project-directory>
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up Cloudinary for image storage:

Create a Cloudinary account at Cloudinary.


**Set up the database:**

Configure the database connection in the .env file (if using SQLite or PostgreSQL).


**Running the Server:**
To start the FastAPI server, run the following command:

uv run fastapi dev main.py
This will start the server at http://localhost:8000, where you can interact with the system via API endpoints.

**Authentication:
**All users must log in using their credentials to access attendance data.

JWT tokens will be used for user authentication.

**Face Recognition Attendance:
**The attendance system will mark attendance based on facial recognition. The system recognizes users by their face images stored in Cloudinary.

Face recognition is performed using dlib and 68 facial landmarks for accuracy.

**API Endpoints
****Authentication**
POST /login: User login (Returns a JWT token).

POST /signup: Register a new user (Admin only can add teachers and students).

**User Actions**
GET /attendance: Retrieve user's attendance record.

POST /attendance/mark: Mark attendance using face recognition.

This action does not require logging in but requires face identification.

GET /users: View all users (Admin only).

POST /user/create: Create new users (Admin only).

**Admin Specific**
GET /attendance/all: View all attendance records (Admin only).

GET /attendance/{class_id}: View attendance by class (Admin only).

GET /attendance/student/{student_id}: View attendance for a specific student (Admin only).

**Data Model**
User Model
UUID (Primary Key)

Name

Email (Unique)

Age

Class

Role (Admin, Teacher, Student)

Profile Image (URL from Cloudinary)

Hashed Password

**Attendance Model**
UUID (Foreign Key to User)

Timestamp (Time of attendance marking)

Status (Present, Late, Absent)

**Dependencies**
The system uses the following libraries and technologies:

FastAPI: For creating the REST API.

Pydantic: For data validation and settings management.

SQLModel: ORM for database management.

dlib: For face recognition based on 68 facial landmarks.

Cloudinary: For image storage and retrieval.

JWT: For secure authentication.

Face Recognition
The system uses HOG (Histogram of Oriented Gradients) and Haar Cascade for detecting faces in real-time, ensuring accuracy in facial recognition.

**Libraries and Articles of Interest:**
I was particularly interested in face recognition libraries and their applications in real-time systems.

I explored HOG and Haar Cascade for object detection, which are foundational techniques used in many modern face recognition systems.

**Future Improvements**
Enhance the project with a automated mailing featue which send the attendance report to the student and the respective coach/teacher

**Acknowledgments :**
dlib for face recognition.

Cloudinary for cloud image storage.

FastAPI for the backend framework.
