# URL Shortener API
Built a basic URL Shortener REST API built using FastAPI and PostgreSQL.

## Project Overview
This project provides a simple API for converting long URLs into shorter URLs and redirecting users from a shortened URL to the original URL.
The application uses FastAPI for the REST API, PostgreSQL for persistent data storage, and SQLAlchemy as the ORM for database interaction.

## Features
- Create a shortened URL from a valid long URL
- Generate a unique 6-character short code
- Store URL mappings in PostgreSQL
- Redirect short URLs to their original URLs
- Validate URL input using Pydantic
- Return a 404 response for unknown short codes
- Automatic API documentation using Swagger UI

## Technologies Used
- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- psycopg2
- Pydantic
- python-dotenv

## Project Structure
```text
URL_Shortener/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore

#API Endpoints
1. Create a Short URL
The JSON request body for Endpoint POST /shorten is
{
  "url": "https://www.google.com/"
}
And the response for this JSON text is
{
  "short_code": "WrRZq8",
  "short_url": "http://127.0.0.1:8000/WrRZq8"
}
The short code will be generated dynamically and will be different for each request.

2. Redirect to Original URL
The example for the endpoint GET/{short_code} is
GET /WrRZq8
The API looks up the short code in PostgreSQL and redirects the user to the corresponding original URL.

3. Root Endpoint
The response for the GET/ endpoint is:
{
  "message": "URL Shortener API is running"
}

Database
PostgreSQL is used to store URL mappings.
Database name is url_shortner and the table created is urls
Columns:
Column	           Type	              Description
id	              Integer	          Primary key
original_url	  String	          Original long URL
short_code	      String	          Unique generated short code
Setup Instructions using VS code Terminal powershell:
1.Installed a compatible version of Python as I have 3.12
2.Create a virtual environment
python -m venv venv
3.Installed the dependencies
pip install -r requirements.txt
4. Install PostgreSQL
Install PostgreSQL and pgAdmin.
Create a PostgreSQL database named:url_shortener

5. Configure Environment Variables
Created a .env file in the project root:DB_USER=postgres
                                        DB_PASSWORD=your_postgresql_password
                                        DB_HOST=localhost
                                        DB_PORT=5432
                                        DB_NAME=url_shortener
Caution:Never share your .env file to anyone or any AI because it contains database credentials.

6. Run the Application
uvicorn main:app --reload
Then the API is available at http://127.0.0.1:8000

7. Open Swagger UI
FastAPI automatically provides interactive API documentation at:http://127.0.0.1:8000/docs
Use Swagger UI to test the API endpoints.

8.Testing
The following scenarios were tested:
i.Successful URL shortening
POST /shorten with a valid url returns 201 Created

ii.Database persistence
The generated URL mapping is stored in the PostgreSQL urls table.
Successful redirection
Opening is http://127.0.0.1:8000/{short_code} that redirects the user to the original URL.

iii.Invalid short code
An unknown short code returns: 404 Not Found
with the following JSON structure:
{
  "detail": "Short URL not found"
}

iv.Invalid URL
An invalid URL submitted to /shorten is rejected by request validation with: 422 Unprocessable Entity

Architecture of the project:
Client
  |
  | HTTP Request
  v
FastAPI
  |
  v
SQLAlchemy
  |
  v
PostgreSQL
  |
  v
urls table

Note: This project is intended as a basic local URL shortening API for the assessment. The generated short URLs use the local application address during development.


 