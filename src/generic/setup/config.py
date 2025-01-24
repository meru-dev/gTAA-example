from os import environ

from dotenv import load_dotenv
from pydantic import BaseModel, Field


class Config(BaseModel):
    base_url: str = Field(alias="BASE_URL")


load_dotenv()
config = Config(**environ)
