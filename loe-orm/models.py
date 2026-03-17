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