from src.database.session import engine
from src.models.book import Base


def init_db():
    """Initialize the database and create tables"""
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()