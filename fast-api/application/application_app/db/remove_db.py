from sqlalchemy import text
from database  import SessionLocal


def remove_db():
    session = SessionLocal()

    try:
        # Disable foreign key checks temporarily (if needed)
        session.execute(text("SET session_replication_role = replica;"))

        # Drop the current schema (be very careful with this command)
        session.execute(text("DROP SCHEMA public CASCADE;"))

        # Recreate an empty schema
        session.execute(text("CREATE SCHEMA public;"))

        # Enable foreign key checks again (if they were disabled)
        session.execute(text("SET session_replication_role = DEFAULT;"))

        # Commit the transaction to apply the changes
        session.commit()

        print("All content removed from the database.")
    except Exception as e:
        session.rollback()
        print(f"Error: {str(e)}")
    finally:
        session.close()


if __name__ == "__main__":
    # This code block will only execute if the script is run directly
    remove_db()
