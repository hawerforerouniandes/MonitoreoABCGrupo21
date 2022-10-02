from functools import wraps
import json

from flask import jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request


# Here is a custom decorator that verifies the JWT is present in the request,
# as well as insuring that the JWT has a claim indicating that this user is
# an administrator
def operador_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['role'] == 'OPERADOR':
                return fn(*args, **kwargs)
            else:
                return {"msg":"Error: Servicio permitido solo para operadores"}, 403

        return decorator

    return wrapper

def cliente_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['role'] == 'CLIENTE':
                return fn(*args, **kwargs)
            else:
                return {"msg":"Error: Servicio permitido solo para clientes"}, 403

        return decorator

    return wrapper