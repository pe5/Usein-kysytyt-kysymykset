from application import db
from application.models import Base
from sqlalchemy.sql import text

class Subject(Base):

    name = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='subject', lazy=True)

    def __init__(self, name):
        self.name = name
