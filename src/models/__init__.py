import sql
from src.models.base_model import BaseModel
from src.models.users import User
from src.models.tariffs import Tariff
from src.models.events import Event

BaseModel.metadata.create_all(sql.client)
