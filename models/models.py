from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class EdinetCodeInfo(Base):
    __tablename__ = 'edinetcodeinfo'
    securitiescode = Column((Integer), primary_key=True)
    fiscalperiod = Column(String(128))
    submitter = Column(String(128))
    businesstype = Column(String(128))
    tosho = Column(String(128))
    description = Column(String(128))

    def __init__(self, securitiescode=None, fiscalperiod=None, submitter=None, 
    businesstype=None, tosho=None, description=None):
        self.securitiescode = securitiescode
        self.fiscalperiod = fiscalperiod
        self.submitter = submitter
        self.businesstype = businesstype
        self.tosho = tosho
        self.description = description

    def __repr__(self):
        return '<Title %r>' % (self.edinetcode)
