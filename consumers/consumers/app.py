from chalice import Chalice

app = Chalice(app_name="consumers")

users = {
    "users": [
        {"name": "usuário1", "phone": "47999999999"},
        {"name": "usuário2", "phone": "47999999999"},
        {"name": "usuário3", "phone": "47999999999"},
    ]
}


companies = {
    "companies": [
        {"name": "empresa1", "telefone": "47999999999"},
        {"name": "empresa2", "telefone": "47999999999"},
        {"name": "empresa3", "telefone": "47999999999"},
    ]
}


@app.route("/consumers/person", methods=["POST"])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requests_params} criado com sucesso!",
    }
    return response


@app.route("/consumers/person", methods=["PUT"])
def put_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requests_params} atualizado com sucesso!",
    }
    return response


@app.route("/consumers/person", methods=["DELETE"])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requests_params} deletado com sucesso!",
    }
    return response


@app.route("/consumers/person", methods=["GET"])
def get_user():
    response = {"statusCode": 200, "body": users}
    return response


@app.route("/consumers/person/{id}", methods=["GET"])
def get_user_id(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "usuário1", "phone": "47999999999"}},
    }
    return response


@app.route("/consumers/company", methods=["POST"])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!",
    }
    return response


@app.route("/consumers/company", methods=["PUT"])
def put_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!",
    }
    return response


@app.route("/consumers/company", methods=["DELETE"])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} deletada com sucesso!",
    }
    return response


@app.route("/consumers/company", methods=["GET"])
def get_user():
    response = {"statusCode": 200, "body": companies}
    return response


@app.route("/consumers/company/{id}", methods=["GET"])
def get_user_id(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "empresa1", "telefone": "47999999999"}},
    }
    return response
