from __future__ import annotations

import datetime

from sqlalchemy import Column, DateTime, Integer, Text

import sql
from src.models.base_model import BaseModel


class Tariff(BaseModel):
    __tablename__ = "tariffs"

    Id = Column(Integer, primary_key=True, autoincrement=True,)
    Tariff_id = Column(Integer, unique=True)
    Tariff_name = Column(Text)
    Data_start = Column(DateTime)
    Data_end = Column(DateTime)
    Number_of_min = Column(Integer)
    Number_of_sms = Column(Integer)
    Number_of_Mb = Column(Integer)

    @staticmethod
    def get_or_create(tariff_id: int = None,
                      tariff_name: str = None,
                      data_start: datetime = None,
                      data_end: datetime = None,
                      number_of_min: int = None,
                      number_of_sms: int = None,
                      number_of_mb: int = None,
                      ) -> Tariff:
        """
        Get or create instance of the User model.
        :param tariff_id:
        :param tariff_name:
        :param data_start:
        :param data_end:
        :param number_of_min:
        :param number_of_sms:
        :param number_of_mb:
        :return:
        """

        instance = sql.session.query(Tariff).filter(Tariff.Tariff_id == tariff_id).first()

        if instance is None:
            instance = Tariff(
                Tariff_id=tariff_id,
                Tariff_name=tariff_name,
                Data_start=data_start,
                Data_end=data_end,
                Number_of_min=number_of_min,
                Number_of_sms=number_of_sms,
                Number_of_Mb=number_of_mb,
            )
            sql.session.add(instance)
            sql.protected_commit()
        return instance
