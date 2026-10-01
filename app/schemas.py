from pydantic import BaseModel, EmailStr, Field, ConfigDict


class EmployeeCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    department: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    salary: float = Field(
        ...,
        gt=0
    )


class EmployeeUpdate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    department: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    salary: float = Field(
        ...,
        gt=0
    )


class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    department: str
    designation: str
    salary: float

    model_config = ConfigDict(
        from_attributes=True
    )