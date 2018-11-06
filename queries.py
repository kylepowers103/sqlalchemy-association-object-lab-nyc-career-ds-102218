from models import *

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

def query_experimentation(session):

    import pdb; pdb.set_trace()
