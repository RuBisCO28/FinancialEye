from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class EdinetCodeInfo(Base):
    __tablename__ = 'edinetcodeinfo'
    edinetcode = Column(String(128), primary_key=True)
    submittype = Column(String(128))
    listingtype = Column(String(128))
    holding = Column(String(128))
    capital = Column(Integer)
    fiscalperiod = Column(String(128))
    submitter = Column(String(128))
    submitteren = Column(String(128))
    submitteryomi = Column(String(128))
    location = Column(String(128))
    businesstype = Column(String(128))
    securitiescode = Column(Integer)
    corpnumber = Column(Integer)

    def __init__(self, edinetcode=None, submittype=None, listingtype=None, holding=None, capital=None,
    fiscalperiod=None, submitter=None, submitteren=None, submitteryomi=None, location=None, businesstype=None, 
    securitiescode=None, corpnumber=None):
        self.edinetcode = edinetcode
        self.submittype = submittype
        self.listingtype = listingtype
        self.holding = holding
        self.capital = capital
        self.fiscalperiod = fiscalperiod
        self.submitter = submitter
        self.submitteren = submitteren
        self.submitteryomi = submitteryomi
        self.location = location
        self.businesstype = businesstype
        self.securitiescode = securitiescode
        self.corpnumber = corpnumber

    def __repr__(self):
        return '<Title %r>' % (self.edinetcode)
