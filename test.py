import employees
import screen_info
import unittest


class EmployeesTest(unittest.TestCase):
    def test_fulltime_type(self):
        """Asserts a full time employee's type is '[FT]'"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=1.0)
        self.assertTrue(shepard.type == '[FT]')

    def test_contractor_type(self):
        """Asserts a contractor's type is '[C]'"""
        zaeed = employees.Contractor(name='Zaeed Massani', longevity=1.0)
        self.assertTrue(zaeed.type == '[C]')

    def test_temporary_type(self):
        """Asserts a temporary employee's type is '[T]'"""
        thane = employees.Temporary(name='Thane Krios', longevity=0.5)
        self.assertTrue(thane.type == '[T]')

    def test_ft_vacation_negative(self):
        """Asserts a full time employee with less than zero years of employment
        has 0 vacation days"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=-3)
        self.assertEqual(shepard.vacation, 0)

    def test_ft_vacation_0(self):
        """Asserts a full time employee with zero years of employment has 0
        vacation days"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=0)
        self.assertEqual(shepard.vacation, 0)

    def test_ft_vacation_less_than_1(self):
        """Asserts a full time employee with less than one but more than zero
        years of employment has 0 vacation days"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=0.8)
        self.assertEqual(shepard.vacation, 0)

    def test_ft_vacation_1(self):
        """Asserts a full time employee with one year of employment has 5
        vacation days"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=1.0)
        self.assertEqual(shepard.vacation, 5)

    def test_ft_vacation_more_than_1(self):
        """Asserts a full time employee with 2.5 years of employment has 10
        vacation days"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=2.5)
        self.assertEqual(shepard.vacation, 10)

    def test_contractor_vacation(self):
        """Asserts a contractor with one year of employment has None for
        vacation days"""
        zaeed = employees.Contractor(name='Zaeed Massani', longevity=1.0)
        self.assertIsNone(zaeed.vacation)

    def test_temporary_vacation(self):
        """Asserts a temporary employee with one year of employment has None
        for vacation days"""
        thane = employees.Temporary(name='Thane Krios', longevity=1.0)
        self.assertIsNone(thane.vacation)

    def test_screen_ft(self):
        """Asserts a full time employee's data is returned correctly by the
        screen function"""
        shepard = employees.Fulltime(name='Jane Shepard', longevity=3.0)
        self.assertEqual('Name: Jane Shepard [FT], Duration: 3.0 years, '
                         'Vacation Accrued: 15 days',
                         screen_info.screen(shepard))

    def test_screen_contractor(self):
        """Asserts a contractor's data is returned correctly by the screen
        function"""
        zaeed = employees.Contractor(name='Zaeed Massani', longevity=1.0)
        self.assertEqual('Name: Zaeed Massani [C], Duration: 1.0 years, '
                         'Vacation Accrued: None',
                         screen_info.screen(zaeed))

    def test_screen_temp(self):
        """Asserts a temporary employee's data is returned correctly by the
        screen function"""
        thane = employees.Temporary(name='Thane Krios', longevity=0.5)
        self.assertEqual('Name: Thane Krios [T], Duration: 0.5 years, '
                         'Vacation Accrued: None',
                         screen_info.screen(thane))
