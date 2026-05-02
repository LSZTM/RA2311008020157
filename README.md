Logging Middleware Backend

Overview

This project implements a simple logging middleware for a backend application.
It captures important events like successful requests, warnings, and errors, and sends them to an external logging service.

The focus was to keep the logging reusable and make sure it doesn’t interrupt the main application even if logging fails.

---

Prerequisites

- Python 3.8 or above
- pip (Python package manager)
- Basic understanding of REST APIs

---

Tech Stack

- Python
- FastAPI
- HTTPX
- python-dotenv

---

API Endpoints

Method| Endpoint| Description
GET| /| Basic success response
GET| /health| Health check endpoint
GET| /error| Simulates an error scenario
GET| /simulate-warning| Simulates a warning condition

---
