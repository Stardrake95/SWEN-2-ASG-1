from App.database import db
from App.models.user import User
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date

class Student(User):
    __tablename__ = 'Student'
    email = db.Column(db.String(256))
    DOB = db.Column(db.Date)
    gender = db.Column(db.String(256))
    degree = db.Column(db.String(256))
    phone = db.Column(db.String(256))
    GPA = db.Column(db.Float)
    resume = db.Column(db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.role = "student"

    def update_DOB(self, date):
        self.DOB = date
        db.session.commit()
        return self.DOB
        
    @hybrid_property
    def age(self):
        if self.DOB is None:
            return None
        today = date.today()
        dob = self.DOB
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))