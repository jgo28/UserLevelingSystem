import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
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
