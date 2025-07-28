import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# The db instance will be initialized in app.py
from .shipment import db

class StatusLog(db.Model):
    __tablename__ = 'status_logs'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # Unique ID
    shipment_id = db.Column(db.String(36), db.ForeignKey('shipments.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100), nullable=True)
    coordinates = db.Column(db.String(100), nullable=True)  # Optional: e.g., 'lat,lng'
    note = db.Column(db.Text, nullable=True) 