import os
from flask import Flask
from flask_cors import CORS
from api.blog_endpoint import blog_bp
from flask_jwt_extended import JWTManager

# config = {
#     'MONGO_URI': os.getenv('MONGO_URI'),
#     'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY')
# }

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# CORS(app, resources={r"/*": {
#     "origins": "*",  # Be more specific in production
#     "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
#     "allow_headers": ["Authorization", "Content-Type"]
# }})

# app.config.from_object(config)


# app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
# app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
# app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
# app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# mail = Mail(app)

# Register Blueprints
app.register_blueprint(blog_bp)



if __name__ == '__main__':
    app.run(port=5000, debug=True)