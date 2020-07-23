# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field


class Pet(BaseModel):
    id_: int = Field(..., alias='id')
    name_: str = Field(..., alias='name')
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class User(BaseModel):
    id_: int = Field(..., alias='id')
    name_: str = Field(..., alias='name')
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class Api(BaseModel):
    apiKey: Optional[str] = Field(
        None, description='To be used as a dataset parameter value'
    )
    apiVersionNumber: Optional[str] = Field(
        None, description='To be used as a version parameter value'
    )
    apiUrl: Optional[AnyUrl] = Field(
        None, description="The URL describing the dataset's fields"
    )
    apiDocumentationUrl: Optional[AnyUrl] = Field(
        None, description='A URL to the API console for each API'
    )


class Apis(BaseModel):
    __root__: List[Api]


class Event(BaseModel):
    name_: Optional[str] = Field(None, alias='name')


class Result(BaseModel):
    event: Optional[Event] = None
