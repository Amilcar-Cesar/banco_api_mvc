from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.errors.error_handler import handle_error
from src.main.composer.cnpj_composer.cnpj_create_account_composer import cnpj_create_account_composer
from src.main.composer.cnpj_composer.cnpj_list_account_composer import cnpj_list_account_composer
from src.main.composer.cnpj_composer.cnpj_saque_composer import cnpj_saque_composer
from src.main.composer.cnpj_composer.cnpj_extrato_composer import cnpj_extrato_composer

cnpj_route_bp = Blueprint("cnpj_routes", __name__)

@cnpj_route_bp.route("/cnpj_create", methods=["POST"])
def create_account():
    http_request = HttpRequest(body=request.json)
    view = cnpj_create_account_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

        
    
@cnpj_route_bp.route("/cnpj_list", methods=["GET"])
def list_account():
    http_request = HttpRequest()
    view = cnpj_list_account_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
    
    
@cnpj_route_bp.route("/cnpj_saque", methods=["POST"])
def saque():
    cliente_id = request.args.get("id", type=int)
    valor_saque = request.json.get("valor_saque")

    http_request = HttpRequest(
                body={"valor_saque": valor_saque},
                param={"id": cliente_id}
                )
    view = cnpj_saque_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
    
@cnpj_route_bp.route("/cnpj_extrato", methods=["GET"])
def extrato():
    cliente_id = request.args.get("id", type=int)

    http_request = HttpRequest(
        body=None,
        param={"id": cliente_id}
    )
    view = cnpj_extrato_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
