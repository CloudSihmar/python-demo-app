from flask import Flask
from employees.employee_service import employee_bp
from companies.company_service import company_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(employee_bp, url_prefix='/employees')
app.register_blueprint(company_bp, url_prefix='/companies')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

