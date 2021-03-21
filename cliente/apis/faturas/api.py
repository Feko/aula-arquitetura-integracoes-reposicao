from __future__ import annotations

from swagger_codegen.api.base import BaseApi

from . import get__api_faturas
from . import post__api_faturas
from . import get__api_faturas_codigo
from . import get__api_faturas_cpf_cpf
class FaturasApi(BaseApi):
    get__api_faturas = get__api_faturas.make_request
    post__api_faturas = post__api_faturas.make_request
    get__api_faturas_codigo = get__api_faturas_codigo.make_request
    get__api_faturas_cpf_cpf = get__api_faturas_cpf_cpf.make_request