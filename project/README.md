Photo Company Webapp
#### Video Demo:  <https://youtu.be/p0ocujius8w>

#### Description:
The Photography Studio Booking System is a web application designed to facilitate easy booking of photography sessions for clients. This project integrates Google Calendar for real-time appointment scheduling, ensuring seamless management of bookings and availability. It also includes email notifications for booking confirmations, providing a comprehensive solution for both clients and photographers.

### Overview
The system is built using Flask, a lightweight Python web framework, and utilizes Google OAuth for secure user authentication. It allows users to log in, view available time slots, and book appointments directly through the website. The application is designed to be user-friendly, providing a clean interface for both clients and administrators.

### Key Features
- **User Authentication**: Users can log in using their Google accounts, ensuring secure authentication and authorization.
- **Appointment Booking**: Clients can select available time slots and book appointments, which are automatically added to the photographer's Google Calendar.
- **Real-time Availability**: The system checks for real-time availability, preventing double bookings and ensuring accurate scheduling.
- **Email Notifications**: Upon booking, clients receive automated email notifications confirming their appointments.
- **Responsive Design**: The website is fully responsive, providing an optimal user experience across various devices.

### Google API Integration
The application leverages the Google Calendar API to manage appointments efficiently. This integration allows for:
- **Real-time Scheduling**: Ensures that appointments are always up-to-date and accurately reflected in the calendar.
- **Automated Notifications**: Sends email notifications to clients upon booking, enhancing user experience and engagement.

### Database Management
The system uses SQLite to store user data securely. This database is designed to handle user registrations and logins efficiently, ensuring that all user information is stored locally and securely.

### Project Structure
The project consists of several key files and directories:
- **app.py**: The main application file containing Flask routes, Google OAuth integration, and database interactions.
- **templates/**: A directory holding HTML templates for different pages, including the layout, index, login, register, and booking pages.
- **static/**: Contains static assets like CSS stylesheets and images used throughout the application.
- **credentials.json**: A JSON file holding Google OAuth credentials for authentication.
- **photography.db**: A SQLite database used for storing user information.

### Design Choices
Several design choices were made during the development of this project:
- **Google OAuth**: Chosen for its ease of use and security benefits, allowing users to log in without creating additional accounts.
- **Google Calendar Integration**: Selected for its robust scheduling features and real-time availability checks, ensuring efficient appointment management.
- **Flask Framework**: Used due to its lightweight nature and ease of development, making it ideal for rapid prototyping and deployment.
- **SQLite Database**: Chosen for simplicity and ease of setup, suitable for small-scale applications like this photography studio booking system.

### Future Enhancements
Potential future enhancements include:
- **Multi-Photographer Support**: Allowing multiple photographers to manage their schedules through the same system.
- **Customizable Booking Forms**: Providing options for clients to specify additional details or preferences during booking.

### Conclusion
The Photography Studio Booking System is a comprehensive solution for managing photography appointments. It combines user-friendly design with robust backend functionality, ensuring a seamless experience for both clients and photographers. This project demonstrates the power of integrating Google services with Flask to create efficient and scalable web applications.