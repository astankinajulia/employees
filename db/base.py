from peewee import AutoField, Model, PostgresqlDatabase

psql_db = PostgresqlDatabase(None)


class BaseModel(Model):
    id = AutoField(primary_key=True)

    class Meta:
        database = psql_db
