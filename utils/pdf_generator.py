from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_receipt(data):
    file_path = data['pdf_path']
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 780, f"Tracking Number: {data['tracking_number']}")

    # Sender Info
    c.drawString(100, 760, f"Sender Name: {data['sender']['name']}")
    c.drawString(100, 745, f"Sender Email: {data['sender']['email']}")
    c.drawString(100, 730, f"Sender Phone: {data['sender']['phone']}")
    c.drawString(100, 715, f"Sender Address: {data['sender']['address']}")

    # Receiver Info
    c.drawString(100, 695, f"Receiver Name: {data['receiver']['name']}")
    c.drawString(100, 680, f"Receiver Email: {data['receiver']['email']}")
    c.drawString(100, 665, f"Receiver Phone: {data['receiver']['phone']}")
    c.drawString(100, 650, f"Receiver Address: {data['receiver']['address']}")

    # Status
    c.drawString(100, 630, f"Current Status: {data['status']}")
    c.drawString(100, 615, f"Estimated Delivery: {data['estimated_delivery']}")

    c.save()
