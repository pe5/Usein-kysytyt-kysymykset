from application import db
from application.models import Base
from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = "Ei vastattu"

    @staticmethod
    def find_questions_with_no_answers():
        stmt = text("SELECT Task.id, Task.name FROM Task"
                    " WHERE (Task.done = '')")
        res = db.engine.execute(stmt)

        response = []
  
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
