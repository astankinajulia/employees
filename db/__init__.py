import inspect
import sys

from config import config
from db.base import *
from db.models import *


def get_tables():
    return [
        x for _, x in
        inspect.getmembers(sys.modules[__name__], inspect.isclass)
        if issubclass(x, BaseModel) and x not in [BaseModel]
    ]


def start():
    """
    Init database
    """

    psql_db.init(
        database=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )

    psql_db.create_tables(
        [t for t in get_tables() if not t.table_exists()],
        safe=True,
    )
