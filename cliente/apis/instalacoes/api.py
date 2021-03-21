from __future__ import annotations

from swagger_codegen.api.base import BaseApi

from . import get__api_instalacoes
from . import post__api_instalacoes
from . import get__api_instalacoes_codigo
from . import get__api_instalacoes_cpf_cpf
class InstalacoesApi(BaseApi):
    get__api_instalacoes = get__api_instalacoes.make_request
    post__api_instalacoes = post__api_instalacoes.make_request
    get__api_instalacoes_codigo = get__api_instalacoes_codigo.make_request
    get__api_instalacoes_cpf_cpf = get__api_instalacoes_cpf_cpf.make_request