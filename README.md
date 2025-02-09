# To-Do Django Application

A simple To-Do application built using **Django** to manage tasks and track daily progress. This project allows users to register, log in, and manage their to-do lists, including adding, updating, and deleting tasks. It is designed with separate branches for HTML and CSS files for better structure and maintainability.

## Features

- **User Authentication**: Allows users to sign up, log in, and manage their accounts.
- **Task Management**: Users can add, edit, and delete tasks.
- **Responsive Design**: The interface is designed to be user-friendly and responsive across devices.
- **Separate Branches**: HTML and CSS files are managed in separate branches for clear project structure.

## Technologies Used

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, CSS
- **Database**: SQLite (Default for Django)
- **Version Control**: Git & GitHub

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/todo-django.git

2. **Navigate into the project directory**:
   ```bash
   cd todo-django
   
3. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   
5. **Run the migrations to set up the database**:
   ```bash
   python manage.py migrate
   
6. **Start the development server**:
   ```bash
   python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000/ to view the application.

## Project Structure


### Explanation of the project structure:

- **todo/**: This is the main Django app where your core logic resides.
  - **migrations/**: Contains database migrations.
  - **models.py**: Defines the data models for your app.
  - **views.py**: Contains application logic for handling requests.
  - **urls.py**: Manages URL routing for the application.
  - **templates/**: Holds HTML files for the views.
  - **static/**: Contains static assets like CSS files, images, and JavaScript.
  
- **manage.py**: A script used for managing the Django project.
- **requirements.txt**: Lists all the required Python libraries and dependencies.
- **README.md**: The project documentation.

## Acknowledgments

- **Django Framework**: The core framework used for building this application.
- **HTML & CSS**: For creating the structure and styling of the web application.
- **GitHub**: For providing a platform for version control and collaboration.
- **Open-Source Contributors**: Special thanks to everyone who contributed to this project.



