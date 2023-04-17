import dataclasses
from typing import List

from db import Employee


@dataclasses.dataclass
class EmployeeSchema:
    id: int
    full_name: str
    job_title: str
    salary: float
    boss_id: int


class EmployeeDBService:
    """ Service for work with employee table. """

    @staticmethod
    def employees_without_bosses() -> List[EmployeeSchema]:
        """ Get employees without bosses. """
        employees: List[Employee] = Employee.select().where(
            Employee.boss_id.is_null()
        )
        return [
            EmployeeSchema(
                id=employee.id,
                full_name=employee.full_name,
                job_title=employee.job_title,
                salary=employee.salary,
                boss_id=employee.boss_id,
            ) for employee in employees
        ]

    @staticmethod
    def get_subordinates(boss_id) -> List[EmployeeSchema]:
        """ Get all subordinates of an employee. """
        employees: List[Employee] = Employee.select().where(
            Employee.boss_id == boss_id
        )
        return [
            EmployeeSchema(
                id=employee.id,
                full_name=employee.full_name,
                job_title=employee.job_title,
                salary=employee.salary,
                boss_id=employee.boss_id,
            ) for employee in employees
        ]
