from src.utils.db_init import init_db
from src.main import run_dev_server


def main():
    # Initialize the database
    init_db()

    # Start the development server
    print("Starting AI-Native Book Backend...")
    run_dev_server()


if __name__ == "__main__":
    main()