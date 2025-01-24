from typing import Any

from pydantic import BaseModel


class BaseBody(BaseModel):
    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()
