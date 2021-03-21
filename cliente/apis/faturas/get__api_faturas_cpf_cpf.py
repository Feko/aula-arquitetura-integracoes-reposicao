from __future__ import annotations

import datetime
import pydantic
import typing

from pydantic import BaseModel

from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest
from swagger_codegen.api import json
class Fatura(BaseModel):
    codigo: typing.Optional[int]  = None
    cpf: typing.Optional[str]  = None
    instalacao: typing.Optional[int]  = None
    leitura: typing.Optional[datetime.datetime]  = None
    valor_fatura: typing.Optional[float]  = None
    valor_leitura: typing.Optional[float]  = None
    vencimento: typing.Optional[datetime.datetime]  = None

def make_request(self: BaseApi,


    cpf: int,

) -> Fatura:
    """Deprecated, utilizar query string"""

    
    body = None
    

    m = ApiRequest(
        method="GET",
        path="/api/faturas/cpf/{cpf}".format(
            
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
            
                "*/*": Fatura,
            
        },
    
    }, m)