# -*- coding: utf-8 -*-

"""
    core.db
    ~~~~~~~
    Database handlers.
"""

import os
import envkey  # NOQA
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = os.environ.get('POSTGRES_USER')
db_pass = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('POSTGRES_HOST')

dsn = f"postgresql+psycopg2://{ db_user }:{ db_pass }@{ db_host }/{ db_name }"

db = create_engine(dsn)

DBSession = sessionmaker(bind=db)
session = DBSession()
