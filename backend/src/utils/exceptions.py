from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Dict, Any


class BookNotFoundException(Exception):
    """Raised when a book is not found in the database"""
    def __init__(self, book_id: str):
        self.book_id = book_id
        super().__init__(f"Book with ID {book_id} not found")


class DatabaseConnectionException(Exception):
    """Raised when there's an issue connecting to the database"""
    def __init__(self):
        super().__init__("Failed to connect to the database")


class InvalidInputException(Exception):
    """Raised when invalid input is provided to an endpoint"""
    def __init__(self, message: str):
        super().__init__(message)


async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Custom handler for HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "type": "HTTPException",
                "message": exc.detail
            }
        }
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom handler for validation errors"""
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "type": "ValidationError",
                "message": "Input validation failed",
                "details": exc.errors()
            }
        }
    )


async def book_not_found_exception_handler(request: Request, exc: BookNotFoundException):
    """Custom handler for book not found errors"""
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "type": "BookNotFound",
                "message": str(exc),
                "book_id": exc.book_id
            }
        }
    )


async def database_connection_exception_handler(request: Request, exc: DatabaseConnectionException):
    """Custom handler for database connection errors"""
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "type": "DatabaseConnectionError",
                "message": str(exc)
            }
        }
    )


async def invalid_input_exception_handler(request: Request, exc: InvalidInputException):
    """Custom handler for invalid input errors"""
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "type": "InvalidInput",
                "message": str(exc)
            }
        }
    )


def add_exception_handlers(app: FastAPI):
    """Add all custom exception handlers to the FastAPI app"""
    app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(BookNotFoundException, book_not_found_exception_handler)
    app.add_exception_handler(DatabaseConnectionException, database_connection_exception_handler)
    app.add_exception_handler(InvalidInputException, invalid_input_exception_handler)