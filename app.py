from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Import your models and blueprints
from models.shipment import db, Shipment
from models.status_log import StatusLog
from routes.shipments import shipment_bp
from routes.status import status_bp
from content.routes import content_bp
from routes.users import user_bp  # Only if you have this file

# ✅ Correct __name__ usage
app = Flask(__name__)
CORS(app)

# ✅ Correct DB setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ✅ Register blueprints
app.register_blueprint(shipment_bp, url_prefix='/api/shipments')
app.register_blueprint(status_bp, url_prefix='/api/shipments')
app.register_blueprint(content_bp)
app.register_blueprint(user_bp, url_prefix='/api/user')  # Remove if not using

# ✅ Basic route to confirm Render deploy
@app.route('/')
def home():
    return '✅ Logistics Backend Running on Render!'

# ✅ Create DB tables
with app.app_context():
    db.create_all()

# ✅ VERY IMPORTANT FOR RENDER TO DETECT YOUR PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
