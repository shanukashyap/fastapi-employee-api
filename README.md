# Employee Management API

A secure Employee Management REST API built using **FastAPI, Python, SQLAlchemy, SQLite, Pydantic, and API Key Authentication**.

The application provides CRUD operations for employees and protects the API endpoints using an API key passed through the `X-API-Key` HTTP header.

## Features

* Create employees
* Get all employees
* Update employees
* Delete employees
* API key authentication
* Protected API endpoints
* Pydantic request validation
* Email validation
* Salary validation
* Duplicate email prevention
* SQLite database
* SQLAlchemy ORM
* Swagger UI documentation
* Proper HTTP status codes
* Secure environment-variable configuration

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* python-dotenv

## Project Structure

```text
fastapi-employee-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── crud.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shanukashyap/fastapi-employee-api.git
```

Move into the project:

```bash
cd fastapi-employee-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

The API key must not be stored directly in the source code.

Create a `.env` file:

```text
API_KEY=your-secret-api-key
```

For example, locally:

```text
API_KEY=super30-secret-key
```

The `.env` file is included in `.gitignore` and must not be pushed to GitHub.

A safe `.env.example` file is included in the repository:

```text
API_KEY=your-secret-api-key-here
```

## Run the Application

Start the server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the API.

## Authentication

The protected endpoints require an API key in the HTTP header:

```text
X-API-Key: your-secret-api-key
```

The API key is loaded from the `.env` environment variable.

The application does not hard-code the secret API key in the source code.

## Authentication Responses

### Missing API Key

If the `X-API-Key` header is missing:

```text
401 Unauthorized
```

Example response:

```json
{
  "detail": "API key is missing"
}
```

### Invalid API Key

If an incorrect API key is provided:

```text
403 Forbidden
```

Example response:

```json
{
  "detail": "Invalid API key"
}
```

### Valid API Key

When the correct API key is provided, the request is allowed to continue to the requested endpoint.

## API Endpoints

| Method | Endpoint                   | Authentication | Description       |
| ------ | -------------------------- | -------------- | ----------------- |
| GET    | `/employees`               | API Key        | Get all employees |
| POST   | `/employees`               | API Key        | Create employee   |
| PUT    | `/employees/{employee_id}` | API Key        | Update employee   |
| DELETE | `/employees/{employee_id}` | API Key        | Delete employee   |

## Create Employee

### Endpoint

```text
POST /employees
```

### Request

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "department": "IT",
  "designation": "Python Developer",
  "salary": 65000
}
```

### Response

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "department": "IT",
  "designation": "Python Developer",
  "salary": 65000
}
```

## Get Employees

### Endpoint

```text
GET /employees
```

The endpoint returns all employees after successful API key authentication.

## Update Employee

### Endpoint

```text
PUT /employees/1
```

### Request

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "department": "AI",
  "designation": "Generative AI Engineer",
  "salary": 90000
}
```

## Delete Employee

### Endpoint

```text
DELETE /employees/1
```

Example response:

```json
{
  "message": "Employee deleted successfully",
  "employee_id": 1
}
```

## Validation

The API uses Pydantic for input validation.

### Name

The employee name must contain between 2 and 100 characters.

### Email

The email must be a valid email address.

### Department

The department must contain between 2 and 50 characters.

### Designation

The designation must contain between 2 and 100 characters.

### Salary

Salary must be greater than zero.

## Example Invalid Request

```json
{
  "name": "A",
  "email": "invalid-email",
  "department": "",
  "designation": "X",
  "salary": -5000
}
```

FastAPI/Pydantic rejects the request with validation errors.

## Duplicate Email Validation

The API prevents two employees from using the same email address.

If an existing email is submitted, the API returns:

```text
400 Bad Request
```

with:

```json
{
  "detail": "Employee with this email already exists"
}
```

## Database

The application uses SQLite.

The database file is:

```text
employees.db
```

SQLAlchemy is used as the ORM.

The main database table is:

```text
employees
```

with fields:

```text
id
name
email
department
designation
salary
```

## Authentication Flow

The authentication process works as follows:

```text
Client
   |
   | X-API-Key
   ↓
FastAPI
   |
   ↓
verify_api_key()
   |
   ├── Missing key → 401
   |
   ├── Invalid key → 403
   |
   └── Valid key
          |
          ↓
      API endpoint
          |
          ↓
      Pydantic validation
          |
          ↓
      Database operation
```

## Security

The real API key is not committed to GitHub.

The `.env` file is included in `.gitignore`.

Only `.env.example` is committed to the repository.

This prevents accidentally exposing the secret API key in the public GitHub repository.

## Testing

The following scenarios should be demonstrated:

1. Successful GET request with valid API key.
2. Successful POST request with valid API key.
3. Successful PUT request with valid API key.
4. Successful DELETE request with valid API key.
5. GET request without API key.
6. GET request with incorrect API key.
7. Invalid employee data.
8. Invalid email address.
9. Negative salary.
10. Duplicate employee email.
11. Request for a nonexistent employee.

## Learning Outcomes

This project demonstrates:

* FastAPI REST API development
* API key authentication
* HTTP headers
* HTTP status codes
* Dependency injection
* Pydantic validation
* SQLAlchemy ORM
* SQLite database integration
* CRUD operations
* Environment variables
* Secret management
* Swagger API documentation
* Error handling
```


