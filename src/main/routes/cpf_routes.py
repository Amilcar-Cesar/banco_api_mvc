from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.cpf_composer.cpf_create_account_composer import cpf_create_account_composer
from src.main.composer.cpf_composer.cpf_list_account_composer import cpf_list_account_composer
from src.main.composer.cpf_composer.cpf_saque_composer import cpf_saque_composer
from src.main.composer.cpf_composer.cpf_extrato_composer import cpf_extrato_composer

cpf_route_bp = Blueprint("cpf_routes", __name__)

@cpf_route_bp.route("/cpf_create", methods=["POST"])
def create_account():
    http_request = HttpRequest(body=request.json)
    view = cpf_create_account_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
    
@cpf_route_bp.route("/cpf_list", methods=["GET"])
def list_account():
    http_request = HttpRequest()
    view = cpf_list_account_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
    
@cpf_route_bp.route("/cpf_saque", methods=["POST"])
def saque():
    cliente_id = request.args.get("id", type=int)
    valor_saque = request.json.get("valor_saque")
    http_request = HttpRequest(
                body={"valor_saque": valor_saque},
                param={"id": cliente_id}
                )
    view = cpf_saque_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
    
@cpf_route_bp.route("/cpf_extrato", methods=["GET"])
def extrato():
    cliente_id = request.args.get("id", type=int)

    http_request = HttpRequest(
        body=None,
        param={"id": cliente_id}
    )
    view = cpf_extrato_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
