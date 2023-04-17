import aiohttp_jinja2

from db.service import EmployeeDBService
from helpers import get_subordinates_recursively


@aiohttp_jinja2.template('index.html')
async def index(request):
    """ Get hierarchy of employees in a tree form. """
    employees = EmployeeDBService.employees_without_bosses()
    result = {}
    for employee in employees:
        res = {
            'subordinates': {}
        }
        get_subordinates_recursively(employee, res)
        result.update(res['subordinates'])
    return {'data': result}
