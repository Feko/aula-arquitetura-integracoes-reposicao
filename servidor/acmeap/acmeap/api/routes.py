# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.clientes import Clientes
from .api.clientes_cpf import ClientesCpf
from .api.instalacoes import Instalacoes
from .api.instalacoes_codigo import InstalacoesCodigo
from .api.instalacoes_cpf_cpf import InstalacoesCpfCpf
from .api.faturas import Faturas
from .api.faturas_codigo import FaturasCodigo
from .api.faturas_cpf_cpf import FaturasCpfCpf


routes = [
    dict(resource=Clientes, urls=['/clientes'], endpoint='clientes'),
    dict(resource=ClientesCpf, urls=['/clientes/<int:cpf>'], endpoint='clientes_cpf'),
    dict(resource=Instalacoes, urls=['/instalacoes'], endpoint='instalacoes'),
    dict(resource=InstalacoesCodigo, urls=['/instalacoes/<int:codigo>'], endpoint='instalacoes_codigo'),
    dict(resource=InstalacoesCpfCpf, urls=['/instalacoes/cpf/<int:cpf>'], endpoint='instalacoes_cpf_cpf'),
    dict(resource=Faturas, urls=['/faturas'], endpoint='faturas'),
    dict(resource=FaturasCodigo, urls=['/faturas/<int:codigo>'], endpoint='faturas_codigo'),
    dict(resource=FaturasCpfCpf, urls=['/faturas/cpf/<int:cpf>'], endpoint='faturas_cpf_cpf'),
]