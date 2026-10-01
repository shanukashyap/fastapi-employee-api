from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import schemas
from . import crud
from . import models
from .auth import verify_api_key


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Employee Management API",
    description="""
    Employee Management API protected with API Key Authentication.

    Features:
    - Create employees
    - View employees
    - Update employees
    - Delete employees
    - API key authentication
    - Pydantic validation
    """,
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Employee Management API is running",
        "docs": "/docs"
    }


@app.get(
    "/employees",
    response_model=list[schemas.EmployeeResponse],
    dependencies=[Depends(verify_api_key)]
)
def get_employees(
    db: Session = Depends(get_db)
):

    return crud.get_employees(db)


@app.post(
    "/employees",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)]
)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    existing_employee = db.query(
        models.Employee
    ).filter(
        models.Employee.email == employee.email
    ).first()

    if existing_employee:

        raise HTTPException(
            status_code=400,
            detail="Employee with this email already exists"
        )

    return crud.create_employee(
        db,
        employee
    )


@app.put(
    "/employees/{employee_id}",
    response_model=schemas.EmployeeResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):

    existing_employee = crud.get_employee(
        db,
        employee_id
    )

    if not existing_employee:

        raise HTTPException(
            status_code=404,
            detail=f"Employee {employee_id} not found"
        )

    return crud.update_employee(
        db,
        employee_id,
        employee
    )


@app.delete(
    "/employees/{employee_id}",
    dependencies=[Depends(verify_api_key)]
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted_employee = crud.delete_employee(
        db,
        employee_id
    )

    if not deleted_employee:

        raise HTTPException(
            status_code=404,
            detail=f"Employee {employee_id} not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }