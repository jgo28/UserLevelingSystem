import os
import sqlalchemy as db
import utils.user as userdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_HOST = os.getenv('HOST')

address = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = db.create_engine(address, echo=True)
connection = engine.connect()
metadata = db.MetaData()

Session = sessionmaker(bind=engine)


# Define and create the User table
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    discord_id = db.Column(db.String(length=50))
    name = db.Column(db.String(length=50))
    level = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    message_count = db.Column(db.Integer)

    def __repr__(self):
        text = ("<User(name='{self.name}', discord_id='{self.discord_id}',"
            "level='{self.level}', experience='{self.experience}',"
            "message_count='{self.message_count}')")
        return text

Base.metadata.create_all(engine)


def add_user(id, name, lvl, exp, msg_count):
    '''
    Adds a new user to the database.
    '''
    session = Session()
    if not user_exists(id):   
        # If discord_id doesn't exist, add the user
        new_user = User(
            discord_id=id,
            name=name,
            level=lvl,
            experience=exp,
            message_count=msg_count
        )
        session.add(new_user)
        session.commit()
        print(f"{id}:{name} has been added to the database.")
        return
    print(
        f"{id}:{name} wasn't added because their discord_id " 
        "already exists in the database!"
    )
    return


def update_user(id, name, lvl, exp, msg_count):
    pass


def user_exists(id):
    '''
    Checks to see if a user exists in the database baed on their discord_id. 
    Returns true if user exists. Returns false if user does not exist.
    '''
    session = Session()
    # Queries just the discord_ids, not the entire object
    query = session.query(User.discord_id).filter(
        User.discord_id == id).scalar() is not None
    return query

def get_user_count():
    '''
    Returns the total number of users in the database.
    '''
    session = Session()
    return session.query(User).count()

def get_all_users():
    '''
    Returns an array of tuples with user data.
    '''
    user_table = db.Table(
        'users', metadata, autoload=True, autoload_with=engine)
    query = db.select([user_table])
    results = connection.execute(query)
    result_set = results.fetchall()
    return result_set
