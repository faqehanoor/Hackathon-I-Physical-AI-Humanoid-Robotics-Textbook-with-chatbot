from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.schemas.book import BookCreate, BookResponse, BookUpdate
from src.models.book import BookModel
from src.database.session import get_db
from src.utils.exceptions import BookNotFoundException, InvalidInputException

router = APIRouter()


@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Create a new book entry"""
    try:
        # Validate input
        if not book.title.strip() or not book.author.strip():
            raise InvalidInputException("Title and author are required fields")

        # Convert schema to model
        db_book = BookModel(**book.model_dump())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)

        return BookResponse.from_orm(db_book)
    except IntegrityError as e:
        db.rollback()
        raise InvalidInputException("Book already exists or violates database constraints")
    except ValueError as e:
        raise InvalidInputException(f"Invalid input: {str(e)}")


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: UUID, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise BookNotFoundException(str(book_id))

    return BookResponse.from_orm(book)


@router.get("/", response_model=List[BookResponse])
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get a list of books"""
    # Validate parameters
    if skip < 0:
        raise InvalidInputException("Skip parameter must be non-negative")
    if limit <= 0 or limit > 1000:
        raise InvalidInputException("Limit parameter must be between 1 and 1000")

    books = db.query(BookModel).offset(skip).limit(limit).all()
    return [BookResponse.from_orm(book) for book in books]


@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: UUID, book_update: BookUpdate, db: Session = Depends(get_db)):
    """Update a specific book by ID"""
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise BookNotFoundException(str(book_id))

    try:
        for key, value in book_update.model_dump(exclude_unset=True).items():
            if key in ["title", "author"] and value and not value.strip():
                raise InvalidInputException(f"{key} cannot be empty or whitespace only")
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

        return BookResponse.from_orm(book)
    except IntegrityError as e:
        db.rollback()
        raise InvalidInputException("Update violates database constraints")


@router.delete("/{book_id}")
async def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    """Delete a specific book by ID"""
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise BookNotFoundException(str(book_id))

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully", "book_id": str(book_id)}