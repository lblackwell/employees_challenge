#include "Employees.h"
#include <string>

// Constructors
Fulltime::Fulltime(std::string name, float longevity)
{
     setName(name);
     setLongevity(longevity);

     std::string t = "[FT]";
     setType(t);

     int v;
     v = static_cast<int>(getVacation()) * 5;
     setVacation(v);
}

Contractor::Contractor(std::string name, float longevity)
{
     setName(name);
     setLongevity(longevity);

     std::string t = "[C]";
     setType(t);

     int v;
     v = NULL;
     setVacation(v);
}

Temporary::Temporary(std::string name, float longevity)
{
     setName(name);
     setLongevity(longevity);

     std::string t = "[T]";
     setType(t);

     int v;
     v = NULL;
     setVacation(v);
}

// Getters
std::string Employee::getName()
{
     return name;
}

float Employee::getLongevity()
{
     return longevity;
}

std::string Employee::getType()
{
     return type;
}

int Employee::getVacation()
{
     return vacation;
}

// Setters
void Employee::setName(std::string newName)
{
     name = newName;
}

void Employee::setLongevity(float newLongevity)
{
     longevity = newLongevity;
}

void Employee::setType(std::string newType)
{
     type = newType;
}

void Employee::setVacation(int newVacation)
{
     vacation = newVacation;
}