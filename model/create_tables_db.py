from database import Base, engine


def create_tables():
    # engine.echo = True
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # engine.echo = True

create_tables()