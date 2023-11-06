from sqlalchemy import Column, Integer, String, create_engine, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from players import Players
from matches import Matches


Base = declarative_base()

name_index = Index("name_index", Players.name)

connection_string = "mysql+pymysql://root:KUku1212_b2zZ@localhost/tennis"
engine = create_engine(url=connection_string, echo=False)
Base.metadata.create_all(engine)