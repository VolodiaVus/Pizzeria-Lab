from flask import Blueprint, jsonify
from my_project.auth.service.CustomerService import CustomerService
from my_project.auth.service.ProductService import ProductService

complex_bp = Blueprint('complex', __name__, url_prefix='/complex')
customer_service = CustomerService()
product_service = ProductService()

@complex_bp.route('/customers/<int:customer_id>/addresses', methods=['GET'])
def get_customer_with_addresses(customer_id: int):
    try:
        customer = customer_service.find_by_id_with_addresses(customer_id)
        if customer:
            return jsonify(customer.to_dict()), 200
        return jsonify({"message": "Customer not found"}), 404
    except AttributeError:
        return jsonify({"error": "Service method not implemented"}), 501

@complex_bp.route('/products/<int:product_id>/ingredients', methods=['GET'])
def get_pizza_with_ingredients(product_id: int):
    try:
        product = product_service.find_pizza_with_ingredients(product_id)
        if product:
            return jsonify(product.to_dict()), 200
        return jsonify({"message": "Product not found"}), 404
    except AttributeError:
        return jsonify({"error": "Service method not implemented"}), 501