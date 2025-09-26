from App.database import db
from sqlalchemy import Enum
import enum

class PositionStatus(enum.Enum):
    open = "open"
    closed = "closed"

class Position(db.Model):
    __tablename__ = 'Position'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    duration_weeks = db.Column(db.Integer)
    requirements = db.Column(db.Text)
    number_of_positions = db.Column(db.Integer, default=1)
    status = db.Column(Enum(PositionStatus, native_enum=False), nullable=False, default=PositionStatus.open)
    employer_id = db.Column(db.Integer, db.ForeignKey('Employer.id'), nullable=False)
    employer = db.relationship("Employer", back_populates="positions")

    def __init__(self, title, employer_id):
        self.title = title
        self.employer_id = employer_id
        self.status = "open"
        

    def update_status(self, status):
        self.status = status
        db.session.commit()
        return self.status

    def update_duration(self, duration_weeks):
        self.duration_weeks = duration_weeks
        db.session.commit()
        return self.duration_weeks

    def update_requirements(self, requirements):
        self.requirements = requirements
        db.session.commit()
        return self.requirements

    def update_location(self, location):
        self.location = location
        db.session.commit()
        return self.location

    def update_start_date(self, start_date):
        self.start_date = start_date
        db.session.commit()
        return self.start_date

    def update_description(self, description):
        self.description = description
        db.session.commit()
        return self.description

    def update_number_of_positions(self, number_of_positions):
        self.number_of_positions = number_of_positions
        db.session.commit()
        return self.number_of_positions

    def delete_position(self):
        db.session.delete(self)
        db.session.commit()
        return

    def list_positions(self):
        return db.session.query(Position).all()