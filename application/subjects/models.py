from application import db
from application.models import Base
from sqlalchemy.sql import text

class Subject(Base):

    name = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='subject', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_id_of_subject(subname):
        stmt = text("SELECT Subject.id FROM Subject"
                    " WHERE (Subject.name =:n)")
        res = db.engine.execute(stmt, n=subname)

        apu = 0

        response = -999
  
        for row in res:
            response = row.id
            apu = apu + 1

        if apu == 0:
            return -999
        else:
            return response
