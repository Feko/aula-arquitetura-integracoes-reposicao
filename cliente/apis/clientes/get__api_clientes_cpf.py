from __future__ import annotations

import datetime
import pydantic
import typing

from pydantic import BaseModel

from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest
from swagger_codegen.api import json
class Cliente(BaseModel):
    cpf: typing.Optional[str]  = None
    endereco: typing.Optional[str]  = None
    nascimento: typing.Optional[datetime.datetime]  = None
    nome: typing.Optional[str]  = None

def make_request(self: BaseApi,


    cpf: int,

) -> Cliente:
    """Obtem um cliente usando CPF como chave"""

    
    body = None
    

    m = ApiRequest(
        method="GET",
        path="/api/clientes/{cpf}".format(
            
                cpf=cpf,
            
        ),
        content_type=None,
        body=body,
        headers=self._only_provided({
        }),
        query_params=self._only_provided({
        }),
        cookies=self._only_provided({
        }),
    )
    return self.make_request({
    
        "200": {
            
                "application/json": Cliente,
            
                "application/xml": Cliente,
            
        },
    
        "400": {
            
                "default": None,
            
        },
    
        "404": {
            
                "default": None,
            
        },
    
    }, m)