from App.database import db
from App.models.user import User

class Employer(User):
    __tablename__ = 'Employer'
    email = db.Column(db.String(255), unique=True)
    company_website = db.Column(db.String(255))
    description = db.Column(db.Text)
    industry = db.Column(db.String(100))
    location = db.Column(db.String(100))
    positions = db.relationship("Position", back_populates="employer")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.role = "employer"