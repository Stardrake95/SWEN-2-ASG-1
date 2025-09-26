from App.models import Position, Employer
from App.database import db

def open_position(title, employer_id):
    employer = db.session.query(Employer).filter_by(id=employer_id).first()
    if employer:
        new_position = Position(title=title, employer_id=employer_id)
        db.session.add(new_position)
        db.session.commit()
        return new_position
    return False