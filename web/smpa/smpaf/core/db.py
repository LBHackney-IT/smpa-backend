import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


db_user = os.environ.get('POSTGRES_USER')
db_pass = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('POSTGRES_HOST')


dsn = f"postgresql+psycopg2://{ db_user }:{ db_pass }@{ db_host }/{ db_name }"

engine = create_engine(dsn)

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)
