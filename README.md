# URL Shortener API

A lightweight RESTful URL Shortener API built with FastAPI and PostgreSQL. 
The application converts long URLs into unique, shareable short URLs and 
redirects users to the original destination.

The API is deployed on Render and uses Neon PostgreSQL for cloud data storage.

## Live Application

- **API:** https://url-shortener-api-sigv.onrender.com
- **Interactive API Documentation:** https://url-shortener-api-sigv.onrender.com/docs
- **GitHub Repository:** https://github.com/saiharshitha055/URL-Shortener

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **FastAPI** | Builds the REST API and handles HTTP requests |
| **Pydantic** | Validates incoming URL data and structures API responses |
| **SQLAlchemy** | ORM used to interact with the PostgreSQL database |
| **PostgreSQL** | Stores original URLs and their generated short codes |
| **Neon PostgreSQL** | Cloud-hosted PostgreSQL database for the deployed application |
| **Uvicorn** | ASGI server used to run the FastAPI application |
| **python-dotenv** | Loads environment variables securely during local development |
| **Render** | Cloud platform used to deploy and host the API |
| **Git & GitHub** | Version control and source-code management |

---

## Key Features

- Converts long URLs into unique 6-character short codes
- Generates short codes using secure random selection
- Prevents short-code collisions before storing a new URL
- Stores URL mappings in PostgreSQL
- Redirects users from a short URL to the original URL
- Validates URL input using Pydantic
- Provides automatic interactive API documentation with Swagger UI
- Uses environment variables for database configuration
- Deployed as a publicly accessible API

---

## API Endpoints

### `POST /shorten`

Creates a shortened URL.

**Request**

```json
{
  "url": "https://www.example.com/very/long/url"
}

Response

{
  "short_code": "TPjH7D",
  "short_url": "https://url-shortener-api-sigv.onrender.com/TPjH7D"
}
GET /{short_code}

Redirects the user to the original URL associated with the short code.

Example

https://url-shortener-api-sigv.onrender.com/TPjH7D

If TPjH7D exists in the database, the API redirects the request to its stored original URL.

How It Works
User submits long URL
        ↓
POST /shorten
        ↓
Pydantic validates the URL
        ↓
Generate unique short code
        ↓
Store URL + short code in PostgreSQL
        ↓
Return public short URL
        ↓
User opens short URL
        ↓
GET /{short_code}
        ↓
Find original URL in PostgreSQL
        ↓
Redirect to original URL
Project Architecture
URL-Shortener/
│
├── main.py            # FastAPI application and API endpoints
├── database.py        # Database connection and session management
├── models.py          # SQLAlchemy database models
├── schemas.py         # Pydantic request/response schemas
├── requirements.txt   # Project dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Files excluded from version control
└── README.md          # Project documentation
Application Components

main.py
Contains the FastAPI application, URL-shortening logic, short-code generation, database operations, and redirect endpoint.

database.py
Configures the SQLAlchemy database engine and database sessions. It supports local PostgreSQL configuration and a cloud DATABASE_URL.

models.py
Defines the database structure used to store shortened URL records.

schemas.py
Defines Pydantic schemas for validating incoming URLs and formatting API responses.

Database

The application uses PostgreSQL to maintain the mapping between short codes and original URLs.

Conceptually, each record contains:

Short Code  →  Original URL
TPjH7D      →  https://www.example.com/...

For the deployed application, the PostgreSQL database is hosted using Neon.

Database credentials and connection strings are stored as environment variables rather than being included in the source code.

Deployment

The API is deployed on Render and connected to Neon PostgreSQL.

GitHub
   ↓
Render
   ↓
FastAPI + Uvicorn
   ↓
Neon PostgreSQL

The deployed API is publicly accessible through its Render URL, allowing users to interact with the API without running the application locally.

API Documentation

FastAPI automatically provides interactive Swagger documentation at:

https://url-shortener-api-sigv.onrender.com/docs

Users can test the API directly from the browser by submitting a long URL through POST /shorten and using the generated short URL.
