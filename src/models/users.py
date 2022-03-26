from __future__ import annotations

import datetime

from sqlalchemy import Column, DateTime, Integer, Text, Float, ForeignKey

import sql
from src.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    Id = Column(Integer, primary_key=True, autoincrement=True,)
    User_id = Column(Integer, unique=True)
    Balance = Column(Float)
    Data_adding = Column(DateTime)
    Age = Column(Integer)
    City_of_living = Column(Text)
    Data_last_activity = Column(DateTime)
    Current_tariff = Column(Integer, ForeignKey('tariffs.Tariff_id'))

    @staticmethod
    def get_or_create(user_id: int = None,
                      balance: float = None,
                      data_adding: datetime = None,
                      age: int = None,
                      city_of_living: str = None,
                      data_last_activity: datetime = None,
                      current_tariff: int = None,) -> User:
        """
        Get or create instance of the User model.
        :param user_id:
        :param balance:
        :param data_adding:
        :param age:
        :param city_of_living:
        :param data_last_activity:
        :param current_tariff:
        :return:
        """

        instance = sql.session.query(User).filter(User.User_id == user_id).first()

        if instance is None:
            instance = User(
                User_id=user_id,
                Balance=balance,
                Data_adding=data_adding,
                Age=age,
                City_of_living=city_of_living,
                Data_last_activity=data_last_activity,
                Current_tariff=current_tariff,
            )
            sql.session.add(instance)
            sql.protected_commit()
        return instance
