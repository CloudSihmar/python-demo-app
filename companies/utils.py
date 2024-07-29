def get_company_info(company_id=None):
    companies = [
        {'id': 1, 'name': 'Tech Solutions', 'industry': 'Technology'},
        {'id': 2, 'name': 'Health Plus', 'industry': 'Healthcare'},
    ]
    
    if company_id is None:
        return companies
    
    for company in companies:
        if company['id'] == company_id:
            return company
    
    return None

