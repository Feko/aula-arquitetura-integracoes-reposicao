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

    __request__: Cliente,


) -> None:
    """Cadastrar um novo cliente"""

    
    body = __request__
    

    m = ApiRequest(
        method="POST",
        path="/api/clientes".format(
            
        ),
        content_type="application/json",
        body=body,
        headers=self._only_provided({
        }),
        query_params=self._only_provided({
        }),
        cookies=self._only_provided({
        }),
    )
    return self.make_request({
    
        "201": {
            
                "default": None,
            
        },
    
        "405": {
            
                "default": None,
            
        },
    
    }, m)