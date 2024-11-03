# miniproject4OakleyCardwell
### INF601 Advanced Programming with Python
### Oakley Cardwell

## Project Description
This project is a Django-based web application that serves as a freelancer's portfolio and services site. It allows users to view services, browse completed projects, learn about the freelancer, contact the freelancer via a form, and register and log in to the site. The application demonstrates fundamental web development concepts using Python and Django, including user authentication, database interactions, and the use of templates and static files with Bootstrap for a responsive and modern design.

## Application Features
- User Authentication: Secure registration and login system using Django's built-in authentication framework.
- Dynamic Content Management: Display services and portfolio projects stored in the database, manageable via the admin interface.
- Contact Form: Users can send messages through a contact form; messages are stored in the database and viewable in the admin site.
- Database Integration: Utilizes SQLite for data storage, with models for services, projects, contact messages, and optional about content.
- Bootstrap Integration: Enhanced user interface using Bootstrap components, including modals for displaying additional information.
- Responsive Design: The application is mobile-friendly and adapts to various screen sizes. 

## Understanding the Application
Upon launching the application, users can:

- View the Home Page: Welcome message with a call to action to view services.
- Explore Services: View a list of services offered, with details displayed in Bootstrap modals.
- Browse the Portfolio: View completed projects with images and descriptions.
- Learn About the Freelancer: Read about the business owner on the About page.
- Contact the Freelancer: Send messages through the contact form.
- Register and Log In: Create an account and log in to access authenticated features if implemented.
- Access the Admin Interface: Manage content through Django's admin site (for administrators).

## Installation
### Clone the Repository:

```bash
git clone https://github.com/yourusername/miniproject4OakleyCardwell.git
```

### Navigate to the Project Directory:

```bash
cd miniproject4OakleyCardwell
```
### Create a Virtual Environment:


```bash
python -m venv venv
```

### Activate the Virtual Environment:

On Windows:

```bash
venv\Scripts\activate
```

### Install the Required Dependencies:

```bash
pip install -r requirements.txt
```

## Database Initialization
Before running the application, you need to set up the database.

### Make Migrations:

```bash
python manage.py makemigrations
```
### Apply Migrations:

```bash
python manage.py migrate
```

### Create a Superuser (for Admin Access):

```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

## Running the Development Server
### Run the Django Application:

```bash
python manage.py runserver
```

### Access the Application:

Open a web browser and navigate to http://127.0.0.1:8000/ to view the application.

## Usage
### Access the Home Page:

View the welcome message and navigate to other pages via the navbar.
### View Services:

- Click on "Services" in the navbar to view the services offered.
- Click "Learn More" on a service to view additional details in a modal.

### Browse the Portfolio:

Click on "Portfolio" to view completed projects with images and descriptions.

### Read About the Freelancer:

Visit the "About" page to learn more about the business owner.

### Contact the Freelancer:

Go to the "Contact" page to send a message via the contact form.

### Register and Log In:

- Use the "Register" link to create a new user account.
- Log in using the "Login" link to access authenticated features.

### Admin Interface:

- Log in to the admin site at http://127.0.0.1:8000/admin/ using the superuser credentials.
- Manage services, projects, contact messages, and other models.
## Requirements
`requirements.txt` contains the necessary dependencies for the project.
You can generate the requirements file by running:

```bash
pip freeze > requirements.txt
```

## Notes
### Media Files:

The application uses media files for project images.
Ensure that MEDIA_URL and MEDIA_ROOT are correctly configured in settings.py.
During development, media files are served via the development server.

### Security Considerations:

The application uses Django's built-in security features.
Ensure the SECRET_KEY in settings.py is kept secret in a production environment.

### Development vs. Production:

This application is intended for educational purposes and runs in development mode.
For production deployment, additional configuration and security measures are required.

## Conclusion
This project serves as a practical demonstration of building a web application with Django, covering key concepts like user authentication, database interactions, and template rendering. By following the installation and usage instructions, you can explore and extend the application to suit your learning objectives.