
# Django REST Framework Library Management System

## Overview

This project is a Library Management System developed using the Django REST Framework, a robust toolkit for building Web APIs in Django. The system is designed based on a provided database schema, ensuring structured and efficient management of library resources. The application is tailored for library staff and users, providing a comprehensive administrative panel for professional library management.

## Objectives

1. **Database Integration:**
   - Implement the provided database schema, including tables for books, authors, publishers, members, loans, and more.

2. **User-Friendly Admin Panel:**
   - Develop a professional and intuitive admin panel for library staff to manage books, members, loans, and other library operations.

3. **RESTful API Development:**
   - Create a set of RESTful APIs to facilitate seamless interaction between the front-end and the database, ensuring efficient data handling.

4. **Authentication and Authorization:**
   - Implement robust user authentication and authorization to secure access to the system.

5. **User Management:**
   - Manage library member information, including registrations, profile updates, and membership renewals.

6. **Book Management:**
   - Include features for adding, updating, deleting, and searching for books. Incorporate details like book availability, location, and loan status.



## Technical Specifications

- **Backend Framework:** Django REST Framework
- **Database:** As per the provided schema (SQLite)
- **Authentication:** Django’s built-in authentication system or OAuth

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/librarySystem.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure :
![image](https://github.com/Rahaf57/LibrarySystem-/assets/86688588/2b388985-05df-49dd-8985-e4f110a44c77)


## Admin Panel:
![image](https://github.com/Rahaf57/LibrarySystem-/assets/86688588/2835c595-7963-49ca-a139-d2886ce98d5e)

## Demo for Admin Panel:

https://github.com/Rahaf57/LibrarySystem-/assets/86688588/91b0d06c-5ba7-4b92-b19f-5d268e907eb0







Visit [http://localhost:8000/admin/](http://localhost:8000/admin/) to access the admin panel.



**Happy coding!**
