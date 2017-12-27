#ifndef EMPLOYEES_H
#define EMPLOYEES_H

#include <string>

class Employee
{
public:
     // Getters
     std::string getName();
     float getLongevity();
     std::string getType();
     int getVacation();

     // Setters
     void setName(std::string newName);
     void setLongevity(float newLongevity);
     void setType(std::string newType);
     void setVacation(int newVacation);

private:
     std::string name;
     float longevity;
     std::string type;
     int vacation;
};

class Fulltime : public Employee
{
public:
     // Constructor
     Fulltime(std::string name, float longevity);
};

class Contractor : public Employee
{
public:
     // Constructor
     Contractor(std::string name, float longevity);
};

class Temporary : public Employee
{
public:
     // Constructor
     Temporary(std::string name, float longevity);
};

#endif