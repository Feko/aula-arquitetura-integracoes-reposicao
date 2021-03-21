from __future__ import annotations

from swagger_codegen.api.base import BaseApi

from . import post__api_clientes
from . import get__api_clientes
from . import get__api_clientes_cpf
class ClientesApi(BaseApi):
    post__api_clientes = post__api_clientes.make_request
    get__api_clientes = get__api_clientes.make_request
    get__api_clientes_cpf = get__api_clientes_cpf.make_request