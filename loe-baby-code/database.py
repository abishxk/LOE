from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseModule:

    def __init__(self):
        self.connection = None
        self.SessionLocal = None

    def initialize_connection(self):
        url = "postgresql://postgres:root%40123@localhost:5432/loehub"
        engine = create_engine(url)
        self.SessionLocal = sessionmaker(bind=engine)
        self.connection = engine
        print("Database Connected")

    def get_session(self):
        return self.SessionLocal()

    def close_connection(self):
        print("Database connection closed")