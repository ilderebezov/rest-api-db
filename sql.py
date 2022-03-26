#import os

#import dotenv

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

client = create_engine('sqlite:///MF.db')
session = Session(client)


def protected_commit():
    """
    Method to create protected commit in data base, in a case troubles during commit
    the will be canceled and there is no any data will be added to data base.
    :return:
    """
    try:
        session.commit()
        session.close()
    except Exception as error:
        logger.error(str(error))
        session.rollback()
        raise error
