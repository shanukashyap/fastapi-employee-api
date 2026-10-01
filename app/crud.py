from sqlalchemy.orm import Session

from . import models


def create_employee(
    db: Session,
    employee_data
):

    employee = models.Employee(
        name=employee_data.name,
        email=employee_data.email,
        department=employee_data.department,
        designation=employee_data.designation,
        salary=employee_data.salary
    )

    db.add(employee)

    db.commit()

    db.refresh(employee)

    return employee


def get_employees(db: Session):

    return db.query(
        models.Employee
    ).all()


def get_employee(
    db: Session,
    employee_id: int
):

    return db.query(
        models.Employee
    ).filter(
        models.Employee.id == employee_id
    ).first()


def update_employee(
    db: Session,
    employee_id: int,
    employee_data
):

    employee = get_employee(
        db,
        employee_id
    )

    if not employee:
        return None

    employee.name = employee_data.name
    employee.email = employee_data.email
    employee.department = employee_data.department
    employee.designation = employee_data.designation
    employee.salary = employee_data.salary

    db.commit()

    db.refresh(employee)

    return employee


def delete_employee(
    db: Session,
    employee_id: int
):

    employee = get_employee(
        db,
        employee_id
    )

    if not employee:
        return None

    db.delete(employee)

    db.commit()

    return employee