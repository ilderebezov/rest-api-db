from __future__ import annotations

import datetime

from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey

import sql
from src.models.base_model import BaseModel


class Event(BaseModel):
    __tablename__ = "events"

    Id = Column(Integer, primary_key=True, autoincrement=True, )
    Event_id = Column(Integer, unique=True)
    Time_event = Column(DateTime)
    User_id = Column(Integer, ForeignKey('users.User_id'))
    Service_type = Column(Text)
    Units_spent = Column(Integer)

    @staticmethod
    def get_or_create(event_id: int = None,
                      time_event: datetime = None,
                      user_id: int = None,
                      service_type: str = None,
                      units_spent: int = None,
                      ) -> Event:
        """
        Get or create instance of the User model.
        :param event_id:
        :param time_event:
        :param user_id:
        :param service_type:
        :param units_spent:
        :return:
        """

        instance = sql.session.query(Event).filter(Event.Event_id == event_id).first()

        if instance is None:
            instance = Event(
                Event_id=event_id,
                Time_event=time_event,
                User_id=user_id,
                Service_type=service_type,
                Units_spent=units_spent,
                )
            sql.session.add(instance)
            sql.protected_commit()
        return instance
