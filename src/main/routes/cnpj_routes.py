from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.cnpj_composer.cnpj_create_account_composer import cnpj_create_account_composer
from src.main.composer.cnpj_composer.cnpj_list_account_composer import cnpj_list_account_composer
from src.main.composer.cnpj_composer.cnpj_saque_composer import cnpj_saque_composer
from src.main.composer.cnpj_composer.cnpj_extrato_composer import cnpj_extrato_composer

cnpj_route_bp = Blueprint("cnpj_routes", __name__)

@cnpj_route_bp.route("/cnpj_create", methods=["POST"])
def create_account():
    try:
        http_request = HttpRequest(body=request.json)
        view = cnpj_create_account_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except ValueError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400
    
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500
    
@cnpj_route_bp.route("/cnpj_list", methods=["GET"])
def list_account():
    try:
        http_request = HttpRequest()
        view = cnpj_list_account_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except ValueError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400
    
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500
    
@cnpj_route_bp.route("/cnpj_saque", methods=["POST"])
def saque():
    try:

        cliente_id = request.args.get("id")
        valor_saque = request.json.get("valor_saque")

        http_request = HttpRequest(
                    body={"valor_saque": valor_saque},
                    param={"id": cliente_id}
                    )
        view = cnpj_saque_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except ValueError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400
    
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": "Erro ao processar a requisição"
        }), 500
    
@cnpj_route_bp.route("/cnpj_extrato", methods=["GET"])
def extrato():
    try:
        
        cliente_id = request.args.get("id")

        http_request = HttpRequest(
            body=None,
            param={"id": cliente_id}
        )
        view = cnpj_extrato_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except ValueError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400
    
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": "Erro ao processar a requisição"
        }), 500