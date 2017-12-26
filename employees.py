import math


class Employee(object):
    """Base class for all employees.

    Args:
        name (str): Employee's first and last name
        longevity (float): Years the employee has been with the company
    """
    def __init__(self, name, longevity):
        self.name = name
        self.longevity = longevity


class Fulltime(Employee):
    """Class for full-time permanent employees. Each full-time employee will
    accrue five days of vacation for each full year of service. Employee's type
    will appear as '[FT]'.

    Args:
        name (str): Employee's first and last name
        longevity (float): Years the employee has been with the company
    """
    def __init__(self, name, longevity):
        super(Fulltime, self).__init__(name, longevity)
        self.type = '[FT]'
        self.vacation = int(max([0, 5 * math.floor(longevity)]))


class Contractor(Employee):
    """Class for contracted employees. Contractors do not accrue vacation time.
    Employee's type will appear as '[C]'.

    Args:
        name (str): Employee's first and last name
        longevity (float): Years the employee has been with the company
    """
    def __init__(self, name, longevity):
        super(Contractor, self).__init__(name, longevity)
        self.type = '[C]'
        self.vacation = None


class Temporary(Employee):
    """Class for temporary employees. Temporary employees do not accrue vacation
    time. Employee's type will appear as '[T]'.

    Args:
        name (str): Employee's first and last name
        longevity (float): Years the employee has been with the company
    """
    def __init__(self, name, longevity):
        super(Temporary, self).__init__(name, longevity)
        self.type = '[T]'
        self.vacation = None
