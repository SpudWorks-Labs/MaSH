from peewee import *

# 1. Define the database file
db = SqliteDatabase('database.db')

# 2. Define the Base Model to avoid repeating the database config
class BaseModel(Model):
    class Meta:
        database = db

# 3. Define your actual workforce tables
class Project(BaseModel):
    name = CharField(unique=True) # Peewee handles the NOT NULL by default
    path = CharField()
    repos = CharField(null=True)

class AIModel(BaseModel): 
    # Renamed to AIModel to avoid confusion with peewee.Model
    name = CharField(unique=True)
    body = TextField()
    model = CharField()

# Map strings to classes for your helper functions
TABLE_MAP = {
    'projects': Project,
    'models': AIModel
}


def init_database():
    """Create tables if they don't exist."""
    with db:
        db.create_tables([Project, AIModel])


def insert_database(table, payload):
    """
    Programmatically insert data.
    Usage: insert_database('projects', {'name': 'MaSH', 'path': '/usr/bin'})
    """
    model_class = TABLE_MAP.get(table)
    if model_class:
        # **payload unpacks the dictionary into keyword arguments

        return model_class.create(**payload)


def read_database(table):
    """Returns all records as a list of dictionaries."""
    model_class = TABLE_MAP.get(table)
    if model_class:
        # .dicts() converts model objects back into readable dictionaries
        return list(model_class.select().dicts())

    return []


def update_database(table, name, values):
    """
    Updates a record by its name.
    Usage: update_database('projects', 'OldName', {'path': '/new/path'})
    """
    model_class = TABLE_MAP.get(table)
    if model_class:
        query = model_class.update(**values).where(model_class.name == name)

        return query.execute()


def remove_database(table, name):
    """Deletes a record by name."""
    model_class = TABLE_MAP.get(table)
    if model_class:
        query = model_class.delete().where(model_class.name == name)
        
        return query.execute()
