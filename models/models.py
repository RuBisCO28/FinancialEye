from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class EdinetCodeInfo(Base):
    __tablename__ = 'edinetcodeinfo'
    edinetcode = Column(String(128), primary_key=True)
    capital = Column(Integer)
    fiscalperiod = Column(String(128))
    submitter = Column(String(128))
    businesstype = Column(String(128))
    securitiescode = Column(Integer)

    def __init__(self, edinetcode=None, capital=None, fiscalperiod=None, submitter=None, 
    businesstype=None, securitiescode=None):
        self.edinetcode = edinetcode
        self.capital = capital
        self.fiscalperiod = fiscalperiod
        self.submitter = submitter
        self.businesstype = businesstype
        self.securitiescode = securitiescode

    def __repr__(self):
        return '<Title %r>' % (self.edinetcode)
        
class FinanceInfo(Base):
    __tablename__ = 'financeinfo'
    rid = Column(Integer, primary_key=True)
    edinetcode = Column(String(128))
    securitiescode = Column(String(128))
    enddate = Column(String(128))
    netsales = Column(Integer)
    costofsales = Column(Integer)
    grossprofit = Column(Integer)
    sellinggeneral = Column(Integer)
    operatingincome = Column(Integer)
    nonoperatingincome = Column(Integer)
    nonoperatingexpenses = Column(Integer)
    ordinaryIncome = Column(Integer)
    extraordinaryincome = Column(Integer)
    extraordinaryloss = Column(Integer)
    incomebeforeincometaxes = Column(Integer)
    incometaxes = Column(Integer)
    profitloss = Column(Integer)

    def __init__(self, rid=None, edinetcode=None, securitiescode=None, enddate=None, netsales=None):
        self.rid = rid
        self.edinetcode = edinetcode
        self.securitiescode = securitiescode
        self.enddate = enddate
        self.netsales = netsales
        self.costofsales = costofsales
        self.grossprofit = grossprofit
        self.sellinggeneral = sellinggeneral
        self.operatingincome = operatingincome
        self.nonoperatingincome = nonoperatingincome
        self.nonoperatingexpenses = nonoperatingexpenses
        self.ordinaryIncome = ordinaryIncome
        self.extraordinaryincome = extraordinaryincome
        self.extraordinaryloss = extraordinaryloss
        self.incomebeforeincometaxes = incomebeforeincometaxes
        self.incometaxes = incometaxes
        self.profitloss = profitloss
        
    def __repr__(self):
        return '<Title %r>' % (self.edinetcode)

