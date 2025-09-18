# Hotel Management System - Simple Authentication Demo

This is a minimal implementation of the login and dashboard pages for the Hotel Management System.

## How to Use

1. Make sure the backend server is running on port 8005
2. Open your browser and go to: http://localhost:8080/login.html
3. Use the test credentials:
   - Username: admin
   - Password: password123

## Pages

- **Login Page**: http://localhost:8080/login.html
- **Dashboard**: http://localhost:8080/dashboard.html

## Features

### Login Page
- Clean, modern login interface
- Form validation
- Error handling
- Automatic token storage in localStorage
- Redirect to dashboard on successful login

### Dashboard Page
- User authentication check
- Welcome message with user information
- Hotel statistics cards
- Feature cards for different modules
- Logout functionality

## Technical Details

The authentication uses the simple authentication endpoints we created:
- Login: `POST http://localhost:8005/api/v1/simple-auth/simple-login`
- Token is stored in localStorage
- User info is stored in localStorage

## Test Credentials

- **Admin User**:
  - Username: admin
  - Password: password123

- **Receptionist User**:
  - Username: reception1
  - Password: password123

- **Cashier User**:
  - Username: cashier1
  - Password: password123