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
    ordinaryincome = Column(Integer)
    extraordinaryincome = Column(Integer)
    extraordinaryloss = Column(Integer)
    incomebeforeincometaxes = Column(Integer)
    incometaxes = Column(Integer)
    profitloss = Column(Integer)
    currentassets = Column(Integer)
    noncurrentassets = Column(Integer)
    propertyplantandequipment = Column(Integer)
    intangibleassets = Column(Integer)
    investmentsAndotherAssets = Column(Integer)
    currentliabilities = Column(Integer)
    noncurrentliabilities = Column(Integer)
    netAssets = Column(Integer)
    scf = Column(Integer)
    icf = Column(Integer)
    fcf = Column(Integer)

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
        self.ordinaryincome = ordinaryincome
        self.extraordinaryincome = extraordinaryincome
        self.extraordinaryloss = extraordinaryloss
        self.incomebeforeincometaxes = incomebeforeincometaxes
        self.incometaxes = incometaxes
        self.profitloss = profitloss
        self.currentassets = currentassets
        self.noncurrentassets = noncurrentassets
        self.propertyplantandequipment = propertyplantandequipment
        self.intangibleassets = intangibleassets
        self.investmentsAndotherAssets = investmentsAndotherAssets
        self.currentliabilities = currentliabilities
        self.noncurrentliabilities = noncurrentliabilities
        self.netAssets = netAssets
        self.scf = scf
        self.icf = icf
        self.fcf = fcf
        
class Stocks(Base):
    __tablename__ = 'stocks'
    pkey = Column(String(128), primary_key=True)
    date = Column(String(128))
    open = Column(Integer)
    high = Column(Integer)
    low = Column(Integer)
    close = Column(Integer)
    volume = Column(Integer)
    endv = Column(Integer)
    code = Column(Integer)

    def __init__(self, date=None):
        self.pkey = pkey
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.endv = endv
        self.code = code


