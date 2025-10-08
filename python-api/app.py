"""
Customer Management API
A Flask-based REST API for managing customer data
"""

from flask import Flask, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

# In-memory database (for demo purposes)
customers = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "555-0100",
        "created_at": "2024-01-15",
        "status": "active"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "555-0101",
        "created_at": "2024-02-20",
        "status": "active"
    },
    {
        "id": 3,
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com",
        "phone": "555-0102",
        "created_at": "2024-03-10",
        "status": "inactive"
    }
]

@app.route('/')
def home():
    """Welcome endpoint"""
    return jsonify({
        "message": "Welcome to the Customer Management API",
        "version": "1.0.0",
        "endpoints": {
            "customers": "/api/customers",
            "customer_by_id": "/api/customers/<id>"
        }
    })

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    status_filter = request.args.get('status')
    
    if status_filter:
        filtered = [c for c in customers if c['status'] == status_filter]
        return jsonify(filtered)
    
    return jsonify(customers)

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get a specific customer by ID"""
    customer = next((c for c in customers if c['id'] == customer_id), None)
    
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    
    return jsonify(customer)

@app.route('/api/customers', methods=['POST'])
def create_customer():
    """Create a new customer"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['name', 'email', 'phone']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    # Create new customer
    new_id = max([c['id'] for c in customers]) + 1
    new_customer = {
        "id": new_id,
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone'],
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "status": data.get('status', 'active')
    }
    
    customers.append(new_customer)
    return jsonify(new_customer), 201

@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update an existing customer"""
    customer = next((c for c in customers if c['id'] == customer_id), None)
    
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    
    data = request.get_json()
    
    # Update fields
    if 'name' in data:
        customer['name'] = data['name']
    if 'email' in data:
        customer['email'] = data['email']
    if 'phone' in data:
        customer['phone'] = data['phone']
    if 'status' in data:
        customer['status'] = data['status']
    
    return jsonify(customer)

@app.route('/api/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete a customer"""
    global customers
    customer = next((c for c in customers if c['id'] == customer_id), None)
    
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    
    customers = [c for c in customers if c['id'] != customer_id]
    return jsonify({"message": "Customer deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
