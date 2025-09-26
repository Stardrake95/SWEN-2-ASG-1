from sqlalchemy import false
from App.models import Shortlist, Position, Staff
from App.database import db

def add_student_to_shortlist(student_id, position_id, staff_id):
    is_open = db.session.query(Position).filter_by(id=position_id, status='open').first()
    list = db.session.query(Shortlist).filter_by(student_id=student_id, position_id=position_id).first()
    teacher = db.session.query(Staff).filter_by(id=staff_id).first()
    position = db.session.query(Position).filter(Position.id==position_id, Position.number_of_positions > 0).first()
    if is_open and teacher and not list and position:
        shortlist = Shortlist(student_id=student_id, position_id=position_id, staff_id=staff_id)
        db.session.add(shortlist)
        db.session.commit()
        return shortlist
    return False

def decide_shortlist(student_id, position_id, decision):
    shortlist = db.session.query(Shortlist).filter_by(student_id=student_id, position_id=position_id, status ="pending").first()
    position = db.session.query(Position).filter(Position.id==position_id, Position.number_of_positions > 0).first()
    if shortlist and position:
        shortlist.update_status(decision)
        position.update_number_of_positions(position.number_of_positions - 1)
        return shortlist
    return False


def get_shortlist_by_student(student_id):
    return db.session.query(Shortlist).filter_by(student_id=student_id).all()
    
  
    