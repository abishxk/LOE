from sqlalchemy import Column, Integer, String
from db_connection import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class KPI(Base):
    __tablename__ = "kpi"
    kpi_id = Column(Integer, primary_key=True)
    kpi_name = Column(String)
    kpi_value = Column(Integer)


class Graph(Base):
    __tablename__ = "graphs"
    graph_id = Column(Integer, primary_key=True)
    graph_name = Column(String)
    graph_filter = Column(String)
    graph_value = Column(Integer)


class ActionRequired(Base):
    __tablename__ = "action_required"
    action_id = Column(Integer, primary_key=True)
    req_id = Column(String)
    client = Column(String)
    type = Column(String)
    specialization = Column(String)
    status = Column(String)
    sla = Column(String)


class StaffingRequest(Base):
    __tablename__ = "staffing_requests"
    staff_id = Column(Integer, primary_key=True)
    spec_filter = Column(String)
    req_id = Column(String)
    client = Column(String)
    project = Column(String)
    specialization = Column(String)
    resource = Column(String)
    status = Column(String)
    project_start_date = Column(String)