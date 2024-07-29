import os
from flask import Flask
from flask_cors import CORS
from api.blog_endpoint import blog_bp
from flask_jwt_extended import JWTManager


app = Flask(__name__)
origins = ["http://localhost:3000", "http://khai-blog-client.s3-website-us-east-1.amazonaws.com/"]
CORS(app, supports_credentials=True, origins=origins[1])

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(blog_bp)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)