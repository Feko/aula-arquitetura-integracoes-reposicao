# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class ClientesCpf(Resource):

    def get(self, cpf):

        return {}, 200, None