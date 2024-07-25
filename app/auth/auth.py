# from flask import jsonify, request
# from flask_jwt_extended import JWTManager, create_access_token
# from app import app # import Flask app instance

# jwt = JWTManager(app)

# class AuthService:

#     def authenticate(username, password):
#         username = request.json.get('username', None)
#         password = request.json.get('password', None)

#         if username == 'admin' and password == 'password':
#             access_token = create_access_token(identity=username)
#             return jsonify(access_token=access_token), 200
#         else:
#             return jsonify({"Msg": "Invalid username or password"}), 401
    
    