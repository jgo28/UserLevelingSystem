import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker
from utils.database.models import Users
from sqlalchemy.orm.exc import MultipleResultsFound


class Methods:
    '''
    Functions that manipulate the Users database.
    '''
    def __init__(self, engine, metadata, connection):
        self.engine = engine
        self.metadata = metadata
        self.connection = connection
        # Creates a new session to the database based on the described engine
        self.session = sessionmaker(bind=self.engine)

    def add_user(self, id, name, lvl, exp, msg_count):
        '''
        Adds a new user to the database.
        '''
        session = self.session()
        if not self.user_exists(id):
            # If discord_id doesn't exist, add the user
            new_user = Users(
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

    def update_user(self, id: str, name: str = None, lvl: int = None,
                    exp: int = None, msg_count: int = None):
        '''
        Updates user data in the database.
        All the other parameters besides 'id' are optional.
        '''
        session = self.session()
        if self.user_exists(id):
            try:
                user = session.query(Users).filter(
                    Users.discord_id == id).scalar()
            except MultipleResultsFound:
                print(
                    "Duplicate discord_id's were found! "
                    "Please check the database."
                )
            else:
                parameters = [name, lvl, exp, msg_count]
                # Column header names of the Users table
                col_names = ["name", "level", "experience", "message_count"]
                # Updates the parameters that were specified to the database
                for var, col in zip(parameters, col_names):
                    if var is not None:
                        setattr(user, col, var)
                        session.commit()
                        print(
                            f"The {col} of user: {id} "
                            f"has been updated to {var}."
                        )
            return
        print("User was not found.")

    def delete_user(self, id):
        '''
        Deletes a user from the database.
        '''
        session = self.session()
        if self.user_exists(id):
            query = session.query(Users).filter(
                Users.discord_id == id).scalar()
            session.delete(query)
            session.commit()
            print(
                f"Users with the discord_id of {id} has been deleted from the "
                "database."
            )
            return
        print(f"User {id} was not found.")

    def delete_all(self):
        '''
        Deletes all the users from the database.
        '''
        session = self.session()
        if self.get_user_count() == 0:
            print("Table is already empty!")
            return
        session.query(Users).delete()
        session.commit()
        print("All the users in the table have been deleted.")

    def user_exists(self, id):
        '''
        Checks to see if a user exists based on their discord_id.
        Returns true if user exists. Returns false if user does not exist.
        '''
        session = self.session()
        # Queries just the discord_ids, not the entire object
        try:
            query = session.query(Users.discord_id).filter(
                Users.discord_id == id).scalar() is not None
        except MultipleResultsFound:
            print(
                "Duplicate discord_id's were found! "
                "Please check the database."
            )
        else:
            return query

    def get_user(self, id):
        '''
        Retrieves data about a user from database.
        Returns a dict containing user information.
        '''
        session = self.session()
        if self.user_exists(id):
            user = session.query(Users).filter(
                Users.discord_id == id).scalar()
            return {"name": user.name, "discord_id": user.discord_id,
                    "level": user.level, "experience": user.experience,
                    "message_count": user.message_count}
        print("User was not found.")

    def get_all_users(self):
        '''
        Retrieves data about every user.
        Returns an array of tuples with every user's data.
        '''
        user_table = sqla.Table(
            'users', self.metadata, autoload=True, autoload_with=self.engine)
        query = sqla.select([user_table])
        results = self.connection.execute(query)
        result_set = results.fetchall()
        return result_set

    def get_user_count(self):
        '''
        Returns the total number of users in the database.
        '''
        session = self.session()
        return session.query(Users).count()
