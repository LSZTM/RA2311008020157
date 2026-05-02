Logging Middleware Backend Service

Overview

This project implements a backend logging middleware that captures application events and sends them to a remote logging service. The middleware is reusable, asynchronous, and designed to handle failures without affecting the main application.

---

Tech Stack

- Python
- FastAPI
- HTTPX
- python-dotenv

---

Project Structure

logging_middleware/
  logger.py
  auth.py
  config.py

notification_app_be/
  app.py

vehicle_maintenence_scheduler/

notification_system_design.md
.gitignore

---

Setup Instructions

Install dependencies

pip install fastapi uvicorn httpx python-dotenv

Configure environment variables

Create a ".env" file:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret

Run the application

uvicorn app:app --reload

---

Logging Middleware

Function

log(stack, level, package, message)

Constraints

- stack: backend
- level: debug, info, warn, error, fatal
- package: controller, route, service, handler, repository, db, etc.
- message: maximum 48 characters

---

Features

- Asynchronous logging
- Token caching for authentication
- Input validation for all fields
- Message length enforcement
- Timeout handling
- Non-blocking logging (does not interrupt application flow)

---

API Endpoints

GET /

Returns a success response.

Response:

{"message": "ok"}

---

GET /health

Returns application status.

Response:

{"status": "running"}

---

GET /error

Simulates an error and logs it.

Response:

{"error": "something went wrong"}

---

GET /simulate-warning

Simulates a warning scenario.

Response:

{"message": "warning simulated"}

---

Notes

- Logging is performed via an external API and is not visible in endpoint responses
- Environment variables are required for authentication
- ".env" file is excluded using ".gitignore"
- Screenshots of API requests, responses, and response time are included separately as required
