from flask import Blueprint, jsonify
from companies.utils import get_company_info

company_bp = Blueprint('company_bp', __name__)

@company_bp.route('/', methods=['GET'])
def get_companies():
    companies = get_company_info()
    return jsonify(companies)

@company_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = get_company_info(company_id)
    if company:
        return jsonify(company)
    else:
        return jsonify({'error': 'Company not found'}), 404

