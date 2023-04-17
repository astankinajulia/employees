from peewee import CharField, DateField, FloatField, IntegerField

from db.base import BaseModel


class Employee(BaseModel):
    full_name = CharField(max_length=80, null=False)
    job_title = CharField(max_length=80, null=False)
    start_date = DateField(null=False)
    salary = FloatField(null=False)
    boss_id = IntegerField(null=True)
