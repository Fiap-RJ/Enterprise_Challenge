from pydantic import BaseModel, Field
from typing import Annotated


class ReadingSchema(BaseModel):
    temperature_c: Annotated[
        float, Field(example=25.0, description="Temperatura em graus Celsius")
    ]
    humidity_pct: Annotated[
        float, Field(gt=0, lt=100, example=45.0, description="Umidade em porcentagem")
    ]
