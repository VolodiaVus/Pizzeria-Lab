from flask import Blueprint, jsonify, request
from my_project.auth.service.CustomerService import CustomerService
from my_project.auth.domain.Customer import Customer

customer_bp = Blueprint('customers', __name__, url_prefix='/customers')
customer_service = CustomerService()

def _get_customer_from_json(data, idCustomers=None):
    return Customer(
        idCustomers=idCustomers,
        name=data.get('name'),
        phone=data.get('phone'),
        email=data.get('email')
    )

@customer_bp.route('/', methods=['GET'])
def get_all_customers():
    customers = customer_service.find_all()
    return jsonify([c.to_dict() for c in customers]), 200

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customer_service.find_by_id(customer_id)
    if customer:
        return jsonify(customer.to_dict()), 200
    return jsonify({"message": "Customer not found"}), 404

@customer_bp.route('/', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        new_customer = _get_customer_from_json(data)
        created_customer = customer_service.create(new_customer)
        return jsonify(created_customer.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    updated_customer_data = _get_customer_from_json(data, idCustomers=customer_id)
    updated_customer = customer_service.update(customer_id, updated_customer_data)

    if updated_customer:
        return jsonify(updated_customer.to_dict()), 200
    return jsonify({"message": "Customer not found"}), 404


@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_service.delete(customer_id):
        return jsonify({"message": f"Customer with ID {customer_id} deleted"}), 200
    return jsonify({"message": "Customer not found"}), 404