#include <iostream>
#include <string>
#include <vector>
#include "Employees.h"

std::string screen(Employee employee)
{
     std::string s;

     s = "Name: " + employee.getName() + " " + employee.getType() +
          ", Duration: " + std::to_string(employee.getLongevity()) +
          " years, Vacation Accrued: ";
     if (employee.getVacation() != NULL)
     {
          s += std::to_string(employee.getVacation());
          s += " days";
     }
     else
     {
          s += "None";
     }

     return s;
}

void screen_list(std::vector<Employee> employees)
{
     for (int i = 0; i < (employees.size() / sizeof(Employee)); i++)
     {
          std::cout << screen(employees[i]);
     }
}