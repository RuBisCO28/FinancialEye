from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class EdinetCodeInfo(Base):
    __tablename__ = 'edinetcodeinfo'
    edinetcode = Column(String(128), primary_key=True)
    fiscalperiod = Column(String(128))
    submitter = Column(String(128))
    businesstype = Column(String(128))
    securitiescode = Column(Integer)
    url = Column(String(128))
    description = Column(String(128))

    def __init__(self, edinetcode=None, fiscalperiod=None, submitter=None, 
    businesstype=None, securitiescode=None, url=None, description=None):
        self.edinetcode = edinetcode
        self.fiscalperiod = fiscalperiod
        self.submitter = submitter
        self.businesstype = businesstype
        self.securitiescode = securitiescode
        self.url = url
        self.description = description

    def __repr__(self):
        return '<Title %r>' % (self.edinetcode)
