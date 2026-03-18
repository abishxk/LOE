from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class StaffingRequest(Base):
    __tablename__ = "staffing_requests"
    staffId = Column(Integer, primary_key=True)
    reqId = Column(String)
    client = Column(String)
    project = Column(String)
    specialization = Column(String)
    status = Column(String)
    projectStartDate = Column(String)

class KPI(Base):
    __tablename__ = "kpi"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)


class Graph(Base):
    __tablename__ = "graph"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)


class ActionRequired(Base):
    __tablename__ = "action_required"
    id = Column(Integer, primary_key=True)
    reqId = Column(String)
    client = Column(String)
    type = Column(String)
    specialization = Column(String)
    status = Column(String)
    sla = Column(String)