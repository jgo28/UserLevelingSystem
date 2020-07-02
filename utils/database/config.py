import os
import sqlalchemy as sqla
from dotenv import load_dotenv
from utils.database.models import Base

load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_HOST = os.getenv('HOST')

e = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = sqla.create_engine(e)
connection = engine.connect()
metadata = sqla.MetaData()    # Used for representing a Table
# Create the table
Base.metadata.create_all(engine)


def get_metadata():
    return metadata


def get_engine():
    return engine


def get_connection():
    return connection
