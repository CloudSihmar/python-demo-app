def get_employee_info(employee_id=None):
    employees = [
        {'id': 1, 'name': 'John Doe', 'position': 'Software Engineer'},
        {'id': 2, 'name': 'Jane Smith', 'position': 'Data Scientist'},
    ]
    
    if employee_id is None:
        return employees
    
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    
    return None

