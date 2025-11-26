from flask import Flask
from my_project.auth.controller.customer_controller import customer_bp
from my_project.auth.controller.complex_controller import complex_bp

app = Flask(__name__)

app.register_blueprint(customer_bp)
app.register_blueprint(complex_bp)

if __name__ == '__main__':
    app.run(debug=True)