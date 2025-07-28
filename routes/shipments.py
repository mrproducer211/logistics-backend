from flask import Blueprint, request, jsonify
from models.shipment import db, Shipment
from utils.pdf_generator import generate_pdf_receipt
from datetime import datetime
import uuid

shipment_bp = Blueprint('shipment_bp', __name__)

@shipment_bp.route('/', methods=['POST', 'OPTIONS'])  # Accept POST and OPTIONS
def create_shipment():
    if request.method == 'OPTIONS':
        return jsonify({'ok': True}), 200  # Handle CORS preflight

    data = request.get_json()

    # Extract shipment data from the request
    sender_name = data.get('sender_name')
    sender_email = data.get('sender_email')
    sender_phone = data.get('sender_phone')
    sender_address = data.get('sender_address')
    receiver_name = data.get('receiver_name')
    receiver_phone = data.get('receiver_phone')
    receiver_address = data.get('receiver_address')
    package_type = data.get('package_type')
    weight = data.get('weight')
    shipment_cost = data.get('shipment_cost')
    estimated_delivery_date = data.get('estimated_delivery_date')

    # Generate a unique tracking number (simple example)
    tracking_number = f'TRK{str(uuid.uuid4())[:8].upper()}'

    # Convert estimated_delivery_date to datetime if provided
    est_delivery = None
    if estimated_delivery_date:
        try:
            est_delivery = datetime.strptime(estimated_delivery_date, '%Y-%m-%d')
        except Exception:
            est_delivery = None

    # Create the shipment object
    shipment = Shipment(
        tracking_number=tracking_number,
        sender_name=sender_name,
        sender_email=sender_email,
        sender_phone=sender_phone,
        sender_address=sender_address,
        receiver_name=receiver_name,
        receiver_phone=receiver_phone,
        receiver_address=receiver_address,
        package_type=package_type,
        weight=weight,
        shipment_cost=shipment_cost,
        estimated_delivery_date=est_delivery,
        status='Registered'
    )
    db.session.add(shipment)
    db.session.commit()

    # Generate PDF receipt and save the file path
    pdf_path = generate_pdf_receipt(shipment)
    shipment.pdf_url = pdf_path
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Shipment registered successfully!',
        'tracking_number': shipment.tracking_number,
        'pdf_url': shipment.pdf_url
    }), 201

@shipment_bp.route('/all', methods=['GET'])
def get_all_shipments():
    shipments = Shipment.query.all()
    shipment_list = []
    for s in shipments:
        shipment_list.append({
            'id': s.id,
            'tracking_number': s.tracking_number,
            'sender_name': s.sender_name,
            'receiver_name': s.receiver_name,
            'status': s.status,
            'estimated_delivery_date': s.estimated_delivery_date.strftime('%Y-%m-%d') if s.estimated_delivery_date else None,
            'pdf_url': s.pdf_url
        })
    return jsonify({'shipments': shipment_list, 'success': True})
