from backend.database.db import Base, engine

from backend.models import *


print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully")