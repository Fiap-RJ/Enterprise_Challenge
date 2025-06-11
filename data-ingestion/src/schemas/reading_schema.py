from pydantic import BaseModel, Field
from typing import Annotated


class ReadingSchema(BaseModel):
    temperatura: Annotated[
        float, Field(example=25.0, description="Temperatura em graus Celsius")
    ]
    umidade: Annotated[
        float, Field(gt=0, lt=100, example=45.0, description="Umidade em porcentagem")
    ]
