from App.database import db
from App.models.user import User

class Employer(User):
    __tablename__ = 'Employer'
    positions = db.relationship("Position", back_populates="employer")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.role = "employer"