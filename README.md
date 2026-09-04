# URL Shortener API

A simple REST API that converts long URLs into short, shareable URLs and redirects users to the original URL.

The application is built with FastAPI and PostgreSQL and is deployed publicly using Render with Neon PostgreSQL as the cloud database.

## Live Demo

- **API:** https://url-shortener-api-sigv.onrender.com
- **Swagger Documentation:** https://url-shortener-api-sigv.onrender.com/docs

## Features

- Create short URLs from long URLs
- Generate unique 6-character short codes
- Redirect short URLs to their original URLs
- Store URL mappings in PostgreSQL
- Interactive Swagger API documentation
- Environment-based configuration for secure database credentials
- Public cloud deployment

## API Endpoints

### 1. Create a Short URL

**POST** `/shorten`

Request:

```json
{
  "url": "https://www.example.com"
}

Response:

{
  "short_code": "TPjH7D",
  "short_url": "https://url-shortener-api-sigv.onrender.com/TPjH7D"
}
2. Redirect to Original URL

GET /{short_code}

Example:

https://url-shortener-api-sigv.onrender.com/TPjH7D

The API looks up the short code and redirects the user to the original URL.

How to Use
Open the Swagger Documentation.
Open POST /shorten.
Click Try it out.
Enter the long URL.
Click Execute.
Copy the generated short_url.
Open or share the short URL.
Technologies Used
Python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Uvicorn
Neon PostgreSQL
Render
Project Structure
URL-Shortener/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Run Locally
1. Clone the repository
git clone https://github.com/saiharshitha055/URL-Shortener.git
cd URL-Shortener
2. Create a virtual environment
python -m venv env

Windows:

.\env\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file using .env.example as a reference.

For local PostgreSQL:

DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=url_shortener
PUBLIC_BASE_URL=http://127.0.0.1:8000

For a cloud PostgreSQL database, use:

DATABASE_URL=your_database_connection_string

Do not commit .env or database credentials to GitHub.

5. Start the application
uvicorn main:app --reload

The local API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
Deployment

The application is deployed on Render and uses Neon PostgreSQL for cloud database storage.

Environment variables are configured securely through the deployment platform.

Repository

GitHub: https://github.com/saiharshitha055/URL-Shortener.git

License
The project is created for educational purposes.

This project was created as part of a technical assignment.
 
