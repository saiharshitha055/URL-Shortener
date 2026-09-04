import os
import secrets
import string

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import URL
from schemas import URLCreate, URLResponse


PUBLIC_BASE_URL = os.getenv(
    "PUBLIC_BASE_URL",
    "http://127.0.0.1:8000"
)


app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}


@app.post(
    "/shorten",
    response_model=URLResponse,
    status_code=status.HTTP_201_CREATED
)
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        original_url=str(url_data.url),
        short_code=short_code
    )

    try:
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to save the shortened URL."
        )

    return {
        "short_code": new_url.short_code,
        "short_url": f"{PUBLIC_BASE_URL}/{new_url.short_code}"
    }


@app.get("/{short_code}")
def redirect_to_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    try:
        url = db.query(URL).filter(
            URL.short_code == short_code
        ).first()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to retrieve the shortened URL."
        )

    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Short URL not found"
        )

    return RedirectResponse(url.original_url)