from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.cnpj_composer.cnpj_create_account_composer import cpf_create_account_composer