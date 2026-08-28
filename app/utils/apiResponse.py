from datetime import datetime, timezone
from typing import Generic, TypeVar
from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class StudentResponse(BaseModel, Generic[DataT]):
    success: bool = True
    statusCode: int = 200
    message: str = "Ok"
    data: DataT | None = None
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )