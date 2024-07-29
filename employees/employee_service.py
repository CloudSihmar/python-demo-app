from flask import Blueprint, jsonify
from employees.utils import get_employee_info

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = get_employee_info()
    return jsonify(employees)

@employee_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = get_employee_info(employee_id)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404

