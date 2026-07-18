from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import routes
from routes.products import product_bp
from routes.users import user_bp
from routes.orders import order_bp
from routes.payments import payment_bp

app.register_blueprint(product_bp, url_prefix="/api/products")
app.register_blueprint(user_bp, url_prefix="/api/users")
app.register_blueprint(order_bp, url_prefix="/api/orders")
app.register_blueprint(payment_bp, url_prefix="/api/payments")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
