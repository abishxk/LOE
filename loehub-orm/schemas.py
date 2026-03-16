from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class StaffingCreate(BaseModel):
    spec_filter: str
    req_id: str
    client: str
    project: str
    specialization: str
    resource: str
    status: str
    project_start_date: str