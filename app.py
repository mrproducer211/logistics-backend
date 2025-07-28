from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # ✅ NEW: import CORS
import os

# Import the Shipment and StatusLog models
from models.shipment import db, Shipment
from models.status_log import StatusLog
from routes.shipments import shipment_bp
from routes.status import status_bp
from routes.users import user_bp
from content.routes import content_bp

app = Flask(__name__)

# ✅ Enable CORS so frontend (admin-content.html) can talk to backend
CORS(app)

# Configure the database (using SQLite for local development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(shipment_bp, url_prefix='/api/shipments')
app.register_blueprint(status_bp, url_prefix='/api/shipments')
app.register_blueprint(user_bp)
app.register_blueprint(content_bp)

@app.route('/')
def home():
    return 'Welcome to the Logistics Shipment Tracking Backend!'

# This will create the database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives a port dynamically
    app.run(host="0.0.0.0", port=port)


