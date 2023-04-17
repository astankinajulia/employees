from typing import List

from db.service import EmployeeDBService, EmployeeSchema


def get_subordinates_recursively(employee: EmployeeSchema, res: dict):
    """ Recursive employee tree generation. """
    res['subordinates'][employee.id] = {
        'full_name': employee.full_name,
        'job_title': employee.job_title,
        'salary': employee.salary,
        'subordinates': {},
    }

    subs: List[EmployeeSchema] = EmployeeDBService.get_subordinates(employee.id)
    for sub in subs:
        get_subordinates_recursively(sub, res['subordinates'][employee.id])
