import os
import utils.user as userdb
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_HOST = os.getenv('HOST')

address = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = db.create_engine(address)
connection = engine.connect()
metadata = db.MetaData()    # Used for representing a Table

# Creates a new session to the database based on the described engine
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

    # Allows us to print out a User object nicely
    def __repr__(self):
        text = ("<User(name='{self.name}', discord_id='{self.discord_id}',"
            "level='{self.level}', experience='{self.experience}',"
            "message_count='{self.message_count}')")
        return text

# Create the table
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


def update_user(id: str, name: str = None, lvl: int = None,
                exp: int = None, msg_count: int = None):
    '''
    Updates user data in the database.
    All the other parameters besides 'id' are optional.
    '''
    session = Session()
    if user_exists(id):
        try:
            user = session.query(User).filter(User.discord_id == id).scalar()
        except MultipleResultsFound:
            print(
                "Duplicate discord_id's were found! Please check the database."
            )
        else:
            parameters = [name, lvl, exp, msg_count]
            # Column header names of the User table
            col_names = ["name" , "level", "experience", "message_count"]
            # Updates the parameters that were specified to the database
            for var, col in zip(parameters, col_names):
                if var is not None:
                    setattr(user, col, var)
                    session.commit()
                    print(f"The {col} of user: {id} has been updated to {var}.")
        return
    print("User was not found.")

def delete_user(id):
    '''
    Deletes a user from the database.
    '''
    session = Session()
    if user_exists(id):
        query = session.query(User).filter(
            User.discord_id == id).scalar()
        session.delete(query)
        session.commit()
        print(
            f"User with the discord_id of {id} has been deleted from the "
            "database."
        )  
        return
    print(f"User {id} was not found.")

def user_exists(id):
    '''
    Checks to see if a user exists in the database baed on their discord_id. 
    Returns true if user exists. Returns false if user does not exist.
    '''
    session = Session()
    # Queries just the discord_ids, not the entire object
    try:
        query = session.query(User.discord_id).filter(
        User.discord_id == id).scalar() is not None
    except MultipleResultsFound:
        print("Duplicate discord_id's were found! Please check the database.")
    else:
        return query

def get_user(id):
    '''
    Retrieves data about a user from database.
    Returns a dict containing user information.
    '''
    session = Session()
    if user_exists(id):
        user = session.query(User).filter(
            User.discord_id == id).scalar()
        return {"name": user.name, "discord_id": user.discord_id,
                "level": user.level, "experience": user.experience,
                "message_count": user.message_count}
    print("User was not found.")

def get_all_users():
    '''
    Retrieves data about every user.
    Returns an array of tuples with every user's data.
    '''
    user_table = db.Table(
        'users', metadata, autoload=True, autoload_with=engine)
    query = db.select([user_table])
    results = connection.execute(query)
    result_set = results.fetchall()
    return result_set

def get_user_count():
    '''
    Returns the total number of users in the database.
    '''
    session = Session()
    return session.query(User).count()

def reset_table_index():
    pass

def check_duplicates():
    '''
    Check database for duplicate discord_id's
    '''
    pass