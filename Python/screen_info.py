def screen(employee):
    """Creates a string containing an employee's employment information.

    Args:
        employee (Employee): employees.Employee object describing the employee

    Returns:
        str: A string containing the employee's name, employment type, number of
            years with the company, and accrued vacation time
    """
    output = 'Name: {} {}, ' \
             'Duration: {} years, ' \
             'Vacation Accrued: {}{}'.format(employee.name,
                                             employee.type,
                                             employee.longevity,
                                             employee.vacation,
                                             ' days' if employee.vacation is not
                                             None else '')
    return output


def screen_list(employees_list):
    """Prints employment data for a list of employees.
    Args:
        employees_list (List[Employee]): A list of employees.Employee objects
            describing the employees whose data should be printed
    """
    for employee in employees_list:
        print screen(employee)
