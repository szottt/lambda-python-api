from chalice import Chalice


app = Chalice(app_name="products")


products = {
    "products": [
        {"product": "arroz", "amount": "2"},
        {"product": "feijão", "amount": "3"},
        {"product": "carne", "amount": "1"},
    ]
}


@app.route("/product", methods=["POST"])
def create_product():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} criado com sucesso!",
    }
    return response


@app.route("/product", methods=["PUT"])
def create_product():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} criado com sucesso!",
    }
    return response


@app.route("/product", methods=["DELETE"])
def create_product():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} criado com sucesso!",
    }
    return response


@app.route("/product", methods=["GET"])
def create_product():
    response = {"statusCode": 200, "body": products}
    return response


@app.route("/product/{id}", methods=["GET"])
def get_user_id(id):
    response = {
        "statusCode": 200,
        "body": {id: {"product": "arroz", "amount": "2"}},
    }
    return response


################################################################### company
