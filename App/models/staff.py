from App.database import db
from App.models.user import User
from App.models.shortlist import Shortlist

class Staff(User):
    __tablename__ = 'Staff'

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.role = "staff"

    def add_to_shortlist(self, student_id, position_id):
        shortlist = Shortlist(student_id=student_id, position_id=position_id, staff_id=self.id)
        db.session.add(shortlist)
        db.session.commit()
        return shortlist