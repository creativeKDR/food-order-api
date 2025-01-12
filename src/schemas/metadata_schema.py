from pydantic import BaseModel, Field


class MetaDataResponse(BaseModel):
    id: int = Field(None, alias='id')
    name: str = Field(None, alias='name')
    display_name: str = Field(None, alias='display_name')

    class Config:
        orm_mode = True
