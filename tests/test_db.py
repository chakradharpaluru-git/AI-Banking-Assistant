import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from backend.database.db import engine


def test_database_connection():

    try:
        connection = engine.connect()

        print("✅ DATABASE CONNECTED SUCCESSFULLY")

        connection.close()

    except Exception as e:

        print("❌ DATABASE CONNECTION FAILED")
        print(e)


if __name__ == "__main__":
    test_database_connection()